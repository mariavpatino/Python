# Import module os
import os
# Import module for reading CSV files
import csv

# Specify the path of the file to work with
election_data = os.path.join("election_data.csv")

# Setting variables -> setting counters. "If you are looping through your rows 
# and adding a total to the previous row, then you will need to start them at 0.
# Setting lists
candidates = []
number_votes = []
percent_votes = []
total_votes = 0

# Opening and reading the CSV file
with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Reading the header row. It is "next", so the code do not read the header in the csv 
    # and I just take into account from the second line -info I need-)
    csv_header = next(csvreader)

    # Going through each row of data after the header
    # It will skip the header 
    for row in csvreader:

        # The total number of votes included in the dataset
        total_votes = total_votes + 1 

        #  If the candidate is not in our list, add the candidate name to our list AND
        # add a vote for that person
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            number_votes.append(1)

            # Add a vote in for the candidate in the index       
        else:
            index = candidates.index(row[2])
            number_votes[index] = number_votes[index] + 1
    
    # Add info to percent_votes list -previously created-
    for votes in number_votes:
        percentage = (votes/total_votes) * 100
        # Round Number
        percentage = round(percentage)
        # Format
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    # Winner candidate
    winner = max(number_votes)
    # Index = Look for the name
    index = number_votes.index(winner)
    winning_candidate = candidates[index]

# Printing info
print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(total_votes)}")
print("-------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(number_votes[i])})")
print("-------------------------")
print(f"Winner: {winning_candidate}")
print("-------------------------")

# Export a file (txt format) with the results
output = open("output_textformat.txt", "w")

output.write("Election Results\n")
output.write("-------------------------\n")
output.write(f"Total Votes: {total_votes}\n")
output.write("-------------------------\n")
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(number_votes[i])})")
    output.write('{}\n'.format(line))
output.write(f"-------------------------\n")
output.write(f"Winner: {winning_candidate}\n")
output.write("-------------------------\n")                                                                                                                            