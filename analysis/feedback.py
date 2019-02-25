import numpy as np
from analysis import ED
def inputfeedback(cv,result):
    data = np.loadtxt("./analysis/out.txt")
    mark = ED.analysisED(cv)
    mark = mark[:, :7 - 1]
    mark = np.append(mark,[result])
    sample = np.concatenate((data,[mark]))
    np.savetxt('./analysis/out.txt', sample)