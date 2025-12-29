from ligand import create_structure
from save_to_csv import save_to_csv

def main():
    input_structure = "1a4w"
    s = create_structure(input_structure)
    save_to_csv(s.neighbors(2), input_structure)

    return 0

if __name__ == "__main__":
    main()