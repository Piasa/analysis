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
    """criterion = nn.BCEWithLogitsLoss()  # 将 sigmoid 和 loss 写在一层，有更快的速度、更好的稳定性

    w = nn.Parameter(torch.randn(2, 1))
    b = nn.Parameter(torch.zeros(1))

    def logistic_reg(x):
        return torch.mm(x, w) + b

    optimizer = torch.optim.SGD([w, b], 1.)
    y_pred = logistic_reg(x_data)
    loss = criterion(y_pred, y_data)
    print(loss.data)
    start = time.time()
    for e in range(1000):
        # 前向传播
        y_pred = logistic_reg(x_data)
        loss = criterion(y_pred, y_data)
        # 反向传播
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        # 计算正确率
        mask = y_pred.ge(0.5).float()
        acc = (mask == y_data).sum().data[0] / y_data.shape[0]
        if (e + 1) % 200 == 0:
            print('epoch: {}, Loss: {:.5f}, Acc: {:.5f}'.format(e + 1, loss.data[0], acc))

    during = time.time() - start
    print()
    print('During Time: {:.3f} s'.format(during))"""
    if alevelscore(cv) + skillscore(cv) + employmentscore(cv) + hobbyscore(cv) >=60:
        return True
    else:
        return False

