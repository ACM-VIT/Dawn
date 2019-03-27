#0-negative 1-neutral 2-positive
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn import preprocessing
wordnet_lemmatizer = WordNetLemmatizer()
dataset=pd.read_csv("Tweets.csv")
le=preprocessing.LabelEncoder()
le.fit(dataset['airline_sentiment'])
dataset['airline_sentiment']=le.transform(dataset['airline_sentiment'])
stop_words=set(stopwords.words('english'))
def textmining(s):
    sw=[]
    p="?;!.,;"
    sentence_words= nltk.word_tokenize(s)
    for word in sentence_words:
        if word not in p and word not in stop_words and word.isalpha():
            sw.append(wordnet_lemmatizer.lemmatize(word,pos="v"))
    return (" ").join(sw)
fw1=[]
wor=[]
for i in dataset['text']:
    i=re.sub("https?://\S+","",i)
    i=re.sub("@\S+","",i)
    fw1.append(textmining(i))
dataset['Feature Words (Lemma)']=fw1
dataset.to_csv('Tweets.csv',index=False)