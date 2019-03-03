from analysis import ED
import torch
import torch.nn as nn
import numpy as np

'''class LR(nn.Module):
    def __init__(self):
        super(LR,self).__init__()
        self.fc=nn.Linear(6,1)
    def forward(self,x):
        out=self.fc(x)
        return out'''
class LR(nn.Module):
    def __init__(self):
        super(LR,self).__init__()
        self.fc1=nn.Linear(6,64)
        self.fc2=nn.Linear(64,64)
        self.fc3=nn.Linear(64,64)
        self.fc6=nn.Linear(64,11)
    def forward(self,x):
        out=torch.tanh(self.fc1(x))
        out=torch.tanh(self.fc2(out))
        out=torch.tanh(self.fc3(out))
        return nn.functional.softmax(self.fc6(out),dim=1)
        '''out=torch.sigmoid(out)'''
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
def inputcv(cv,score):
    result = ED.analysisED(cv)
    n, l = result.shape
    mean = np.loadtxt("./analysis/mean.txt")
    for j in range(l - 1):
        result[:, j] = (result[:, j] - mean[j*2+1]) / mean[j*2+2]
    test_data = result[:,:l - 1]
    net = LR()
    net.load_state_dict(torch.load('./analysis/model.pkl',map_location=device))
    net.eval()
    test_in=torch.from_numpy(test_data).float()
    test_in = test_in
    test_out=net(test_in)
    out = test_out.max(-1)[1].detach().numpy()
    mark = out[0]
    bias = 0

    if score >=80:
        bias = 2
    elif score <=50:
        bias = -2
    else:
        bias = 0

    if bias + mark >10:
        mark = 10
    elif bias + mark<0:
        mark = 0
    else:
        mark = mark + bias

    return mark
