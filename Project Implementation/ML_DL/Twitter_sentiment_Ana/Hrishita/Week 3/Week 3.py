import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, twitter_samples
import re
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import NaiveBayesClassifier
from nltk import classify
from sklearn.externals import joblib

df=pd.read_csv('twitter_project.csv',delimiter=',')
df.drop(['tweet_location','tweet_id','airline_sentiment_confidence','negativereason','negativereason_confidence','airline','airline_sentiment_gold','name','negativereason_gold','retweet_count','tweet_coord','tweet_created','user_timezone'],axis=1,inplace=True)

ls=LancasterStemmer()
lm=WordNetLemmatizer()
vectorizer=TfidfVectorizer()

stopWords=list(stopwords.words('english'))
stopWords.append('amp')
smilies = [':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
    ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
    '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
    'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
    '<3', ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
    ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
    ':c', ':{', '>:\\', ';(', '(', ')', 'via']

def cleaning_text(tweets):
    lemmatized=[]
    for text in tweets:
        text=text.lower()
        correction=TextBlob(text)
        text=correction.correct()
        words=text.split()
        filtered=[]
        for word in words:
            if(word not in smilies and word not in stopWords and not re.match(r"^@",word) and not re.match(r'https?://[A-Za-z0-9./]+',word) and not re.match(r'www\.[A-Za-z0-9]+',word)):
                filtered.append(word)
        filtered=' '.join(filtered)
        filtered=word_tokenize(filtered)
        cleaned=[]
        for token in filtered:
            if(token not in stopWords and token not in ".'?!" and token.isalpha() and len(token)>1):
                cleaned.append(token)
        lemma=[]
        for clean_word in cleaned:
            lemma.append(lm.lemmatize(clean_word,pos='a'))
        lemma=' '.join(lemma)
        lemmatized.append(lemma)
    return lemmatized


#tweet_data=list(df['text'])
#lemmatized_tokens=list(cleaning_text(tweet_data))
#df['lemma']=lemmatized_tokens

df.to_csv('twitter_project.csv',sep=',')

def vocab_gen(list_of_tweets,sent_of_tweet):
    sample_set=[]
    list_of_tweets=cleaning_text(list_of_tweets)
    for temp in list_of_tweets:
        word_dict=vectorizer.fit(temp.split(" "))
        sample_set.append((word_dict),sent_of_tweet)
    return sample_set

def ml_model():
    pos_tweets=twitter_samples.strings('positive_tweets.json')
    pos_tweets=vocab_gen(pos_tweets,'pos')
    neg_tweets=twitter_samples.strings('negative_tweets.json')
    neg_tweets=vocab_gen(neg_tweets,'neg')
    neu_tweets=twitter_samples.strings('neutral_tweets.json')
    neu_tweets=vocab_gen(neu_tweets,'neu')
    test_set=pos_tweets[:1000]+neg_tweets[:1000]+neu_tweets[:1000]
    train_set=pos_tweets[1000:]+neg_tweets[1000:]+neu_tweets[1000:]
    classifier=NaiveBayesClassifier.train(train_set)
    accuracy=classify.accuracy(classifier, test_set);
    print(accuracy)
    joblib.dump(classifier,'twitter_sent.pkl')
    







    
    






    





