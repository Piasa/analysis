from analysis import *
import json
from pprint import pprint
from pprint import pprint
import pandas as pd
import torch
import torch.nn as nn

if __name__=="__main__":
    a = {'A-Level Qualifications': [{'Grade': 'C', 'Subject': 'Mathematics'},
                            {'Grade': 'C', 'Subject': 'Further Mathematics'},
                            {'Grade': 'C',
                             'Subject': 'Applied Art and Design '},
                            {'Grade': 'C', 'Subject': 'Journalism '}],
                            'Degree Level': '2:2',
 'Degree Qualification': 'Mathematics and Physics, MMathPhys',
 'Hobbies': [{'Interest': 8, 'Name': 'Gardening'},
             {'Interest': 3, 'Name': 'Tango'},
             {'Interest': 7, 'Name': 'Horse riding'},
             {'Interest': 5, 'Name': 'DIY'},
             {'Interest': 1, 'Name': 'Sword swallowing'},
             {'Interest': 8, 'Name': 'Book restoration'},
             {'Interest': 1, 'Name': 'Sculpting'},
             {'Interest': 7, 'Name': 'Scrapbooking'},
             {'Interest': 10, 'Name': 'Juggling'}],
 'Languages Known': [{'Expertise': 7, 'Language': 'Visual Basic .NET'},
                     {'Expertise': 9, 'Language': 'SQL'},
                     {'Expertise': 6, 'Language': 'Java'},
                     {'Expertise': 8, 'Language': 'C'},
                     {'Expertise': 7, 'Language': 'UNITY'},
                     {'Expertise': 7, 'Language': 'PhP'},
                     {'Expertise': 9, 'Language': 'LaTeX'},
                     {'Expertise': 6, 'Language': 'Hack'},
                     {'Expertise': 8, 'Language': 'HTML'},
                     {'Expertise': 5, 'Language': 'CUDA'},
                     {'Expertise': 6, 'Language': 'Ruby-on-rails'}],
 'Name': 'Kenyetta Nabozny',
 'Previous Employment': [{'Company': 'Cobra',
                          'Length of Employment': '3 years 1 month',
                          'Position': 'Senior Web Developer'}],
 'Skills': [{'Expertise': 4, 'Skill': 'Italian'},
            {'Expertise': 5, 'Skill': 'Google Drive'},
            {'Expertise': 6, 'Skill': 'Constructive criticism'},
            {'Expertise': 7, 'Skill': 'Online collaboration'}],
 'University Attended': 'University of Glasgow'}
    print(predict.inputcv(a))
    #feedback.inputfeedback(a,170)
    '''a = open('/Users/gaoyifan/Downloads/CVDataset/cvDataset.json', 'rt')
    f = json.load(a)
    a.close()
    x = 0
    u = []
    for i in f:
        
        u.append(x['Position'])
    pprint(u)'''
    data = np.loadtxt("./analysis/out.txt")
    n, l = data.shape
    for j in range(l-1):
        meanVal=np.mean(data[:,j])
        stdVal=np.std(data[:,j])
        data[:,j]=(data[:,j]-meanVal)/stdVal
        print(meanVal,stdVal)
