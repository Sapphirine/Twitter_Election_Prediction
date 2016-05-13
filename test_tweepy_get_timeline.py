# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 19:32:53 2016

@author: jonathanchang
"""
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from alchemyapi import AlchemyAPI
import tweepy
import time
import csv
import os.path
import json

alchemyapi = AlchemyAPI()

consumer_key = 'l5052mEBXWlUUMmPruYA5ZPwU'
consumer_secret = '74zApUjj5GztfJYNbj4KBctB3j3skCirmEoqLilQnKE5e1BuT2'
access_token = '3943692555-8ere0NGBIeVIor9fXnbvIry1OyJWk6XrH3rCTtE'
access_token_secret = 'i6xFpnDfNArsYTXgrRvZ3VZI6SQtR8NWh14ASGeHDVUfT'


'''
#Cathy's account:
consumer_key = '9VJSL3NotMkz5z6l9aExseS4H'
consumer_secret = 'SQbllMONUKhPKnseRnDI5PKCqRMG6hbtOKlRNBjx0dvEKZ40Qs'
access_token = '153439125-BdV8GS2ffVFkIsbpnFUKo0jtAHXGS3dvXXoXJCER'
access_token_secret = '0BTDeeAZl5VAagVR8nWhDiXFCfRopKPacks1aq7n02Wpy'
'''

def extractCandidate(text):
    candidate_keyword_dict = dict()

    candidate_keyword_dict['Clinton'] = ['#democrats', 'Hillary', 'Clinton', '#HillaryClinton', '#hillaryclinton',
    '@HillaryClinton', '#hillary2016', '#ImWithHer', '#HillaryEmails']
    candidate_keyword_dict['Trump'] = ['#republican', 'Donald', 'Trump', '#DonaldTrump', '#donaldtrump',
    '@realDonaldTrump', '#Trump2016', '#SaferThanATrumpRally', '#NeverTrump', '#MakeDonaldDrumpfAgain']
    candidate_keyword_dict['Sanders'] = ['Bernie', 'Sanders', '#berniesanders', '#feelthebern', '#bernie2016', '#berniesanders']
    candidate_keyword_dict['Cruz'] = ['Ted', 'Cruz', '#tedcruz', '#nevertrump']
    candidate_keyword_dict['Kasich'] = ['Kasich', '#johnkasich', '#kasich2016', '#writeinkasich', 'John Kasich', '#kasich']
    candidate_keyword_dict['Rubio'] = ['Marco', 'Rubio', '#marcorubio', '#nominatemarco']
    candidate_keyword_dict['Carson'] = ['Carson', '#bencarson', '#drcarson']

    for candidate in candidate_keyword_dict:
        for keyword in candidate_keyword_dict[candidate]:
            if keyword.lower() in text.lower():
                return candidate
    return 'no_match'


def getSentiment(text):
    '''
    Sentiment Analysis with AlchemyAPI
    '''
    myText = text
    response = alchemyapi.sentiment("text", myText)
    #print 'Alchemy results ----------> ' + str(response)
    if response['status'] == 'ERROR':
        return ('neutral', 0)
    else:
        if 'score' in response["docSentiment"]:
            return (response["docSentiment"]["type"], response["docSentiment"]["score"])
        else:
            return (response["docSentiment"]["type"], 0)

if __name__ == '__main__':

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    file_name = "realDonaldTrump_tweets.csv"

    if os.path.isfile(file_name):
        print "File already found"
        c = csv.writer(open(file_name, "a"))
    else:
        c = csv.writer(open(file_name, "wb"))
        c.writerow(["tweet_id","handle","text","sentiment type","sentiment score",
        "created_at","retweet_count","favorite_count","coordinates_lat","coordinates_lon"])

    c = csv.writer(open(file_name, "a"))

    stuff = api.user_timeline(screen_name = 'realDonaldTrump', count = 200, include_rts = True)

    for status in stuff:
        print status.text
        extracted_tweet_id = status.id
        extracted_handle = status.user.screen_name.encode('utf8')
        extracted_text = status.text.encode('utf8')
        extracted_created_at = status.created_at
        extracted_sentiment_score = getSentiment(status.text.encode('utf8'))[1]
        extracted_sentiment_type = getSentiment(status.text.encode('utf8'))[0]
        #extracted_sentiment_score = 0
        #extracted_sentiment_type = 0

        if status.coordinates is not None:
            extracted_coordinates_lat = status.coordinates[0]
            extracted_coordinates_lon = status.coordinates[1]
        else:
            extracted_coordinates_lat = 0
            extracted_coordinates_lon = 0


        extracted_favorite_count = status.favorite_count

        extracted_retweet_count = status.retweet_count

        csv_out_list = [extracted_tweet_id, extracted_handle, extracted_text, extracted_sentiment_type,
        extracted_sentiment_score, extracted_created_at, extracted_retweet_count, extracted_favorite_count,
        extracted_coordinates_lat, extracted_coordinates_lon]

        c.writerow(csv_out_list)
