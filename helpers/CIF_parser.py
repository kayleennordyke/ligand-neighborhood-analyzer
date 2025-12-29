import json

from gemmi import cif

def read_cif(filepath: str):
    """
    Read a CIF file using gemmi. 
    """
    doc = cif.read_file(filepath)
    cif_dict = json.loads(doc.as_json())
    return cif_dict