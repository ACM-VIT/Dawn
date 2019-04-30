import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
from nltk.stem import LancasterStemmer 

ls=LancasterStemmer()

stopWords=list(stopwords.words('english'))
stopWords.append('amp')

def cleaning_text(text):
    text=text.lower()
    words=text.split()
    filtered=[]
    for word in words:
        if(word not in stopWords and not re.match(r"^@",word) and not re.match(r'https?://[A-Za-z0-9./]+',word) and not re.match(r'www\.[A-Za-z0-9]+',word)):
            filtered.append(word)
    filtered=' '.join(filtered)
    filtered=word_tokenize(filtered)
    cleaned=[]
    for token in filtered:
        if(token not in stopWords and token not in ".'?!" and token.isalpha() and len(token)>1):
            cleaned.append(token)
    return ' '.join(cleaned)

def stemming_text(text):
    text=text.lower()
    stems=[]
    tokens=word_tokenize(text)
    for token in tokens:
        stems.append(ls.stem(token))
    return ' '.join(stems)

df=pd.read_csv('twitter_project.csv',delimiter=',')
df.drop(['tweet_location','tweet_id','airline_sentiment_confidence','negativereason','negativereason_confidence','airline','airline_sentiment_gold','name','negativereason_gold','retweet_count','tweet_coord','tweet_created','user_timezone'],axis=1,inplace=True)

tweets_list=list(df['text'])
clean_text=[]

for tweet in tweets_list:
    clean_text.append(cleaning_text(tweet))      
df['filtered_text']=clean_text

stemmed_tokens=[]
for cleaned in clean_text:
    stemmed_tokens.append(stemming_text(cleaned))
df['stemmed_text']=stemmed_tokens


print(df.info())

