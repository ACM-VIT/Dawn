import matplotlib.pyplot as plt
import seaborn as sns ; sns.set() #for plot styling
import numpy as np

from sklearn.datasets.samples_generator import make_blobs

X , y_true = make_blobs(n_samples = 300 , centers = 4 , cluster_std = 0.60 , random_state = 0) # make a blob dataset with n_sample = no. of samples , centers = k , cluster_std = standard deviation of center corresponding points 
plt.scatter(X[:,0],X[:,1] , s= 50); # print dataset

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 4)  #defining k
kmeans.fit(X)
## to print centers generated through the model : print(kmeans.cluster_centers_)
y_kmeans = kmeans.predict(X)
#for i in range(300):
    #print("cluster of " , X[i] , '=' , y_kmeans[i])

print('###################################################################################')

#for manually find Kmeans without library:
    
from sklearn.metrics import pairwise_distances_argmin #euclidian distance 
def find_clusters(X,n_clusters , rseed=2):
    #1 Choose Clusters Randomly
    rng = np.random.RandomState(rseed)
    i = rng.permutation(X.shape[0])[:n_clusters]
    centers = X[i]
    while True:
        #2a Assign labels based on closest center
        labels = pairwise_distances_argmin(X,centers) #selects min dist center an assigns center's label to point

        #2b Find new centers from mean
        new_centers = np.array([X[labels==i].mean(0) for i in range(n_clusters)]) 
        
        
        #2c Check whether previous center = new center
        if np.all(centers==new_centers):
            break
        centers = new_centers
    return centers,labels

centers,labels = find_clusters(X,4)
plt.scatter(X[:,0],X[:,1] , c = y_kmeans , s = 50 , cmap = 'viridis')
plt.scatter(centers[:,0] , centers[:,1] , c = 'red' , s = 200 )
#for i in range(300):
    #print("cluster of " , X[i] , '=' , labels[i])


