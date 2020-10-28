import csv
import json

stylies = []
with open('style.csv', 'r') as f_csv:
    rows = csv.reader(f_csv, delimiter='\t')
    for row in rows:
        s = {'name': row[0], 'image': row[1], 'mlmodel': row[2]}
        stylies.append(s)

with open('style.json', 'w') as f:
    json.dump(stylies, f, indent=4)
