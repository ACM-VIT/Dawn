import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
dataset=pd.read_csv("Twitter_data.csv")
stop_words=set(stopwords.words('english'))
def textmining(s,l):
    word_tokens=word_tokenize(s)
    p="?:!.,;"
    fs=[l.stem(word).lower() for word in word_tokens if word.isalpha() and not word in stop_words or word in ["AT_USER","LINK"]]    
    return fs
fw1=[]
fw2=[]
wor=[]
for i in dataset['Tweets']:
    i=re.sub("https?://\S+","LINK",i)
    i=re.sub("@\S+","AT_USER",i)
    wor.append(i)
    fw1.append(textmining(i,PorterStemmer()))
    fw2.append(textmining(i,LancasterStemmer()))
dataset['Words']=wor
dataset['Feature Words (Porter)']=fw1
dataset['Feature Words (Lancaster)']=fw2
dataset.to_csv('Twitter_data.csv')