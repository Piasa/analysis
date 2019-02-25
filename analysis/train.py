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
np.random.shuffle(data)

train_data=data[:9000,:l-1]
train_lab=data[:9000,l-1]
test_data=data[9000:,:l-1]
test_lab=data[9000:,l-1]
class LR(nn.Module):
    def __init__(self):
        super(LR,self).__init__()
        self.fc=nn.Linear(6,2)
    def forward(self,x):
        out=self.fc(x)
        out=torch.sigmoid(out)
        return out

def test(pred,lab):
    t=pred.max(-1)[1]==lab
    return torch.mean(t.float())

net=LR()
criterion=nn.CrossEntropyLoss()
optm=torch.optim.Adam(net.parameters())
epochs=5000

for i in range(epochs):
    net.train()
    x=torch.from_numpy(train_data).float()
    y=torch.from_numpy(train_lab).long()
    y_hat=net(x)
    loss=criterion(y_hat,y)
    optm.zero_grad()
    loss.backward()
    optm.step()
    if (i+1)%100 ==0 :
        net.eval()
        test_in=torch.from_numpy(test_data).float()
        test_l=torch.from_numpy(test_lab).long()
        test_out=net(test_in)
        accu=test(test_out,test_l)
        print("Epoch:{},Loss:{:.4f},Accuracy：{:.2f}".format(i + 1, loss.item(), accu))
torch.save(net.state_dict(), 'model.pkl')
