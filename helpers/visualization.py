import matplotlib.pyplot as plt
import numpy as np
from ligand import Structure
from itertools import cycle

def visualization(structure : Structure, max_distance : float):
    n = structure.neighbors(max_distance) # ligands w/ its residue neighbor
    
    # keys for ligands and residues that are neighbors for just one ligand
    ligand = next(iter(n))
    residues = n[ligand]

    # extracting atom coordinates
    l_coords = np.array(structure.ligands[ligand])
    r_coords = []

    # residues is (rkey, dist), so need to unpack
    for rkey, dist in residues:
        r_coords.append(structure.residues[rkey])

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.scatter(
        l_coords[:, 0],
        l_coords[:, 1],
        l_coords[:, 2],
        color="black",
        s=40,
        label=f"Ligand {ligand[0]}"
    )

    colors = cycle(plt.cm.tab10.colors)
    for (rkey, dist), color in zip(residues, colors):
        r_coords = np.asarray(structure.residues[rkey], dtype=float)

        ax.scatter(
            r_coords[:, 0],
            r_coords[:, 1],
            r_coords[:, 2],
            color=color,
            s=20,
            label=f"{rkey[0]} {rkey[1]} {rkey[2]}"
        )

    ax.set_xlabel("X (Å)")
    ax.set_ylabel("Y (Å)")
    ax.set_zlabel("Z (Å)")
    ax.set_title(f"Ligand neighborhood (R ≤ {max_distance} Å)")

    ax.legend(loc="best", fontsize=8)
    plt.tight_layout()
    plt.show()
