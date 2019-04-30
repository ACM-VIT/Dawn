import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
from nltk.stem import WordNetLemmatizer
from nltk import NaiveBayesClassifier
from nltk import classify
from sklearn.externals import joblib

df=pd.read_csv('Twitter_Project.csv',delimiter=',')
ds=pd.read_csv('dataset.csv',delimiter=',')
lm=WordNetLemmatizer()

stopWords=list(stopwords.words('english'))
stopWords.append('amp')

def cleaning(tweets):
    lemmas=[]
    for tweet in tweets:
        words=tweet.lower()
        words=words.split()
        filtered=[]
        for word in words:
            if((re.match(r"^#", word) or word.isalpha()) and word not in stopWords):
                filtered.append(word)
        tweet=' '.join(filtered)
        tokens=word_tokenize(tweet)
        lemma=[]
        for token in tokens:
            if(token.isalpha()):
                lemma.append(lm.lemmatize(token))
        lemma=' '.join(lemma)
        lemmas.append(lemma)
    return lemmas

tweets=list(df.Text)
pos_sample=ds.loc[ds['airline_sentiment']=='positive']
neg_sample=ds.loc[ds['airline_sentiment']=='negative']
neu_sample=ds.loc[ds['airline_sentiment']=='neutral']
lemmatized=list(cleaning(tweets))
df['Feature_Words']=lemmatized
df.to_csv('twitter_project.csv',sep=',',index='False')


def bag_of_words(tweet):
    words = cleaning(tweet)
    words_dictionary = dict([word, True] for word in words)
    return words_dictionary

def ml_model():   
    pos_tweets=list(pos_sample.text)
    neg_tweets=list(neg_sample.text)
    neu_tweets=list(neu_sample.text)
    pos_set=[]
    neg_set=[]
    neu_set=[]
    for tweet in pos_tweets:
        pos_set.append((bag_of_words(tweet),'pos'))
    for tweet in neg_tweets:
        neg_set.append((bag_of_words(tweet),'neg'))
    for tweet in neu_tweets:
        neu_set.append((bag_of_words(tweet),'neu'))
    for word in pos_set:
        if word[0] in neu_set or word[0] in neg_set:
            pos_set.remove(word)
            neg_set.remove(word)
            neu_set.remove(word)
    for word in neg_set:
        if word[0] in pos_set or word[0] in neu_set:
            pos_set.remove(word)
            neg_set.remove(word)
            neu_set.remove(word)
    for word in neu_set:
        if word[0] in neg_set or word[0] in pos_set:
            pos_set.remove(word)
            neg_set.remove(word)
            neu_set.remove(word)
    x=int(0.9*max(len(neg_set),len(pos_set),len(neu_set)))
    test_set=pos_set[x:]+neg_set[x:]+neu_set[x:]
    train_set=pos_set[:x]+neg_set[:x]+neu_set[:x]
    classifier=NaiveBayesClassifier.train(train_set)
    accuracy=classify.accuracy(classifier, test_set);
    print("Accuracy is ",accuracy)
    joblib.dump(classifier,'twitter_sent.pkl')

def analysis():
    ml_model()
    predictions=[]
    pos_count, neg_count, neu_count=0,0,0
    clsfr=joblib.load('twitter_sent.pkl')
    for tweet in tweets:
        prediction=clsfr.classify(bag_of_words(tweet))
        predictions.append(prediction)
        if(prediction=='pos'):
            pos_count+=1
        elif(prediction=='neg'):
            neg_count+=1
        else:
            neu_count+=1
    df['Sentiment']=predictions
    df.to_csv('twitter_project.csv',sep=',',index='False')
    print('No of positive tweets: ',pos_count)
    print('No of negative tweets: ',neg_count)
    print('No of neutral tweets: ',neu_count)
    if(pos_count>neg_count and pos_count>neu_count):
        print('Airline got its shit together')
    elif(neg_count>pos_count and neg_count>neu_count):
        print('Airline needs to get its shit together')
    else:
        print('Customer response is more boring than a history lesson')
        
analysis()
    