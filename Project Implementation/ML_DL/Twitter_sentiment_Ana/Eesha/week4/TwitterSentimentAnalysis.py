#0-negative 1-neutral 2-positive
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn import preprocessing
from nltk.corpus import twitter_samples
from nltk import NaiveBayesClassifier
import nltk.classify.util
from sklearn.externals import joblib
from nltk import classify
dataset=pd.read_csv("Tweets.csv")
def lemm():
    wordnet_lemmatizer = WordNetLemmatizer()
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
def bag_of_words(tweets):
    words_dictionary = dict([tweet,True] for tweet in tweets)
    return words_dictionary
def train():
    dneg=pd.read_csv("negative.csv")
    neg_tweets=dneg["Feature Words (Lemma)"].fillna("null")
    #neg_tweets = twitter_samples.strings('negative_tweets.json')
    dpos=pd.read_csv("positive.csv")
    pos_tweets=dpos["Feature Words (Lemma)"].fillna("null")
    #pos_tweets = twitter_samples.strings('positive_tweets.json')
    dneu=pd.read_csv("neutral.csv")
    neu_tweets=dneu["Feature Words (Lemma)"].fillna("null")
    #neu_tweets = twitter_samples.strings('neutral_tweets.json')
    pos_tweets_set=[]
    for tweet in pos_tweets:
        pos_tweets_set.append((bag_of_words(tweet.split(" ")),'pos'))
    neg_tweets_set=[]
    for tweet in neg_tweets:
        neg_tweets_set.append((bag_of_words(tweet.split(" ")),'neg'))
    neu_tweets_set=[]
    for tweet in neu_tweets:
        neu_tweets_set.append((bag_of_words(tweet.split(" ")),'neu'))
    xy=min(len(dpos),len(dneg),len(dneu))
    x=int(0.8*xy)
    y=int(0.2*xy)
    test_set=pos_tweets_set[:x]+neg_tweets_set[:x]+neu_tweets_set[:x]
    train_set=pos_tweets_set[y:]+neg_tweets_set[y:]+neu_tweets_set[y:]
    classifier = NaiveBayesClassifier.train(train_set)
    accuracy=classify.accuracy(classifier,test_set)
    joblib.dump(classifier,'ml_model.pkl')
    return accuracy*100
    
def view():
    no_of_pos, no_of_neg,no_of_neu = 0, 0, 0
    clf = joblib.load('ml_model.pkl')
    # print(clf.show_most_informative_features(5))
    sent=[]
    for row in range(dataset.shape[0]):
        prediction = clf.classify(bag_of_words(str(dataset['Feature Words (Lemma)'][row]).split(" ")))
        if prediction=='pos':
            no_of_pos+=1
            x=2
        elif prediction=='neu':
            no_of_neu+=1
            x=1
        elif prediction=='neg':
            x=0
            no_of_neg+=1
        sent.append(x)
    dataset["Predicted Sentiment"]=sent
    dataset.to_csv("Tweets.csv",index=False)
    a=train()
    print(f'Accuracy = {a:.2f}%')
    print("\nTotal Tweets = ",no_of_pos+no_of_neg+no_of_neu)
    print("\nNo. of positive tweets = ",no_of_pos,end="")
    print("\nNo. of negative tweets = ",no_of_neg,end="")
    print("\nNo. of neutral tweets = ",no_of_neu,end="")
lemm()
train()
view()