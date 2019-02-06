import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,2,3,5,4,6,7,3,5])
y = np.array([20,35,35,50,70,60,80,100,69])

plt.xlabel('X')
plt.ylabel('Y')

plt.scatter(x,y,color = "m" , marker = "o" , s = 30)

plt.show()

## black box algorithm H(x) = W*x + B where W goes for weight and B is biase
## cost function is the squared error sum of distance of each point from the line
## gradient decent

## error j  is hence sigma whole square of H(x)i - yi where i is from 1 to number of coordinates / total points
## W = W - alpha*(partial diff (J,W))
## B = B - alpha*(partial diff (J,B))

## alpha is decided by the programmer and decides the size of steps. smaller alpha more precision more time
