import numpy as np

x = np.array([1,2,3,5,4,6,7,3,5])
y = np.array([20,35,35,50,70,60,80,100,69])

w = 0   ##initializing use any number zero is risky
b = 0   ##same as above

alpha = 0.01
error = 0
for i in range ( len(x)):
    temp = (w*x[i] + b - y[i])**2
    error += temp

print('error  =  ',error/float (len(x)))


def hypothesis(w,b):
    sum = 0
    for i in range(len(x)):
        temp = w*x[i] + b
        sum += temp
    return sum



def grad_descent(w,b,iterations,alpha):
    for i in range(iterations):
        b_grad = 0
        w_grad = 0
        for j in range(len(x)):
            w_grad += 2*(w*x[j] + b  - y[j])*x[j]/len(x)  ## by partial differenciation
            b_grad += 2*(w*x[j] + b - y[j])/len(x)
        w = w - (alpha * w_grad)
        b = b - (alpha * b_grad)
    return w,b


w,b = grad_descent(w,b,1000,0.01)

print("final line is: "  + str(w) + " x + " +   str(b))
