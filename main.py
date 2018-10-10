import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'YOUR-CONSUMER-KEY'              #it is our consumer-key of our developer account
consumer_secret = 'YOUR-CONSUMER-SECRET'        #it is our consumer-secret code of our developer account
access_token = 'YOUR-ACCESS-TOKEN'              #it is our access-token of our developer account
access_secret = 'YOUR-ACCESS-SECRET'            #it is our access-secret code of our developer account
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)


#to read my own timeline i will use
for status in tweepy.Cursor(api.home_timeline).items(10):    #due to 10 items it will select only 10 tweets from my homepage.
  print(status.text)
  
 
  
