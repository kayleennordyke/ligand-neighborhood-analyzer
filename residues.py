from CIF_parser import read_cif
import numpy as np
import os

class DimensionError(Exception):
    # For incorrect dimensions
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"{self.message}"
    
def create_residue(residue_code):
    """Creates a residue."""
    residue_code = residue_code + ".cif"
    DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
    path = os.path.join(DATA_DIR, residue_code)
    return Residue.from_cif(path)

class Residue:
    def __init__(self, name, atoms, bonds, one_letter_code, three_letter_code, residue_type):
        self.name = name
        self.atoms = atoms
        self.bonds = bonds
        self.one_letter_code = one_letter_code
        self.three_letter_code = three_letter_code
        self.residue_type = residue_type

        self.atom_ids = self.atoms["atom_ids"]
        self.symbols = self.atoms["symbols"]
        self.coordinates = self.atoms["coordinates"]

    @property
    def n_atoms(self):
        return len(self.atom_ids)
    
    @classmethod
    def from_cif(cls, path):
        res = read_cif(path)
        key = next(iter(res))

        # name
        name = res[key]['_chem_comp.name']

        # three letter code
        three_letter_code = res[key]['_chem_comp.three_letter_code']

        # one letter code
        one_letter_code = res[key]['_chem_comp.one_letter_code']

        # atoms, includes: atoms_id, symbols, coordinates
        x = res[key]['_chem_comp_atom.pdbx_model_cartn_x_ideal']
        y = res[key]['_chem_comp_atom.pdbx_model_cartn_y_ideal']
        z = res[key]['_chem_comp_atom.pdbx_model_cartn_z_ideal']

        atoms = {
            "atom_ids" : res[key]['_chem_comp_atom.atom_id'],
            "symbols" : res[key]['_chem_comp_atom.type_symbol'],
            "coordinates" : np.array([[x[i], y[i], z[i]] for i in range(len(x))])
        }

        # residue type
        residue_type = res[key]['_chem_comp.type']
        if "PEPTIDE" in residue_type.upper():
            residue_type = 'amino_acid'
        elif "DNA" in residue_type or "RNA" in residue_type:
            residue_type = 'nucleic_acid'

        # bonds
        atom1 = res[key]['_chem_comp_bond.atom_id_1']
        atom2 = res[key]['_chem_comp_bond.atom_id_2']
        order = res[key]['_chem_comp_bond.value_order']
        bonds = [(atom1[i], atom2[i], order[i]) for i in range(len(atom1))]

        return Residue(name, atoms, bonds, one_letter_code, three_letter_code, residue_type)
