import tweepy
from textblob import TextBlob
consumer_key='gclBIeqyiRqk61avfg60SeRtG'
consumer_value='nrwo4ACoOCIIEuCVcSjanSCiymecIZ45KuVS2j2Ydqke2A5H2c'
access_token='974658694037286912-Yvv1XaVlUNViJALRmyDCMWURoOa859S'
access_token_secret='WCpKxAw9OhgVwSSC8a7qd52Rpi0nwnnfCJM1wqNBcupV6'
auth=tweepy.OAuthHandler(consumer_key,consumer_value)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
public_tweets=api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis=TextBlob(tweet.text)
	print(analysis.sentiment)

