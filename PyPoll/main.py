import os
import csv

#file path
election_csv = "election_data.csv"

#lists
votes = []

#variables
khan_counter = 0
correy_counter = 0
otooley_counter = 0
li_counter = 0

#open csv
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # Loop through the data
    for row in csv.reader(csvfile):
        
        #total votes
        votes.append(row[0])
        total_votes = len(votes)

        #candidate vote counter
        if (row[2]) == "Khan":
            khan_counter = khan_counter + 1
        elif (row[2]) == "Correy":
            correy_counter = correy_counter +1
        elif (row[2]) == "O'Tooley":
            otooley_counter = otooley_counter + 1
        else: 
            li_counter = li_counter + 1

    #candidate percentages
    khan_percent = (khan_counter) / (total_votes) * 100
    correy_percent = (correy_counter) / (total_votes) * 100
    otooley_percent = (otooley_counter) / (total_votes) * 100
    li_percent = (li_counter) / (total_votes) * 100

    #winner
    vote_counter = [(khan_counter), (correy_counter), (otooley_counter), (li_counter)]
    num_winner = max(vote_counter)

    if num_winner == khan_counter:
        winner = "Khan"
    elif num_winner == correy_counter:
        winner = "Correy"
    elif num_winner == otooley_counter:
        winner = "O'Tooley"
    else: winner = "Li"

#results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Khan: {round(khan_percent)}% ({khan_counter})")
print(f"Correy: {round(correy_percent)}% ({correy_counter})")
print(f"Li: {round(li_percent)}% ({li_counter})")
print((f"O'Tooley: {round(otooley_percent)}% ({otooley_counter})"))
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

file = open("output.txt", "w")
file.write("Election Results\n")
file.write("-------------------------\n")
file.write(f"Total Votes: {total_votes}\n")
file.write("-------------------------\n")
file.write(f"Khan: {round(khan_percent)}% ({khan_counter})\n")
file.write(f"Correy: {round(correy_percent)}% ({correy_counter})\n")
file.write(f"Li: {round(li_percent)}% ({li_counter})\n")
file.write((f"O'Tooley: {round(otooley_percent)}% ({otooley_counter})\n"))
file.write("-------------------------\n")
file.write(f"Winner: {winner}\n")
file.write("-------------------------\n")
file.close()