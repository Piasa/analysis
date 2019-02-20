import torch
import pandas
from pprint import pprint

def employmentscore(cv):
    score = 0
    i = cv['Previous Employment']
    score = len(i) * 5
    return score

def hobbyscore(cv):
    score = 0
    for i in cv['Hobbies']:
        score = score + i['Interest']
    return score


def skillscore(cv):
    score = 0
    for i in cv['Skills']:
        score = score + i['Expertise']
    return score



def alevelscore(cv):
    alevel = 0
    for i in cv['A-Level Qualifications']:
        for x in i['Grade']:
            if x == 'A*':
                alevel == alevel +10
            elif x == 'A':
                alevel = alevel + 8
            elif x == 'B':
                alevel = alevel + 6
            elif x == 'C':
                alevel = alevel + 4
    return alevel

def analysisED(cv):
    if alevelscore(cv) + skillscore(cv) + employmentscore(cv) + hobbyscore(cv) >=60:
        return True
    else:
        return False

