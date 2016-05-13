from __future__ import division
import csv


'''
["tweet_id","handle","text","candidate","state","sentiment type","sentiment score","created_at",
"coordinates_lat","coordinates_lon"]
'''

candidate_name_list = ['Clinton','Trump']

clinton_tweet_count = 0
sanders_tweet_count = 0
trump_tweet_count = 0
cruz_tweet_count = 0
kasich_tweet_count = 0
rubio_tweet_count = 0
carson_tweet_count = 0

candidate_count_list = [0]*7
candidate_count_dict = dict()

with open("election_tweets_copy.csv", "rb") as f:
    #reader = csv.reader(f, delimiter="\t")
    reader = csv.reader(f)
    for i, line in enumerate(reader):
        #print 'line[{}] = {}'.format(i, line)
        #print line

        if line[3] == 'Clinton':
            clinton_tweet_count += 1
            candidate_count_list[0] += 1

            if line[4] not in candidate_count_dict:
                candidate_count_dict[line[4]] = [0]*7
                candidate_count_dict[line[4]][0] += 1
            else:
                candidate_count_dict[line[4]][0] += 1

        if line[3] == 'Trump':
            trump_tweet_count += 1
            candidate_count_list[1] += 1

            if line[4] not in candidate_count_dict:
                candidate_count_dict[line[4]] = [0]*7
                candidate_count_dict[line[4]][1] += 1
            else:
                candidate_count_dict[line[4]][1] += 1


total_percent_list = [x / sum(candidate_count_list) for x in candidate_count_list]
#print total_percent_list

candidate_percent_dict = dict()
for state in candidate_count_dict:
    temp_list = candidate_count_dict[state][:]
    candidate_percent_dict[state] = [0]*2

    for i in range(0,2):
        candidate_percent_dict[state][i] = candidate_count_dict[state][i] / sum(temp_list[0:2])

'''
Total USA analysis
'''
print '<<<<<<< Total for USA >>>>>>>>'
for i, candidate_name in enumerate(candidate_name_list):
    print candidate_name + ' percentage of total tweets: ' +  str(total_percent_list[i]*100) + '%'
'''
State specific analysis
'''
prediction_dict = dict()
for state in candidate_count_dict:
    print '<<<<<<< ' + state + ' >>>>>>>>'
    for i, candidate_name in enumerate(candidate_name_list):
        print candidate_name + ' percentage of total tweets: ' +  str(candidate_percent_dict[state][i]*100) + '%'

    clinton_percent = candidate_percent_dict[state][0]
    trump_percent = candidate_percent_dict[state][1]
    predicted_clinton_vote = clinton_percent*100*(1-0.194645659614)#.2118) #.2118
    predicted_trump_vote = trump_percent*100*(1-0.526207527965)#.4868) #.5368
    predicted_clinton_percent = predicted_clinton_vote / (predicted_clinton_vote + predicted_trump_vote)
    predicted_trump_percent = predicted_trump_vote / (predicted_clinton_vote + predicted_trump_vote)

    if predicted_clinton_percent > predicted_trump_percent:
        print 'Prediction: Clinton wins with: ' + str(predicted_clinton_percent*100) + '%'
        prediction_dict[state] = 'Clinton'
    else:
        print 'Prediction: Trump wins with: ' + str(predicted_trump_percent*100) + '%'
        prediction_dict[state] = 'Trump'

'''
Calculate Overall Winner based on Electoral Votes
'''

electoral_vote_dict = dict()
electoral_vote_dict['AK'] = 3
electoral_vote_dict['AL'] = 9
electoral_vote_dict['AR'] = 6
electoral_vote_dict['AZ'] = 11
electoral_vote_dict['CA'] = 55
electoral_vote_dict['CO'] = 9
electoral_vote_dict['CT'] = 7
#electoral_vote_dict['DC'] = 3
electoral_vote_dict['DE'] = 3
electoral_vote_dict['FL'] = 29
electoral_vote_dict['GA'] = 16
electoral_vote_dict['HI'] = 4
electoral_vote_dict['IA'] = 6
electoral_vote_dict['ID'] = 4
electoral_vote_dict['IL'] = 20
electoral_vote_dict['IN'] = 11
electoral_vote_dict['KS'] = 6
electoral_vote_dict['KY'] = 8
electoral_vote_dict['LA'] = 8
electoral_vote_dict['MA'] = 11
electoral_vote_dict['MD'] = 10
electoral_vote_dict['ME'] = 4
electoral_vote_dict['MI'] = 16
electoral_vote_dict['MN'] = 10
electoral_vote_dict['MO'] = 10
electoral_vote_dict['MS'] = 6
electoral_vote_dict['MT'] = 3
electoral_vote_dict['NC'] = 15
electoral_vote_dict['ND'] = 3
electoral_vote_dict['NE'] = 5
electoral_vote_dict['NH'] = 4
electoral_vote_dict['NJ'] = 14
electoral_vote_dict['NM'] = 5
electoral_vote_dict['NV'] = 6
electoral_vote_dict['NY'] = 29
electoral_vote_dict['OH'] = 18
electoral_vote_dict['OK'] = 7
electoral_vote_dict['OR'] = 7
electoral_vote_dict['PA'] = 20
electoral_vote_dict['RI'] = 4
electoral_vote_dict['SC'] = 9
electoral_vote_dict['SD'] = 3
electoral_vote_dict['TN'] = 11
electoral_vote_dict['TX'] = 38
electoral_vote_dict['UT'] = 6
electoral_vote_dict['VA'] = 13
electoral_vote_dict['VT'] = 3
electoral_vote_dict['WA'] = 12
electoral_vote_dict['WI'] = 10
electoral_vote_dict['WV'] = 5
electoral_vote_dict['WY'] = 3

clinton_electoral_vote_total = 0
trump_electoral_vote_total = 0
for state in electoral_vote_dict:
    if prediction_dict[state] == 'Clinton':
        clinton_electoral_vote_total += electoral_vote_dict[state]
    else:
        trump_electoral_vote_total += electoral_vote_dict[state]

print 'Clinton wins ' + str(clinton_electoral_vote_total) + ' electoral votes'
print 'Trump wins ' + str(trump_electoral_vote_total) + ' electoral votes'
