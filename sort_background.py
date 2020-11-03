import os
import cv2
import json

all_files = list(filter(lambda x: x.startswith('.') is False, os.listdir('./background/')))

out = []
for i, f in enumerate(all_files):
    img = cv2.imread(f'./background/{f}')
    name = str(i).zfill(5) + '.jpg'
    out.append('https://github.com/tungxuan1656/transfer-style-mlmodel/releases/download/background/' + name)
    cv2.imwrite('./sort_background/' + name, img)

# generate list file
with open('background.json', 'w') as f:
    json.dump(out, f, indent=4)
