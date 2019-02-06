

#KNN - Predict whether a person will have diabetes or not
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

#Reading CSV file
dataset = pd.read_csv('KNN_Dataset.csv')
print(dataset.head())  #prints first 5 dataset tuples

#clean Dataset by replacing zeros with mean of attribute
zero_not_accepted = ['Glucose', 'BloodPressure' , 'SkinThickness' , 'BMI' , 'Insulin' , 'Age']
for column in zero_not_accepted:
    dataset[column] = dataset[column].replace(0,np.NaN) #replace 0 with NULL
    mean = int(dataset[column].mean(skipna=True)) #calculate mean and skip NULL
    dataset[column] = dataset[column].replace(np.NaN,mean) #replace NULL with mean value
    
print(dataset['SkinThickness']) # check no zeros !!

#split dataset into train and test dataset
X = dataset.iloc[:,0:8] #column 1 to 8
Y = dataset.iloc[:,8] #column 9 as label (ans)
X_train , X_test , Y_train , Y_test = train_test_split(X,Y,random_state = 0 , test_size = 0.2)  #test_size is % of dataset split into test

#feature Scaling : Scaling Data as one column will have values in 1000s but next will have value<10 hence scaling imp
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)

# Define the model
classifier = KNeighborsClassifier(n_neighbors = 11 , p = 2 , metric = 'euclidean') #n_neighbour = k , p = no. of different outputs , metric = type with which distance to be calculated
#fit Model
classifier.fit(X_train , Y_train)


#Running the model:
Y_pred = classifier.predict(X_test)

#evaluating the model:
cm = confusion_matrix(Y_test,Y_pred)
print("confusion Matrix:")
print(cm)
print("f1 Score - " , f1_score(Y_test , Y_pred))
print("Accuracy - " , accuracy_score(Y_test,Y_pred))

