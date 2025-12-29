import pandas as pd

def save_to_csv(neighbor_dictionary, input_structure):
    rows = []

    for lkey, neighbors in neighbor_dictionary.items():
        for rkey, dist in neighbors:
            rows.append({
                "lig_name": lkey[0],
                "lig_chainID": lkey[1],
                "lig_resnum": lkey[2],
                "lig_inscode": lkey[3],
                "res_name": rkey[0],
                "res_chainID": rkey[1],
                "res_resnum": rkey[2],
                "res_inscode": rkey[3],
                "min_dist": dist
            })
    df = pd.DataFrame(rows)

    df.to_csv(f"results/{input_structure}_neighbors.csv", index=False)
    return df