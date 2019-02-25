import numpy as np

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

def languagescore(cv):
    score = 0
    for i in cv['Languages Known']:
        score = score + i['Expertise']
    return score

def alevelscore(cv):
    score = 0
    for i in cv['A-Level Qualifications']:
        for x in i['Grade']:
            if x == 'A*':
                score = score +10
            elif x == 'A':
                score = score + 8
            elif x == 'B':
                score = score + 6
            elif x == 'C':
                score = score + 4
    return score

def degree(cv):
    score = 0
    if cv['Degree Level'] == '1st':
        score = score + 10
    elif cv['Degree Level'] == '2:1':
        score = score + 8
    else:
        score = score + 5
    return score

def analysisED(cv):

    if alevelscore(cv)>=24 and languagescore(cv)>=15 and degree(cv)>=8:
        return np.array([[alevelscore(cv),skillscore(cv),employmentscore(cv),hobbyscore(cv),degree(cv),languagescore(cv),1]])
    else:
        return np.array([[alevelscore(cv),skillscore(cv),employmentscore(cv),hobbyscore(cv),degree(cv),languagescore(cv),0]])

