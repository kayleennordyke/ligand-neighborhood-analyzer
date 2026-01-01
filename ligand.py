from helpers.CIF_parser import read_cif
import numpy as np
import os
from helpers.exceptions import NotALigand
from helpers.mappings import amino_set
    
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
        """
        Requirements
        ------------
        type: list, name: list, 
        xcoord: list, ycoord: list , zcoord: list,
        chainID: list, resnum: list, inscode: list
        """
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

        res = read_cif(path)
        block = next(iter(res))
        res = res[block]

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
        self.residue = {}

        for i in range(num_atoms):
            key = (self.name[i], self.chainID[i], self.resnum[i], self.inscode[i])
            if self.name[i] in amino_set:
                if key not in self.residue:
                    self.residue[key] = []
                self.residue[key].append(np.array([self.xcoord[i], self.ycoord[i], self.zcoord[i]]))
            
        return self.residue

    @property 
    def ligands(self):
        num_atoms = len(self)
        self.ligand = {}

        for i in range(num_atoms):
            key = (self.name[i], self.chainID[i], self.resnum[i], self.inscode[i])
            if (self.name[i] not in amino_set and self.type[i] == 'HETATM' and self.name[i] != 'HOH'):
                if key not in self.ligand:
                    self.ligand[key] = []
                self.ligand[key].append(np.array([self.xcoord[i], self.ycoord[i], self.zcoord[i]]))
        
        return self.ligand

    ## TODO, anything that isn't a residue or ligand like h2o or an ion
    def randos(self):
        randos = {}
        pass

    def calculate_distance(self, coord1, coord2):
        """
        Calculate the minimum distance between two sets of 3D coordinates.

        Parameters
        ----------
        coord1, coord2 : array-like
            Atomic coordinates with shape (N,3) and (M,3)

        Returns
        -------
        distance : float
            Minimum atom–atom distance
        """
        a = np.asarray(coord1) 
        b = np.asarray(coord2)

        diff = a[:, None, :] - b[None, :, :] 
        dist_sq = (diff ** 2).sum(axis=2)
        distance = np.sqrt(dist_sq.min())
        return distance

    def neighbors(self, max_distance):
        l = self.ligands
        r = self.residues
        
        neighbors = {}

        # BRUTE FORCE - TODO OPTIMIZE
        for lkey, lvalue in l.items():
            for rkey, rvalue in r.items():
                distance = self.calculate_distance(lvalue, rvalue)
                if distance < max_distance:
                    # then residue is neighbor of ligand
                    if lkey not in neighbors:
                        neighbors[lkey] = []
                    neighbors[lkey].append((rkey, distance))
        self.max_distance = max_distance
        
        return neighbors