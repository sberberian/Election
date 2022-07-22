    # DATA WE NEED TO RETRIEVE



# Add our dependencies.
import csv

import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect save path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# (1a) Initialize a total voter counter
total_votes = 0

# (1b) Initialize candidate list 
candidate_options = []

# (1c) Initialize candidate_votes empty dictionary 
candidate_votes = {}

# (1e) Winning candidate and winning count tracker
winning_candidate = ""

winning_count = 0 

winning_percentage = 0 


# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
   


    # 1. TOTAL NUMBER OF VOTES CAST (a)

        # (2a) Add to the total vote count
        total_votes += 1



    # 2. COMPLETE LIST OF CANDIDATES WHO RECEIVED VOTES (b)

        # (2b) Print the candidate name from each row 
        candidate_name = row[2]

        # (3b) If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # (4b) Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # (2c) Begin tracking that candidate's vote count 
            candidate_votes[candidate_name] = 0

        # (3c) Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
    
    # (5e) Print and save final vote count to our text file 
    with open(file_to_save, "w") as txt_file:
        
        election_results = ( 
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        
        print(election_results, end="")

        txt_file.write(election_results)

        # 3. TOTAL NUMBER OF VOTES EACH CANDIDATE WON (c) 

        # 4. PERCENTAGE OF VOTES EACH CANDIDATE WON (d)

        # (1d) Iterate through the candidate list 
        for candidate_name in candidate_votes:
            
            # (2d) Retrieve vote couunt of a candidate
            votes = candidate_votes[candidate_name]

            # (3d) Calculate the percentage of votes 
            vote_percentage = float(votes) / float(total_votes) * 100

            # (4d) Print candidate name, voter count, and percentage
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            print(candidate_results)

            # Save candidate results to text file
            txt_file.write(candidate_results)

        # 5. WINNER OF ELECTION BASED ON POPULAR VOTE (e)

            # (1e) Determine winning vote count and candidate
            # (1e) Determine if the votes are greater than the winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):

                # (2e) If true then set winning_count = votes and winning_percent = vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage

                # (3e) Set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
        
        # (4e) Print the winning candidates' results to the terminal 
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)

        # Save the winning candidate's name to the text file
        txt_file.write(winning_candidate_summary)
