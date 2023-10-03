# import the module
import tweepy
import os
import pandas as pd
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# assign the values accordingly
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
bearer_token = os.getenv('BEARER_TOKEN')

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)

# the screen name of the user
name = "Nimroddj"


try:
    #The number of tweets we want to retrieved from the user
    tweets = api.user_timeline(screen_name=name, count=10)
    
    #Pulling Some attributes from the tweet
    attributes_container = [[tweet.created_at, tweet.favorite_count,tweet.source,  tweet.text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
    columns = ["Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
    #Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
        
    #Save the dataframe as a csv file
    tweets_df.to_csv('tweets.csv', index=False)
except BaseException as e:
    print('Status Failed On,',str(e))

