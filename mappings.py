"""
Map 3 letter codes to one letter and vice versa, and CPK colors.
"""
amino_set = {
    "ALA",
    "ARG",
    "ASN",
    "ASP",
    "CYS",
    "GLN",
    "GLU",
    "GLY",
    "HIS",
    "ILE",
    "LEU",
    "LYS",
    "MET",
    "PHE",
    "PRO",
    "SER",
    "THR",
    "TRP",
    "TYR",
    "VAL"
 }
three_to_one = {
    "ALA": "A",
    "ARG": "R",
    "ASN": "N",
    "ASP": "D",
    "CYS": "C",
    "GLN": "Q",
    "GLU": "E",
    "GLY": "G",
    "HIS": "H",
    "ILE": "I",
    "LEU": "L",
    "LYS": "K",
    "MET": "M",
    "PHE": "F",
    "PRO": "P",
    "SER": "S",
    "THR": "T",
    "TRP": "W",
    "TYR": "Y",
    "VAL": "V",
}

# Implement one to three mapping
# will be useful for your project
one_to_three = {
    "A" : "ALA",
    "R" : "ARG",
    "N" : "ASN",
    "D" : "ASP",
    "C" : "CYS",
    "Q" : "GLN",
    "E" : "GLU",
    "G" : "GLY",
    "H" : "HIS",
    "I" : "ILE",
    "L" : "LEU",
    "K" : "LYS",
    "M" : "MET",
    "F" : "PHE",
    "P" : "PRO",
    "S" : "SER",
    "T" : "THR",
    "W" : "TRP",
    "Y" : "TYR",
    "V" : "VAL",
}

CPK = {
    "H" : "white",
    "C" : "black",
    "N" : "blue",
    "O" : "red",
    "S" : "yellow",
    "P" : "orange",
    "F" : "green",
    "CL" : "green",
    "BR" : "brown",
    "I" : "purple",
}

order_to_weight = {
    "SING" : 1.0,
    "DOUB" : 2.0,
    "TRIP" : 3.0,
    "AROM" : 1.5,
}