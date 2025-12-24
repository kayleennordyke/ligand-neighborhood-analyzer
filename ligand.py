from CIF_parser import read_cif
import numpy as np
import os
from exceptions import NotALigand

    
class NotALigand(Exception):
    # not a ligand
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"{self.message}"
    
def create_ligand(residue_code):
    """Creates a Ligand from a Residue."""
    residue_code = residue_code + ".cif"
    DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
    path = os.path.join(DATA_DIR, residue_code)
    return Ligand.from_cif(path)

class Ligand:
    def __init__(self):
        pass

    @classmethod
    def from_cif(cls, path):
        res = read_cif(path)
        key = next(iter(res))

        # is ligand?
        type = res[key]['_atom_site.group_PDB']

        if type != 'HETATM':
            raise NotALigand(f"Not a ligand, is instead a {type}")
    
        # residue name
        name = res[key]['_atom_site.label_comp_id']

        # cooredinates # in angstroms
        coord = res[key]['_atom_site.Cartn_x/y/z']

        return Ligand(type, name, coord)