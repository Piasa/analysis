import json
from pprint import pprint
if __name__=="__main__":
    file = "/Users/gaoyifan/Downloads/CVDataset/cvDataset.json"
    fb = open(file, 'r')
    load_dict = json.load(fb)
    fb.close()
    alevel = ()
    university = ()
    hobbies = ()
    language = ()
    employee = ()
    for i in load_dict:
        if i['Degree Level'] == '1st' and i['University Attended'] == 'New York University':
            pprint(i)
