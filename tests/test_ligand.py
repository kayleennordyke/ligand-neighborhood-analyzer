import os
import pytest
import numpy as np
from residues import DimensionError

# Fix your moodule name
from ligand import Structure, create_structure

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
    inscode = ['?', '?', '?', '?', '?', '?', '?', '?']
    s = Structure(type, name, xcoord, ycoord, zcoord, chainID, resnum, inscode)

    coord1 = [[0, 2, 0], [0, 0, 0], [-1, 3, 0]]
    coord2 = [[0, 1, 0], [0, 1, 2]]
    dist = s.calculate_distance(coord1, coord2)
    assert np.isclose(dist, 1.0)