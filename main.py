from ligand import create_structure

def main():
    s = create_structure("1a4w")

    print(s.ligands)
    return 0

if __name__ == "__main__":
    main()