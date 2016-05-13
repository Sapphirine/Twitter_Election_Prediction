from __future__ import division
import csv
import time
import os.path
import json


'''
["tweet_id","handle","text","candidate","state","sentiment type","sentiment score","created_at",
"coordinates_lat","coordinates_lon"]
'''

candidate_name_list = ['Clinton','Sanders','Trump','Cruz','Kasich','Rubio']

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

        if line[3] == 'Sanders':
            sanders_tweet_count += 1
            candidate_count_list[1] += 1

            if line[4] not in candidate_count_dict:
                candidate_count_dict[line[4]] = [0]*7
                candidate_count_dict[line[4]][1] += 1
            else:
                candidate_count_dict[line[4]][1] += 1

        if line[3] == 'Trump':
            trump_tweet_count += 1
            candidate_count_list[2] += 1

            if line[4] not in candidate_count_dict:
                candidate_count_dict[line[4]] = [0]*7
                candidate_count_dict[line[4]][2] += 1
            else:
                candidate_count_dict[line[4]][2] += 1

        if line[3] == 'Cruz':
            cruz_tweet_count += 1
            candidate_count_list[3] += 1

            if line[4] not in candidate_count_dict:
                candidate_count_dict[line[4]] = [0]*7
                candidate_count_dict[line[4]][3] += 1
            else:
                candidate_count_dict[line[4]][3] += 1

        if line[3] == 'Kasich':
            kasich_tweet_count += 1
            candidate_count_list[4] += 1

            if line[4] not in candidate_count_dict:
                candidate_count_dict[line[4]] = [0]*7
                candidate_count_dict[line[4]][4] += 1
            else:
                candidate_count_dict[line[4]][4] += 1

        if line[3] == 'Rubio':
            rubio_tweet_count += 1
            candidate_count_list[5] += 1

            if line[4] not in candidate_count_dict:
                candidate_count_dict[line[4]] = [0]*7
                candidate_count_dict[line[4]][5] += 1
            else:
                candidate_count_dict[line[4]][5] += 1

        if line[3] == 'Carson':
            carson_tweet_count += 1
            candidate_count_list[6] += 1

            if line[4] not in candidate_count_dict:
                candidate_count_dict[line[4]] = [0]*7
                candidate_count_dict[line[4]][6] += 1
            else:
                candidate_count_dict[line[4]][6] += 1

total_percent_list = [x / sum(candidate_count_list) for x in candidate_count_list]
#print total_percent_list



candidate_percent_primary_results_dict = dict()
candidate_percent_primary_results_dict['AL'] = [.778,.192,.434,.211,.044,.187]
candidate_percent_primary_results_dict['AK'] = [.184,.816,.335,.365,.041,.151]
candidate_percent_primary_results_dict['AZ'] = [.668,.297,.328,.305,.037,.249]
candidate_percent_primary_results_dict['CT'] = [.518,.464,.579,.117,.284,.012]
candidate_percent_primary_results_dict['DE'] = [.598,.392,.608,.159,.204,.009]
candidate_percent_primary_results_dict['FL'] = [.644,.333,.457,.171,.068,.27]
candidate_percent_primary_results_dict['GA'] = [.713,.282,.388,.236,.056,.244]
candidate_percent_primary_results_dict['HI'] = [.3,.698,.424,.327,.106,.131]
candidate_percent_primary_results_dict['ID'] = [.212,.78,.281,.454,.074,.159]
candidate_percent_primary_results_dict['IL'] = [.505,.487,.388,.303,.197,.087]
candidate_percent_primary_results_dict['IN'] = [.475,.525,.533,.366,.076,.005]
candidate_percent_primary_results_dict['IA'] = [.499,.496,.243,.276,0,.231]
candidate_percent_primary_results_dict['KS'] = [.323,.677,.233,.482,.107,.167]
candidate_percent_primary_results_dict['LA'] = [.711,.232,.414,.378,.064,.112]
candidate_percent_primary_results_dict['ME'] = [.355,.643,.326,.459,.121,.08]
candidate_percent_primary_results_dict['MD'] = [.63,.332,.544,.189,.23,.007]
candidate_percent_primary_results_dict['MA'] = [.501,.487,.493,.096,.18,.179]
candidate_percent_primary_results_dict['MI'] = [.482,.498,.365,.249,.243,.093]
candidate_percent_primary_results_dict['MN'] = [.384,.616,.213,.29,.058,.365]
candidate_percent_primary_results_dict['MS'] = [.826,.165,.473,.363,.088,.051]
candidate_percent_primary_results_dict['MO'] = [.496,.494,.409,.407,.099,.061]
candidate_percent_primary_results_dict['NV'] = [.526,.473,.459,.214,.036,.239]
candidate_percent_primary_results_dict['NH'] = [.38,.604,.353,.117,.158,.106]
candidate_percent_primary_results_dict['NY'] = [.58,.42,.604,.145,.251,0]
candidate_percent_primary_results_dict['NC'] = [.546,.408,.402,.368,.127,.077]
candidate_percent_primary_results_dict['OH'] = [.565,.427,.356,.131,.468,.029]
candidate_percent_primary_results_dict['OK'] = [.415,.519,.283,.344,.036,.26]
candidate_percent_primary_results_dict['PA'] = [.556,.436,.567,.216,.194,.007]
candidate_percent_primary_results_dict['RI'] = [.436,.546,.636,.106,.246,.006]
candidate_percent_primary_results_dict['SC'] = [.735,.26,.325,.223,.076,.225]
candidate_percent_primary_results_dict['TN'] = [.661,.324,.389,.247,.053,.212]
candidate_percent_primary_results_dict['TX'] = [.652,.332,.267,.438,.042,.177]
candidate_percent_primary_results_dict['UT'] = [.203,.793,.14,.692,.168,0]
candidate_percent_primary_results_dict['VT'] = [.136,.861,.327,.097,.304,.193]
candidate_percent_primary_results_dict['VA'] = [.643,.352,.345,.169,.094,.319]
candidate_percent_primary_results_dict['WI'] = [.431,.566,.351,.482,.141,.01]
candidate_percent_primary_results_dict['WY'] = [.443,.557,.072,.663,0,19.5]

candidate_percent_dict = dict()
for state in candidate_percent_primary_results_dict:
    temp_list = candidate_count_dict[state][:]
    candidate_percent_dict[state] = [0]*7

    for i in range(0,2):
        candidate_percent_dict[state][i] = candidate_count_dict[state][i] / sum(temp_list[0:2])
    for i in range(2,6):
        candidate_percent_dict[state][i] = candidate_count_dict[state][i] / sum(temp_list[2:6])

'''
Total USA analysis
'''

primary_tweets_percent_list = candidate_count_list[:]
temp_candidate_count_list = candidate_count_list[:]
for i in range(0,2):
    primary_tweets_percent_list[i] = primary_tweets_percent_list[i]/sum(temp_candidate_count_list[0:2])
for i in range(2,6):
    primary_tweets_percent_list[i] = primary_tweets_percent_list[i]/sum(temp_candidate_count_list[2:6])

#print primary_tweets_percent_list

primary_results_percent_list = [0.5465,0.4535,0.5405,0.2893,0.08108,0.08903,0]

#print primary_results_percent_list

total_percent_diff_list = [0]*7

for i in range(0,6):
    total_percent_diff_list[i] = (primary_results_percent_list[i] - primary_tweets_percent_list[i])/(primary_results_percent_list[i])

for i, candidate_name in enumerate(candidate_name_list):
    print candidate_name + ' percentage of total tweets: ' +  str(primary_tweets_percent_list[i]*100) + '%'
    print candidate_name + ' percentage of primary delegates won: ' +  str(primary_results_percent_list[i]*100) + '%'
    print candidate_name + ' percentage difference: ' +  str(total_percent_diff_list[i]*100) + '%'

'''
State specific analysis
'''

total_percent_diff_dict = dict()
for state in candidate_percent_primary_results_dict:
    total_percent_diff_dict[state] = [0]*7

    for i in range(0,6):
        if candidate_percent_dict[state][i] != 0:
            total_percent_diff_dict[state][i] = (candidate_percent_dict[state][i] - candidate_percent_primary_results_dict[state][i])/candidate_percent_dict[state][i]
        else:
            total_percent_diff_dict[state][i] = 0

for state in candidate_percent_primary_results_dict:
    print '<<<<<<< ' + state + ' >>>>>>>>'
    for i, candidate_name in enumerate(candidate_name_list):
        print candidate_name + ' percentage of total tweets: ' +  str(candidate_percent_dict[state][i]*100) + '%'
        print candidate_name + ' percentage of primary delegates won: ' +  str(candidate_percent_primary_results_dict[state][i]*100) + '%'
        print candidate_name + ' percentage difference: ' +  str(total_percent_diff_dict[state][i]*100) + '%'

total_count = 0
total_clinton_percent_diff = 0
total_trump_percent_diff = 0

for state in total_percent_diff_dict:
    total_count += 1
    total_clinton_percent_diff += total_percent_diff_dict[state][0]
    total_trump_percent_diff += total_percent_diff_dict[state][2]

clinton_avg_percent_diff = total_clinton_percent_diff/total_count
trump_avg_percent_diff = total_trump_percent_diff/total_count

print 'A: ' + str(clinton_avg_percent_diff)
print 'B: ' + str(trump_avg_percent_diff)

'''
Write percent differences for each state to CSV
'''
file_name = "percent_diff_by_state.csv"

if os.path.isfile(file_name):
    print "File already found"
    c1 = csv.writer(open(file_name, "a"))
else:
    c1 = csv.writer(open(file_name, "wb"))
    c1.writerow(["state","clinton","trump"])

c1 = csv.writer(open(file_name, "a"))

for state in total_percent_diff_dict:
    csv_out = [state,total_percent_diff_dict[state][0],total_percent_diff_dict[state][2]]
    c1.writerow(csv_out)
