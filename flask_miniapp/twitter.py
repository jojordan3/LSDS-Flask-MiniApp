'''Retrieve tweets, embeddings and persist in the database
'''
import tweepy
from decouple import config
import basilica
from .models import DB, Tweet, User


TWITTER_AUTH = tweepy.OAuthHandler(
    config('TWITTER_CONSUMER_KEY'),
    config('TWITTER_CONSUMER_SECRET')
    )
TWITTER_AUTH.set_access_token(
    config('TWITTER_ACCESS_TOKEN'),
    config('TWITTER_ACCESS_TOKEN_SECRET')
    )
TWITTER = tweepy.API(TWITTER_AUTH)

BASILICA = basilica.Connection(config('BASILICA_KEY'))

'''
>>>from flask_miniapp.twitter import *
>>>tweets = twitter_user.timeline(count=200, exclude_replies=True,
                                  include_rts=False, tweet_mode='extended')
>>>tweet_text = tweets[0].full_text
>>>embedding = BASILICA.embed_sentence(tweet_text, model='twitter')
'''
