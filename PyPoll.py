import csv
import os

# 1. Open the data file.
# 2. Write down the names of all the candidates.
# 3. Add a vote count for each candidate.
# 4. Get the total votes for each candidate.
# 5. Get the total votes cast for the election.

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#contains candidates
candidate_options = []

#votes per candidate 
candidate_votes = {}

#contains total votes
total_votes = 0

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(str(headers) + "\n")

    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    for candidate in candidate_options:

        votes = candidate_votes[candidate]

        vote_percentage = float(votes)/float(total_votes) * 100

        print(candidate + " " + str(format(vote_percentage, '.1f')) + "% (" + str(votes) + ")\n")
         
        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if votes > winning_count:
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.

            winning_count = votes
            winning_percentage = vote_percentage

            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate


    print("-------------------------------\n")
    print("Winner: " +  str(winning_candidate) + "\n")
    print("Winning Vote Count: " +  str(winning_count) + "\n")
    print("Winning Percentage: " +  str(winning_percentage) + "\n")
    print("-------------------------------\n")
        


# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     txt_file.write("Countries in the Election\n")

     txt_file.write("-------------------------\n")

     # Write three counties to the file.
     txt_file.write("Arapahoe\nDenver\nJefferson")
