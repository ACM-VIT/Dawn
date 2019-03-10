import numpy as np
import pandas as pd
import tweepy
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

#twitter credentials
consumer_key="78RUKFcecaqjFrsGp8RrMb4ws"
consumer_secret="BQ96RtxfFzCvjyqr9CTlkTjAybmWtSb0DADqd39v6ggPdXbJUg"
access_token="1099288373389254657-mULMkrrfb7LW8HgImyMJG8z0IciM9L"
access_token_secret="KCxIU2tvvr2yUyPhhjUBg1JOY4WxJ8Of26OeupCL4WUDE"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets_list=(api.user_timeline("POTUS", count=200))

tweets={'text':[]}
for tweet in tweets_list:
        tweets['text'].append(tweet.text)
        
df=pd.DataFrame(tweets, columns=['text'])
exported_csv=df.to_csv(r"C:\Users\Hrishita Chakrabarti\Desktop\twitter.csv")