# ligand Neighborhood Analyzer

A python program to find neighboring residues of ligands present in a CIF file. 

## Preview

![Ligand–Residue Neighbor Visualization](media/demo.gif)

## Table of Contents

- [Demo-Preview](#demo-preview)
- [Table of Contents](#table-of-contents)
- [Usage](#usage)
- [Examples](#examples)
- [Development](#development)
- [Acknowledgements](#acknowledgements)

## Usage
[(Back to Top)](#table-of-contents)

This project consists of **two components**:
1. **CSV generation**
2. **Interactive visualization**

### Part 1: CSV Generation
This portion generates a CSV file located in the `results\` directory. The CSV contains **ligands and their neighboring residues** within a user-specified distance and structure.

> Note: Structure CIF files must be located in the `data\' directory. Users can find CIF files from **RCSB PDB**.

#### Run from terminal:

```bash
python main.py --struct `STRUCTURE_ID` --dist `MAX_DISTANCE`
```
STRUCTURE_ID: structure identifier CIF file (e.g. `1a4w`)

MAX_DISTANCE: neighbor cutoff distance in angstroms (e.g. `3`)

### Part 2: Visualization
This portion is a visual demonstration of ligand to residue neighbors provided in the notebook:
`visual_demo.ipynb`

> Note: Only the second cell needs to be modified.

In the seconds cell, users can specify **structure id** and **neighbor cutoff distance**. The remaining cells can be ran with no modification to generate the interactive visualization.

## Examples
[(Back to Top)](#table-of-contents)



## Development

## Acknowledgements


