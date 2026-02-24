import os
import pytest
import numpy as np
from src.ligand_neighborhood.helpers.exceptions import NotALigand
from src.ligand_neighborhood.structure import Structure, create_structure

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


# =====================================================================
# STAGE 1: Basic Constructor
# =====================================================================

@pytest.mark.stage1
def test_constructor_basic_interface():
    """Structure must accept required arguments and expose basic attributes."""
    pass

# =====================================================================
# STAGE 2: Distance function
# =====================================================================

@pytest.mark.stage2
def test_distance_computed_correctly():
    "Make sure that distance is computed correctly"

    # just to initialize
    type = ['ATOM', 'ATOM', 'ATOM', 'ATOM', 'HETATM', 'HETATM', 'HETATM', 'HETATM']
    name = ['GLU', 'GLU', 'GLU', 'GLU', 'TYS', 'TYS', 'TYS', 'TYS']
    xcoord = [15.848, 16.526, 17.547, 14.847, 15.901, 16.482, 15.434, 14.580]
    ycoord = [3.489, 3.246, 3.893, 4.613, 2.361, 2.005, 1.805, 3.049]
    zcoord = [-6.866, -5.518, -5.212, -6.620, -4.748, -3.448, -2.340, -2.234]
    chainID = ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C']
    resnum = [10, 10, 10, 10, 11, 11, 11, 11]
    s = Structure(type, name, xcoord, ycoord, zcoord, chainID, resnum)

    coord1 = [[0, 2, 0], [0, 0, 0], [-1, 3, 0]]
    coord2 = [[0, 1, 0], [0, 1, 2]]
    dist = s._calculate_distance(coord1, coord2)
    assert np.isclose(dist, 1.0)


# =====================================================================
# STAGE 3: Length and residue/ligand grouping
# =====================================================================

@pytest.mark.stage3
def test_structure_length():
    """Structure __len__ equals number of atoms."""
    type = ['ATOM', 'ATOM', 'HETATM', 'HETATM']
    name = ['GLU', 'GLU', 'TYR', 'TYR']
    xcoord = [0.0, 1.0, 2.0, 3.0]
    ycoord = [0.0, 1.0, 2.0, 3.0]
    zcoord = [0.0, 1.0, 2.0, 3.0]
    chainID = ['A', 'A', 'A', 'A']
    resnum = [1, 1, 2, 2]
    s = Structure(type, name, xcoord, ycoord, zcoord, chainID, resnum)
    assert len(s) == 4


@pytest.mark.stage3
def test_residues_and_ligands_properties():
    """residues contains amino acid keys; ligands contains HETATM non-amino keys."""
    type = ['ATOM', 'ATOM', 'HETATM', 'HETATM']
    name = ['GLU', 'GLU', 'TYS', 'TYS']  # GLU in amino_set -> residues; TYS not in amino_set -> ligands
    xcoord = [0.0, 1.0, 2.0, 3.0]
    ycoord = [0.0, 1.0, 2.0, 3.0]
    zcoord = [0.0, 1.0, 2.0, 3.0]
    chainID = ['A', 'A', 'A', 'A']
    resnum = [1, 1, 2, 2]
    s = Structure(type, name, xcoord, ycoord, zcoord, chainID, resnum)
    assert isinstance(s.residues, dict)
    assert isinstance(s.ligands, dict)
    assert ('GLU', 'A', 1) in s.residues
    assert ('TYS', 'A', 2) in s.ligands
    assert len(s.residues[('GLU', 'A', 1)]) == 2
    assert len(s.ligands[('TYS', 'A', 2)]) == 2