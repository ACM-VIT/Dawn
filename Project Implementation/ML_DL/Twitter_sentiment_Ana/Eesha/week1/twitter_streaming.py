import tweepy
import pandas as pd
import numpy as np
consumer_key=""
consumer_secret=""
access_key=""
access_secret=""

def get_tweets(username): #Function to extract tweets
    #Authorization to consusmer key and consumer secret
    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    #Access to user's access key and access secret
    auth.set_access_token(access_key,access_secret)
    #Calling API
    api=tweepy.API(auth)
    #200 tweets to be extracted
    tweets=api.user_timeline(screen_name=username,count=200)
    #Create dataset to store all values
    data=pd.DataFrame(data=[tweet.text for tweet in tweets],columns=['Tweets'])
    data['Length']=np.array([len(tweet.text) for tweet in tweets])
    data['ID']=np.array([tweet.id for tweet in tweets])
    data['Date']=np.array([tweet.created_at for tweet in tweets])
    data['Likes']=np.array([tweet.favorite_count for tweet in tweets])
    data['Retweets']=np.array([tweet.retweet_count for tweet in tweets])
    data['Sentiment'] =np.array(["" for tweet in tweets])
    data.to_csv('Twitter_data.csv',sep=',')

get_tweets("realDonaldTrump")
