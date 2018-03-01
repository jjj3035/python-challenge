import os
import csv

path1 = os.path.join('election_data_1.csv')
path2 = os.path.join('election_data_2.csv')

files = [path1, path2]
votes = []
candidate_list = []

for file in files:
    with open(file, newline ='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter =',')
        next(csvreader, None)
        for row in csvreader:
            if row[2] in candidate_list:
                vote_count = int(row[0])
                votes[candidate_list.index(row[2])] = int(votes[candidate_list.index(row[2])]) + vote_count
            else:
                candidate_list.append(row[2])
                votes.append(int(row[0]))
                
total_votes = sum(votes)
max_votes = max(votes)
winner = candidate_list[votes.index(max_votes)]

with open("output.txt", 'w+') as text_file:
    print ('Election Results', file=text_file)
    print ('-------------------------', file=text_file)
    print ('Total Votes:',total_votes, file=text_file)
    print ('-------------------------', file=text_file)
    for candidate in candidate_list:
        vote_count = votes[candidate_list.index(candidate)]
        print (candidate,':','{:.2%}'.format(vote_count/total_votes),'(',vote_count,')', file=text_file)
    print ('-------------------------', file=text_file)
    print ('Winner:',winner, file=text_file)
    print ('-------------------------', file=text_file)
    
with open('output.txt', 'r') as text_file:
    for line in text_file.readlines():
        print (line)
