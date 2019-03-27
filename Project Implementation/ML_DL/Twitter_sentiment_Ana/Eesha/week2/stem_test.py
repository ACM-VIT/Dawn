import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
dataset=pd.read_csv("train.csv")
stop_words=set(stopwords.words('english'))
def textmining(s,l):
    sentence_words= nltk.word_tokenize(sentence)
    for word in sentence_words:
        if word in p:
            sentence_words.remove(word)
        else:
            word=wordnet_lemmatizer.lemmatize(word,pos="v")
    return sentence_words
fw1=[]
for i in dataset['Tweets']:
    i=re.sub("https?://\S+","",i)
    i=re.sub("@\S+","",i)
    wor.append(i)
    fw1.append(textmining(i))
dataset['Words']=wor
dataset['Feature Words (Lemma)']=fw1
dataset.to_csv('train.csv')