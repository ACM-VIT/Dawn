from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

#setting random seed
np.random.seed(0)


#looking at data
iris = load_iris()
#create an excel spreadsheet like dataset
df = pd.DataFrame(iris.data, columns=iris.feature_names)

#print(df.head())


#add new column for species name
df['species'] = pd.Categorical.from_codes(iris.target,iris.target_names)

#print(df.head())

#create Test and Train Data
df['is_train'] = np.random.uniform(0,1,len(df))<=0.75  #generating a random no. between 0 and 1 for each row then if number <=75 True else False
print(df.head())

train = df[df['is_train']==True]
test = df[df['is_train']==False]
print('no of test ' , len(test))
print('no of train ', len(train))

#dividing features in dataset
features = df.columns[:4] # name of features
#print(features)

#convert species into digits :P
y = pd.factorize(train['species'])[0]  #0 because an array of array so index factorize checks diff types and allocates numbers to each
print(y)

#creating Data set done*************************************************

#random forest implimentation:

#random forest classifier
clf = RandomForestClassifier(n_jobs = 2 , random_state = 0) #2 variables random state for seeing where it starts
#training
clf.fit(train[features],y) #(features , labels)

#testing

y = clf.predict(test[features])
print('prediction' , y)

#viewing the predicted probabilities of the first 10 obs
print(clf.predict_proba(test[features])[0:10]) #look at first 10 
print(clf.predict_proba(test[features])[10:20])

#if same array has same probability then leftmost aka first value is prediction of random forest


#mapping names for the plants setosa , versicolor , virginica
preds = iris.target_names[clf.predict(test[features])]
print(preds[0:25])

#confusion matrix:
print(pd.crosstab(test['species'] , preds , rownames = ['Actual Species'] , colnames = ['Predicted Species']))

