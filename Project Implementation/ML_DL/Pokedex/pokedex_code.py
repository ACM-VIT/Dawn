# Pokedex

#Importing libraries
import cv2
import os
import numpy as np
import imutils

X = []
y = []

# Resize all the pictures to 200x200 and convert it into grayscale
def changeimg(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img1 = imutils.resize(img,height = 200)
    w = img1.shape[1]
    if w<200:
        img2 = imutils.resize(img,width = 200)
        h = img2.shape[0]
        return img2[int((h-200)/2):int((h+200)/2), 0:200]
    else:
        return img1[0:200, int((w-200)/2):int((w+200)/2)]

for i in os.listdir("pokemon"):
    for j in os.listdir("pokemon/"+i):
        x = "pokemon/"+i+"/"+j
        img = cv2.imread(x)
        new_img = changeimg(img)
        X.append(new_img)
        y.append(i)

# X needs to be a 2D numpy array for sklearn
X = np.array(X)
X = X.reshape(100,-1)

# Label encode all the string values
from sklearn.preprocessing import LabelEncoder
labelencoder_y = LabelEncoder()
#0-Eevee, 1-Gengar, 2-Jigglypuff, 3-Pikachu, 4-Squirtle 
y = labelencoder_y.fit_transform(y)  

# Splitting dataset into train and test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0, shuffle = True)

# Applying Principal Component Analysis
from sklearn.decomposition import PCA
pca = PCA(n_components = 18, whiten=True).fit(X_train)
X_train = pca.transform(X_train)
X_test = pca.transform(X_test)

# Fit the classifier to the train set
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
#param grid values are set after running the best_params_ function
param_grid = {'kernel': ['rbf'],  'C': [1000], 'gamma': [0.005],}
classifier = GridSearchCV(SVC(class_weight='balanced'), param_grid)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
    
# Your Pokedex is ready! Feed it a picture of any Pokemon and the Pokedex will identify it
labels = ["Eevee","Gengar","Jigglypuff","Pikachu","Squirtle"]
im = cv2.imread("ev.jpg")
new_im = changeimg(im)
I = np.array([new_im]).reshape(1,-1)
I_pca = pca.transform(I)
index = int(classifier.predict(I_pca))
s = "Its an "+labels[index]+"!"

im1 = cv2.cvtColor(im,cv2.COLOR_BGR2RGB) #matplotlib loads pictures as RGB
import matplotlib.pyplot as plt
imgplot = plt.imshow(im1)
plt.title(s)
plt.show()
