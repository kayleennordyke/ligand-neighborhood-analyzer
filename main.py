from ligand import create_structure
from helpers.save_to_csv import save_to_csv
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Find ligand neighbors from a structure."
    )

    # to specify structure
    parser.add_argument(
        "--struct",
        type=str,
        default="1a4w",
        help="CIF structure file, default is 1a4w"
    )

    # to specify structure
    parser.add_argument(
        "--dist",
        type=float,
        default=2.5,
        help="Maximum distance of neighbors in Angstroms, default is 2.5."
    )

    args = parser.parse_args()
    input_structure = args.structure
    max_distance = args.distance
    s = create_structure(input_structure)
    save_to_csv(s.neighbors(max_distance), input_structure)
    return 0

if __name__ == "__main__":
    main()