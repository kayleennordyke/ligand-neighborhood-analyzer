from ligand import create_structure

def main():
    s = create_structure("1a4w")

    print(s.neighbors(2))
    return 0

if __name__ == "__main__":
    main()