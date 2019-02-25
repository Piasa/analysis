from analysis import ED
import torch
import torch.nn as nn
import numpy as np

class LR(nn.Module):
    def __init__(self):
        super(LR,self).__init__()
        self.fc=nn.Linear(6,2)
    def forward(self,x):
        out=self.fc(x)
        out=torch.sigmoid(out)
        return out

def inputcv(cv):
    result = ED.analysisED(cv)
    n, l = result.shape
    mean = np.loadtxt("./analysis/mean.txt")
    for j in range(l - 1):
        result[:, j] = (result[:, j] - mean[j*2+1]) / mean[j*2+2]
    test_data = result[:,:l - 1]
    net = LR()
    net.load_state_dict(torch.load('./analysis/model.pkl'))
    net.eval()
    test_in=torch.from_numpy(test_data).float()
    test_out=net(test_in)
    out = test_out.max(-1)[1].detach().numpy()
    if out[0] == 0:
        return False
    else:
        return True
