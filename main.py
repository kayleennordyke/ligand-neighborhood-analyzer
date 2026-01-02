from ligand import create_structure
from helpers.save_to_csv import save_to_csv

def main():
    input_structure = "1a4w"
    max_distance = 2.5
    s = create_structure(input_structure)
    save_to_csv(s.neighbors(max_distance), input_structure)
    return 0

if __name__ == "__main__":
    main()