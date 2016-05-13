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

class StdOutListener(StreamListener):

    def on_error(self, status):
        print status

    def on_status(self, status):

        print status.user.location
        extracted_candidate = extractCandidate(status.text.encode('utf8'))

        if status.user.location is not None and extracted_candidate != 'no_match':

            print 'Processing Tweet ----------> ' + status.text

            location_text = status.user.location.encode('utf8')
            extracted_state = extractState(location_text)


            if extracted_state != 'no_match':
                #extracted_candidate = extractCandidate(status.text.encode('utf8'))
                extracted_tweet_id = status.id
                extracted_handle = status.user.screen_name.encode('utf8')
                extracted_text = status.text.encode('utf8')
                extracted_created_at = status.created_at


                extracted_sentiment_score = getSentiment(status.text.encode('utf8'))[1]
                extracted_sentiment_type = getSentiment(status.text.encode('utf8'))[0]
                #extracted_sentiment_score = 0
                #extracted_sentiment_type = 0

                print '1'

                if status.coordinates is not None:
                    extracted_coordinates_lat = status.coordinates[0]
                    extracted_coordinates_lon = status.coordinates[1]
                else:
                    extracted_coordinates_lat = 0
                    extracted_coordinates_lon = 0


                #extracted_favorite_count = status.favorite_count

                #extracted_retweet_count = status.retweet_count

                csv_out_list = [extracted_tweet_id, extracted_handle, extracted_text,
                extracted_candidate, extracted_state, extracted_sentiment_type,
                extracted_sentiment_score, extracted_created_at, extracted_coordinates_lat,
                extracted_coordinates_lon]

                print 'here!'
                c.writerow(csv_out_list)


def extractState(text):
    state_keyword_dict = dict()
    state_keyword_dict['AL'] = ['Alabama', 'AL']
    state_keyword_dict['AK'] = ['Alaska', 'AK']
    state_keyword_dict['AZ'] = ['Arizona', 'AZ']
    state_keyword_dict['AR'] = ['Arkansas', 'AR']
    state_keyword_dict['CA'] = ['California', 'CA']
    state_keyword_dict['CO'] = ['Colorado', 'CO']
    state_keyword_dict['CT'] = ['Connecticut', 'CT']
    state_keyword_dict['DE'] = ['Delaware', 'DE']
    state_keyword_dict['FL'] = ['Florida', 'FL']
    state_keyword_dict['GA'] = ['Georgia', 'GA']
    state_keyword_dict['HI'] = ['Hawaii', 'HI']
    state_keyword_dict['ID'] = ['Idaho', 'ID']
    state_keyword_dict['IL'] = ['Illinois', 'IL']
    state_keyword_dict['IN'] = ['Indiana', 'IN']
    state_keyword_dict['IA'] = ['Iowa', 'IA']
    state_keyword_dict['KS'] = ['Kansas', 'KS']
    state_keyword_dict['KY'] = ['Kentucky', 'KY']
    state_keyword_dict['LA'] = ['Louisiana', 'LA']
    state_keyword_dict['ME'] = ['Maine', 'ME']
    state_keyword_dict['MD'] = ['Maryland', 'MD']
    state_keyword_dict['MA'] = ['Massachusetts', 'MA']
    state_keyword_dict['MI'] = ['Michigan', 'MI']
    state_keyword_dict['MN'] = ['Minnesota', 'MN']
    state_keyword_dict['MS'] = ['Mississippi', 'MS']
    state_keyword_dict['MO'] = ['Missouri', 'MO']
    state_keyword_dict['MT'] = ['Montana', 'MT']
    state_keyword_dict['NE'] = ['Nebraska', 'NE']
    state_keyword_dict['NV'] = ['Nevada', 'NV']
    state_keyword_dict['NH'] = ['New Hampshire', 'NH']
    state_keyword_dict['NJ'] = ['New Jersey', 'NJ']
    state_keyword_dict['NM'] = ['New Mexico', 'NM']
    state_keyword_dict['NY'] = ['New York', 'NY']
    state_keyword_dict['NC'] = ['North Caroline', 'NC']
    state_keyword_dict['ND'] = ['North Dakota', 'ND']
    state_keyword_dict['OH'] = ['Ohio', 'OH']
    state_keyword_dict['OK'] = ['Oklahoma', 'OK']
    state_keyword_dict['OR'] = ['Oregon', 'OR']
    state_keyword_dict['PA'] = ['Pennsylvania', 'PA']
    state_keyword_dict['RI'] = ['Rhode Island', 'RI']
    state_keyword_dict['SC'] = ['South Carolina', 'SC']
    state_keyword_dict['SD'] = ['South Dakota', 'SD']
    state_keyword_dict['TN'] = ['Tennessee', 'TN']
    state_keyword_dict['TX'] = ['Texas', 'TX']
    state_keyword_dict['UT'] = ['Utah', 'UT']
    state_keyword_dict['VT'] = ['Vermont', 'VT']
    state_keyword_dict['VA'] = ['Virginia', 'VA']
    state_keyword_dict['WA'] = ['Washington', 'WA']
    state_keyword_dict['WV'] = ['West Virginia', 'WV']
    state_keyword_dict['WI'] = ['Wisconsin', 'WI']
    state_keyword_dict['WY'] = ['Wyoming', 'WY']

    extracted_state = 'no_match'

    for state in state_keyword_dict:
        for keyword in state_keyword_dict[state]:
            if keyword in text:
                extracted_state = state
    return extracted_state

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

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    keyword_list = list()
    keyword_dict = dict()

    keyword_dict['Clinton'] = ['#democrats', 'Hillary', 'Clinton', '#HillaryClinton', '#hillaryclinton',
    '@HillaryClinton', '#hillary2016', '#ImWithHer', '#HillaryEmails']
    keyword_dict['Trump'] = ['#republican', 'Donald', 'Trump', '#DonaldTrump', '#donaldtrump',
    '@realDonaldTrump', '#Trump2016', '#SaferThanATrumpRally', '#NeverTrump', '#MakeDonaldDrumpfAgain']
    keyword_dict['Sanders'] = ['Bernie', 'Sanders', '#berniesanders', '#feelthebern', '#bernie2016', '#berniesanders']
    keyword_dict['Cruz'] = ['Ted', 'Cruz', '#tedcruz', '#nevertrump']
    keyword_dict['Kasich'] = ['Kasich', '#johnkasich', '#kasich2016', '#writeinkasich', 'John Kasich', '#kasich']
    keyword_dict['Rubio'] = ['Marco', 'Rubio', '#marcorubio', '#nominatemarco']
    keyword_dict['Carson'] = ['Carson', '#bencarson', '#drcarson']

    for key in keyword_dict:
        keyword_list += keyword_dict[key]

    print keyword_list

    file_name = "election_tweets.csv"

    if os.path.isfile(file_name):
        print "File already found"
        c = csv.writer(open(file_name, "a"))
    else:
        c = csv.writer(open(file_name, "wb"))
        c.writerow(["tweet_id","handle","text","candidate","state","sentiment type","sentiment score","created_at",
        "coordinates_lat","coordinates_lon"])

    c = csv.writer(open(file_name, "a"))

    stream = Stream(auth, l)
    #stream.filter(track=keyword_list, languages=['en'])

    while True:  #Endless loop: personalize to suit your own purposes
        try:
            stream.filter(track=keyword_list, languages=['en'])
        except:
            #e = sys.exc_info()[0]  #Get exception info (optional)
            #print 'ERROR:',e  #Print exception info (optional)
            continue
