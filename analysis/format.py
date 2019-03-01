import numpy as np
import json
from analysis import *
a = open('/Users/gaoyifan/Downloads/CVDataset/cvDataset.json', 'rt')
f = json.load(a)
a.close()
sample = np.array([[25,25,5,15,10,20,100]])
a = 1
for i in f:
    a = a + 1
    if(a%1000 == 0):
        print(a)
    sample = np.concatenate((sample , ED.analysisED(i)))
np.savetxt('out.txt', sample)
