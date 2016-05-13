from __future__ import division
import csv


'''
["tweet_id","handle","text","candidate","state","sentiment type","sentiment score","created_at",
"coordinates_lat","coordinates_lon"]
'''

candidate_name_list = ['Clinton','Trump']

clinton_positive_tweet_count = 0
clinton_negative_tweet_count = 0
clinton_total_tweet_count = 0
trump_positive_tweet_count = 0
trump_negative_tweet_count = 0
trump_total_tweet_count = 0
sanders_positive_tweet_count = 0
sanders_negative_tweet_count = 0
sanders_total_tweet_count = 0
cruz_positive_tweet_count = 0
cruz_negative_tweet_count = 0
cruz_total_tweet_count = 0
kasich_positive_tweet_count = 0
kasich_negative_tweet_count = 0
kasich_total_tweet_count = 0
rubio_positive_tweet_count = 0
rubio_negative_tweet_count = 0
rubio_total_tweet_count = 0

with open("election_tweets_sentiment.csv", "rb") as f:
    #reader = csv.reader(f, delimiter="\t")
    reader = csv.reader(f)
    for i, line in enumerate(reader):
        #print 'line[{}] = {}'.format(i, line)
        #print line

        if line[3] == 'Clinton':
            clinton_total_tweet_count += 1

        if line[5] == 'positive' and line[3] == 'Clinton':
            clinton_positive_tweet_count += 1

        if line[5] == 'negative' and line[3] == 'Clinton':
            clinton_negative_tweet_count += 1

        if line[3] == 'Trump':
            trump_total_tweet_count += 1

        if line[5] == 'positive' and line[3] == 'Trump':
            trump_positive_tweet_count += 1

        if line[5] == 'negative' and line[3] == 'Trump':
            trump_negative_tweet_count += 1

        if line[3] == 'Sanders':
            sanders_total_tweet_count += 1

        if line[5] == 'positive' and line[3] == 'Sanders':
            sanders_positive_tweet_count += 1

        if line[5] == 'negative' and line[3] == 'Sanders':
            sanders_negative_tweet_count += 1

        if line[3] == 'Cruz':
            cruz_total_tweet_count += 1

        if line[5] == 'positive' and line[3] == 'Cruz':
            cruz_positive_tweet_count += 1

        if line[5] == 'negative' and line[3] == 'Cruz':
            cruz_negative_tweet_count += 1

        if line[3] == 'Kasich':
            kasich_total_tweet_count += 1

        if line[5] == 'positive' and line[3] == 'Kasich':
            kasich_positive_tweet_count += 1

        if line[5] == 'negative' and line[3] == 'Kasich':
            kasich_negative_tweet_count += 1

        if line[3] == 'Rubio':
            rubio_total_tweet_count += 1

        if line[5] == 'positive' and line[3] == 'Rubio':
            rubio_positive_tweet_count += 1

        if line[5] == 'negative' and line[3] == 'Rubio':
            rubio_negative_tweet_count += 1

print 'Percentage positive Clinton tweets: ' + str((clinton_positive_tweet_count/clinton_total_tweet_count)*100) + '%'
print 'Percentage negative Clinton tweets: ' + str((clinton_negative_tweet_count/clinton_total_tweet_count)*100) + '%'
print 'Percentage positive Sanders tweets: ' + str((sanders_positive_tweet_count/sanders_total_tweet_count)*100) + '%'
print 'Percentage negative Sanders tweets: ' + str((sanders_negative_tweet_count/sanders_total_tweet_count)*100) + '%'
print 'Percentage positive Trump tweets: ' + str((trump_positive_tweet_count/trump_total_tweet_count)*100) + '%'
print 'Percentage negative Trump tweets: ' + str((trump_negative_tweet_count/trump_total_tweet_count)*100) + '%'
print 'Percentage positive Cruz tweets: ' + str((cruz_positive_tweet_count/cruz_total_tweet_count)*100) + '%'
print 'Percentage negative Cruz tweets: ' + str((cruz_negative_tweet_count/cruz_total_tweet_count)*100) + '%'
print 'Percentage positive Kasich tweets: ' + str((kasich_positive_tweet_count/kasich_total_tweet_count)*100) + '%'
print 'Percentage negative Kasich tweets: ' + str((kasich_negative_tweet_count/kasich_total_tweet_count)*100) + '%'
print 'Percentage positive Rubio tweets: ' + str((rubio_positive_tweet_count/rubio_total_tweet_count)*100) + '%'
print 'Percentage negative Rubio tweets: ' + str((rubio_negative_tweet_count/rubio_total_tweet_count)*100) + '%'
