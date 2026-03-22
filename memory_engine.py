import pandas as pd

memory = pd.read_csv("memory.csv")

def memory_category(desc):
    d = desc.lower()

    for _, row in memory.iterrows():
        if row["merchant"] in d:
            return row["category"]

    return None

