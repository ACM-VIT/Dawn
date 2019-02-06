import numpy as np


#no. of days a student studied for his/her boards
x = np.array([16,16,27,26,15,37,32,20,25,40,30,21,23,20,19,20,30,22,16])
 # 90%+ = 1 , below 90% = 0
y = np.array([1,1,0,1,1,0,0,1,0,0,0,0,0,1,1,1,0,1,1])
def sigmoid(x):
    return 1/(1+np.exp(-x))

alpha = 0.001

def grad_decent(x,y,inp):
    t1,t2=0,0

    for i in range(1000):
        grad1 , grad2 = 0,0
        for j in range(len(x)):
            grad1 += sigmoid(t1+t2*x[j]) - y[j]
            grad2 += (sigmoid(t1+t2*x[j]) - y[j])*x[j]
        t1 -= alpha*grad1
        t2 -= alpha*grad2
    return sigmoid(t1+t2*inp)

inp = int(input('enter the number of days you studied   '))
print('probability of you getting 90% + is =  ' + str(grad_decent(x,y,inp)))
