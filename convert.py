# import csv
import json
import pandas as pd

df = pd.read_excel('./style.xlsx')
print(df)

rows = df.to_numpy()

stylies = []
for row in rows:
    s = {'name': row[0], 'imageURL': row[1], 'mlmodelURL': row[2], 'mlmodelc': row[3]}
    stylies.append(s)

with open('style.json', 'w') as f:
    json.dump(stylies, f, indent=4)
