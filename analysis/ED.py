import numpy as np
import pandas as pd
import csv

def employmentscore(cv):
    score = 0
    for i in cv['Previous Employment']:
        with open('./analysis/data/Position.csv') as f:
            Position = csv.DictReader(f)
            for x in Position:
                if x['Position'] == " '" + i['Position'] + "'":
                    Rank = int(x['Rank'])
                    if Rank < 5:
                        Rank = 5
                    score = score + Rank * 5
    return score

def hobbyscore(cv):
    score = 0
    for i in cv['Hobbies']:
        score = score + i['Interest']
    return score


def skillscore(cv):
    score = 0
    for i in cv['Skills']:
        with open('./analysis/data/Skill.csv') as f:
            skill = csv.DictReader(f)
            for x in skill:
                if x['Skill'] == "'" + i['Skill'] + "'":
                    Rank = int(x['Rank'])
                    if Rank < 5:
                        Rank = 5
                    score = score + Rank * i['Expertise']
    return score

def languagescore(cv):
    score = 0
    for i in cv['Languages Known']:
        with open('./analysis/data/Language.csv') as f:
            language = csv.DictReader(f)
            for x in language:
                if x['Language'] == "'"+i['Language']+"'":
                    Rank = int(x['Rank'])
                    if Rank <5:
                        Rank = 5
                    score = score + Rank * i['Expertise']
    return score

def alevelscore(cv):
    score = 0
    for i in cv['A-Level Qualifications']:
        with open('./analysis/data/Alevel.csv') as f:
            alevel = csv.DictReader(f)
            for sub in alevel:
                if sub['Subject'] == " '"+i['Subject']+"'":
                    Rank = int(sub['Rank'])
                    if Rank < 5:
                        Rank = 5
                    x = i['Grade']
                    if x == 'A*':
                        score = score + 10 * Rank
                    elif x == 'A':
                        score = score + 8 * Rank
                    elif x == 'B':
                        score = score + 6 * Rank
                    elif x == 'C':
                        score = score + 4 * Rank
    return score

def degree(cv):
    score = 0
    University = cv['University Attended']
    Rank = 5
    with open('./analysis/data/University.csv') as f:
        Uni = csv.DictReader(f)
        for i in Uni:
            if i['University'] == "'"+University+"'":
                Rank = int(i['Rank'])
    if cv['Degree Level'] == '1st':
        score = score + Rank * 10
    elif cv['Degree Level'] == '2:1':
        score = score + Rank * 8
    else:
        score = score + Rank * 5
    return score

def analysisED(cv):
    a = alevelscore(cv)+skillscore(cv)+employmentscore(cv)+hobbyscore(cv)+degree(cv)+languagescore(cv)
    print (alevelscore(cv), skillscore(cv), employmentscore(cv), hobbyscore(cv), degree(cv), languagescore(cv), a)
    return np.array([[alevelscore(cv),skillscore(cv),employmentscore(cv),hobbyscore(cv),degree(cv),languagescore(cv),a]])

    '''if alevelscore(cv)>=24 and languagescore(cv)>=15 and degree(cv)>=8:
        return np.array([[alevelscore(cv),skillscore(cv),employmentscore(cv),hobbyscore(cv),degree(cv),languagescore(cv),1]])
    else:
        return np.array([[alevelscore(cv),skillscore(cv),employmentscore(cv),hobbyscore(cv),degree(cv),languagescore(cv),0]])'''

