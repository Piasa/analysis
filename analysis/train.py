import torch
import torch.nn as nn
import numpy as np

data=np.loadtxt("out.txt")
mean = np.array([0])
n,l=data.shape

for j in range(l-1):
    meanVal=np.mean(data[:,j])
    stdVal=np.std(data[:,j])
    data[:,j]=(data[:,j]-meanVal)/stdVal
    mean = np.append(mean,[meanVal,stdVal])
np.savetxt('mean.txt', mean)
'''np.random.shuffle(data)'''

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
train_data=data[:9000,:l-1]
train_lab=data[:9000,l-1]
test_data=data[9000:,:l-1]
test_lab=data[9000:,l-1]
print(train_lab)
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
        return out
'''class LR(nn.Module):
    def __init__(self):
        super(LR,self).__init__()
        self.fc=nn.Linear(6,11) # 由于24个维度已经固定了，所以这里写24
    def forward(self,x):
        out=self.fc(x)
        out=torch.nn.functional.softmax(out,dim=1)
        return out'''

def test(pred,lab):
    t=pred.max(-1)[1]==lab
    return torch.mean(t.float())

net=LR()
net.to(device)
criterion=nn.CrossEntropyLoss()
'''criterion=nn.MSELoss()'''
optm=torch.optim.Adam(net.parameters())
#optm = torch.optim.SGD(net.parameters(),lr=0.01,momentum=0.9)
epochs=10000

for i in range(epochs):
    net.train()
    x=torch.from_numpy(train_data).float()
    y=torch.from_numpy(train_lab).long()
    x = x.to(device)
    y = y.to(device)
    y_hat=net(x)
    loss=criterion(y_hat,y)
    optm.zero_grad()
    loss.backward()
    optm.step()
    if (i+1)%1000 ==0 :
        net.eval()
        test_in=torch.from_numpy(test_data).float().to(device)
        test_l=torch.from_numpy(test_lab).long().to(device)
        test_out=net(test_in)
        accu=test(test_out,test_l)
        print("Epoch:{},Loss:{:.4f}Accu:{:.3f}".format(i + 1, loss.item(),accu))
torch.save(net.state_dict(), 'model.pkl')
