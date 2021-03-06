# The data we need to retireve 
# 1. The total number of votes cast 
# 2. A complete list of canidates who recieved votes 
# 3. The percentage of votes each canidate won 
# 4. A total number of votes each canidate won 
# 5. The winner of the election based on popular vote 

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

import csv
from functools import total_ordering
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
# 1. Initialize a total vote counter 
total_votes=0

# Candidate options
candidate_options=[]
# Declare candidate dictonary
candidate_votes={}
# winning candidate and winning count tracker
winning_candidate=""
winning_count=0
winning_percentage=0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
    
       # Add to the total vote count. 
       total_votes+=1

       # Print the candidate name for each row.
       candidate_name=row[2]

       # If the candidate does not match the existing candidate...
       if candidate_name not in candidate_options:
           # add it to the list of candidates.
           candidate_options.append(candidate_name)
           #track the candidate's vote count. 
           candidate_votes[candidate_name]=0

       # add a vote to that candidate's count.
       candidate_votes[candidate_name]+=1 

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # determine winning vote count and candidate.
    # determine if the votes is greater than the winning count
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        winning_count=votes
        winning_percentage=vote_percentage
        winning_candidate=candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)    
    
