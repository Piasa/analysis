# analysis
put analysis folder next to the python file you want to use 
add 'from analysis import *' at the head of the python file
two function available:
predict.inputcv(cv)
input a cv file and return a bool. true means pass false means not
pass.
feedback.inputfeedback(cv,result):
take a cv and a result. result is 1 or 0.1 means pass, 0 means not pass