import json
from pprint import pprint
if __name__=="__main__":
    file = "/Users/gaoyifan/Downloads/CVDataset/cvDataset.json"
    fb = open(file, 'r')
    load_dict = json.load(fb)
    fb.close()
    pprint(load_dict[0:20])
