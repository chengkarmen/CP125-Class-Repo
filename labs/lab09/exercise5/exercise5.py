import pandas as pd


def high_performers(filename):
    data = pd.read_csv(filename)
    count = len(data.loc[(data['Math']> 85) & (data['Science']> 85) & (data['English'] > 85) & (data['Physics'] > 85) & (data['Chemistry']> 85)])
    name = set(data.loc[(data['Math']> 85) & (data['Science']> 85) & (data['English'] > 85) & (data['Physics'] > 85) & (data['Chemistry']> 85), 'Name'])
    return {"count": count,
            "names": name}

high_performers('labs/lab09/data/students.csv')