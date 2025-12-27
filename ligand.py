from CIF_parser import read_cif
import numpy as np
import os
from exceptions import NotALigand
from mappings import amino_set
from residues import create_residue

    
# class NotALigand(Exception):
#     # not a ligand
#     def __init__(self, message):
#         super().__init__(message)
#         self.message = message

#     def __str__(self):
#         return f"{self.message}"
    
def create_structure(residue_code):
    """Creates a Ligand from a Residue."""
    residue_code = residue_code + ".cif"
    DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
    path = os.path.join(DATA_DIR, residue_code)
    return Structure.from_cif(path)

class Structure:
    def __init__(
            self, type: list, name: list, 
            xcoord: list, ycoord: list , zcoord: list,
            chainID: list, resnum: list, inscode: list):
        self.type = type
        self.name = name
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.zcoord = zcoord
        self.chainID = chainID
        self.resnum = resnum
        self.inscode = inscode

    @classmethod
    def from_cif(cls, path):
        print("RUNNING ligand.py from_cif:", __file__)
        

        res = read_cif(path)
        block = next(iter(res))
        res = res[block] 
        
        #print("_atom_site.group_PDB" in res)
        #print([k for k in res.keys() if k.startswith("_atom_site.")])

        # ligand?
        type = res['_atom_site.group_pdb']

        # residue name
        name = res['_atom_site.label_comp_id']

        # coordinates # in angstroms
        xcoord = res['_atom_site.cartn_x']
        ycoord = res['_atom_site.cartn_y']
        zcoord = res['_atom_site.cartn_z']

        # chain id
        chainID = res['_atom_site.label_asym_id']

        # res num
        resnum = res['_atom_site.label_seq_id']

        # insersion code
        inscode = res['_atom_site.pdbx_pdb_ins_code']

        return Structure(type, name, xcoord, ycoord, zcoord, chainID, resnum, inscode)
    
    def __len__(self):
        return len(self.type)
    
    @property
    def residues(self):
        # num of unique atoms
        num_atoms = len(self)
        residues = {}

        for i in range(num_atoms):
            key = (self.name[i], self.chainID[i], self.resnum[i], self.inscode[i])
            if self.name[i] in amino_set:
                if key not in residues:
                    residues[key] = []
                residues[key].append([self.xcoord[i], self.ycoord[i], self.zcoord[i]])
            
        return residues

    @property 
    def ligands(self):
        num_atoms = len(self)
        ligands = {}

        for i in range(num_atoms):
            key = (self.name[i], self.chainID[i], self.resnum[i], self.inscode[i])
            if (self.name[i] not in amino_set and self.type[i] == 'HETATM' and self.name[i] != 'HOH'):
                if key not in ligands:
                    ligands[key] = []
                ligands[key].append([self.xcoord[i], self.ycoord[i], self.zcoord[i]])
        
        return ligands

    def randos(self):
        randos = {}
        pass

    def neighbors(self):
        pass