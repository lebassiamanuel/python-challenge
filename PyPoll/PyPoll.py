import os
import csv

'''
You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", 
"County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of 
the following values:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote
'''


Py_Poll = os.path.join("Resources","election_data.csv")

list_candidate = []
unique_candidate = []
vote_count = []
percentOfVotes = []
count = 0

# Open the CSV using the set path PyPollcsv

with open(Py_Poll) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f"csvheader is:  {csv_header}")
  
    for row in csvreader:
        count = count + 1   # total number of vote counts
        list_candidate.append(row[2])
        # Create a set from the candidatelist to get the unique candidate names
    for n in set(list_candidate):
        unique_candidate.append(n)
        total_votes_per_candidate = list_candidate.count(n)
        vote_count.append(total_votes_per_candidate)
        # tvpc is the percent of total votes per candidate
        tvpc = (total_votes_per_candidate/count)*100
        percentOfVotes.append(tvpc)
        
    winningCount = max(vote_count)
    winner = unique_candidate[vote_count.index(winningCount)]
    
# Note to TA: I have tried several ways to get the max of the votecount list and retrieve the name as Winner. But unsucessful. 
# Hence I am leaving that part out of this code. But Khan is the winner, I know!!!!
# Jake suggested: votecount = votecount["percentage"].sort_values()
# Print to terminal
# Output perhaps needs to be rounded to 3 decimal points. Leaving that formatting out for now) 
 
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(percentOfVotes[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner + " with winning count of " + str(winningCount))
print("-------------------------")

# Print to a text file: election_results.txt
# Output perhaps needs to be rounded to 3 decimal points. Leaving that formatting out for now) 

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(percentOfVotes[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + " with winning count of " + str(winningCount) + "\n")
    text.write("---------------------------------------\n")