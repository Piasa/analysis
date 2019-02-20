from analysis import *
import json
from pprint import pprint
import pandas as pd
if __name__=="__main__":
    a = {'A-Level Qualifications': [{'Grade': 'A', 'Subject': 'Mathematics'},{'Grade': 'A', 'Subject': 'Psychology '},{'Grade': 'C', 'Subject': 'Archaeology '},
    {'Grade': 'A', 'Subject': 'Engineering '}],
    'Degree Level': '1st',
    'Degree Qualification': 'Engineering, BEng',
    'Hobbies': [{'Interest': 8, 'Name': 'Hiking'},
             {'Interest': 2, 'Name': 'Fencing'},
             {'Interest': 2, 'Name': 'Weight lifting'},
             {'Interest': 10, 'Name': 'Book collecting'}],
    'Languages Known': [{'Expertise': 4, 'Language': 'C'},
                     {'Expertise': 6, 'Language': 'Visual Basic .NET'},
                     {'Expertise': 6, 'Language': 'Java'}],
    'Name': 'Kris Mcclung',
    'Previous Employment': [{'Company': 'Medetic',
                          'Length of Employment': '2 years 2 months',
                          'Position': 'Senior Software Developer'}],
    'Skills': [{'Expertise': 3, 'Skill': 'Fundraising'},
            {'Expertise': 8, 'Skill': 'Research'},
            {'Expertise': 7, 'Skill': 'Access'},
            {'Expertise': 7, 'Skill': 'Powerpoint'}],
    'University Attended': 'New York University'}
    print(ED.analysisED(a))
    a = open('/Users/gaoyifan/Downloads/CVDataset/cvDataset.json','rt')
    f = json.load(a)
    a.close()
    u = []
    alevel = pd.read_csv('./analysis/data/University.csv');
    for i in f:
        for x in i['A-Level Qualifications']:
            if not(x['Grade'] in u):
                u.append(x['Grade'])

    pprint(u)
