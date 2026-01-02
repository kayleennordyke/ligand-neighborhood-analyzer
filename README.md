# Ligand Neighborhood Analyzer

A python program to find neighboring residues of ligands present in a CIF file. 

> This project is intended for educational and exploratory analysis and does not perform energetic or dynamic modeling.


## Preview
This demo visual was created using the structure **1a4w** with a max neighbor distance of **3**.
![Ligand–Residue Neighbor Visualization](media/demo.gif)

## Table of Contents

- [Demo-Preview](#demo-preview)
- [Table of Contents](#table-of-contents)
- [Requirements](#requirements)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)

## Requirements

- Python ≥ 3.11
- NumPy
- gemmi
- nglview

A `Makefile` is provided to simplify environment setup and dependency installation.

To create a conda environment with all required dependencies installed, run the following in the terminal:

```bash
make environment
```

Then, activate the environment with:

```bash
conda activate ligand-neighborhood-analyzer
```


## Usage
[(Back to Top)](#table-of-contents)

This project consists of **two components**:
1. **CSV generation**
2. **Interactive visualization**

### Part 1: CSV Generation
This portion generates a CSV file located in the `results/` directory. The CSV contains **ligands and their neighboring residues** within a user-specified distance and structure.

> Note: Structure CIF files must be located in the `src/ligand_neighborhhod/data/' directory. CIF structure files can be obtained from the [RCSB Protein Data Bank](https://www.rcsb.org).


#### Run from terminal:

```bash
PYTHONPATH=src python -m ligand_neighborhood.main --struct `STRUCTURE_ID` --dist `MAX_DISTANCE`
```
STRUCTURE_ID: structure identifier CIF file (e.g. `1a4w`)

MAX_DISTANCE: neighbor cutoff distance in angstroms (e.g. `3`)

### Part 2: Visualization
This portion is a visual demonstration of ligand to residue neighbors provided in the notebook:
`visual_demo.ipynb`

> Note: Only the second cell needs to be modified.

In the second cell, users can specify **structure id** and **neighbor cutoff distance**. The remaining cells can be run with no modification to generate the interactive visualization.

## Acknowledgements

This software uses the following open source packages:

- [NumPy](https://numpy.org/)
- [nglview](https://github.com/nglviewer/nglview)
- [gemmi](https://github.com/project-gemmi/gemmi)

Special thanks to my professor at UC Berkeley, **Dr. Jessica Nash**, for providing the CIF parsing function as part of a course assignment, which was directly incorporated into this project.  

Additional thanks to my TA, **Usman Jamshed**, for sharing his [personal project](https://github.com/ujamshed/dgbg), which influenced the direction of this project.

