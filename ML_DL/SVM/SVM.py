# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 19:21:04 2018

@author: Anunay Bagga
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets.samples_generator import make_blobs

#Create 40 seperable points
X,y = make_blobs(n_samples=40 , centers = 2 , random_state=20) #20 each side

clf = svm.SVC(kernel = 'linear' , C=1000)
clf.fit(X,y)

#display data in graph:
plt.scatter(X[:,0] , X[:,1] , c=y , s = 30 )


#pridicting new data:
newData = [[3,4],[5,6]]
print(clf.predict(newData))

#plot the decision functions:
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

##create grid:
xx = np.linspace(xlim[0] , xlim[1] , 30) # 30 = no. of points
yy = np.linspace(ylim[0] , ylim[1] , 30)
YY,XX = np.meshgrid(yy,xx)
xy = np.vstack([XX.ravel(),YY.ravel()]).T

Z = clf.decision_function(xy).reshape(XX.shape)

#plot decision boundary :
ax.contour(XX,YY,Z,colors = 'k' , levels = [-1,0,1] , linestyles = ['--','-','--'])

