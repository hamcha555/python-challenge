# MAKE SURE First we'll import the os module
# This will allow us to create file paths across operating systems
# MAKE SURE Module for reading CSV files
import os
import csv
from typing import Counter, DefaultDict

#---------------------------------------------------------
#-----pull csv file data-----
#---------------------------------------------------------
elec_path = os.path.join('resources','election_data_sample.csv')

# lists & variable
voteslist_1 = []
voteslist_2 = []
voteslist_3 = []
voteslist_4 = []
voteslist_5 = []
candlist_all = []
candlist_perc = []

votes_cand_1 = 0
votes_cand_2 = 0
votes_cand_3 = 0
votes_cand_4 = 0
votes_cand_5 = 0
votes_all = 0

perc_cand_1 = 0
perc_cand_2 = 0
perc_cand_3 = 0
perc_cand_4 = 0
perc_cand_5 = 0

cand_1 = "Khan"
cand_2 = "Correy"
cand_3 = "Li"
cand_4 = "O'Tooley"
cand_winner = ""
votes_text = ""
cand_1_text = ""
cand_2_text = ""
cand_3_text = ""
cand_4_text = ""
winner_text = ""

#---------------------------------------------------------
# Function to format percentage
#---------------------------------------------------------
def perc_formatter(x):
    pldiff_formatter = "{0:.3f}%"
    pldiff_avg_output = pldiff_formatter.format(x)
    return(pldiff_avg_output)


#---------------------------------------------------------
# print analysis header in terminal
print(f"Election Results")
print(f"----------------------------")


#---------------------------------------------------------
#-----Determine number of candidates
#---------------------------------------------------------
with open(elec_path, 'r') as elec_file: 
    elec_reader = csv.reader(elec_file, delimiter = ",")
    elec_header = next(elec_reader)

    ## build list of all candidates in row
    for row in elec_reader:
        candlist_all.append(row[2])

    ## create dictionary to remove duplicates.  no duplicates in dictionary
    candlist_all = list(dict.fromkeys(candlist_all))
    # print(len(candlist_all))


#---------------------------------------------------------
#-----METHOD 3 Read through each row and create lists for each candidate
#---------------------------------------------------------
with open(elec_path, 'r') as elec_file: 
    elec_reader = csv.reader(elec_file, delimiter = ",")
    elec_header = next(elec_reader)

    for row in elec_reader:

        if str(row[2]) == cand_1:
            voteslist_1.append(row[2])

        elif str(row[2]) == cand_2:
            voteslist_2.append(row[2])
            
        elif str(row[2]) == cand_3:
            voteslist_3.append(row[2])

        elif str(row[2]) == cand_4:
            voteslist_4.append(row[2])
        else:
            voteslist_5.append(row[2])
    
    #count total and candidate votes
    votes_all = len(voteslist_1) + len(voteslist_2) + len(voteslist_3) + len(voteslist_4) + len(voteslist_5)
    votes_cand_1 = len(voteslist_1)
    votes_cand_2 = len(voteslist_2)
    votes_cand_3 = len(voteslist_3)
    votes_cand_4 = len(voteslist_4)
    votes_cand_5 = len(voteslist_5)

    #calc percentage of candidate votes
    perc_cand_1 = votes_cand_1 / votes_all
    perc_cand_2 = votes_cand_2 / votes_all 
    perc_cand_3 = votes_cand_3 / votes_all 
    perc_cand_4 = votes_cand_4 / votes_all 
    perc_cand_5 = votes_cand_5 / votes_all 
    
    ##build list of candidate vote percentages
    candlist_perc = [perc_cand_1, perc_cand_2, perc_cand_3, perc_cand_4, perc_cand_5]

    ##????????????????????????????
    ## for the list.append(object) can you combine text and variable??
    ##?????????????????????????????
    # for idx in range(1, (len(candlist_all)+1)):
    #     candlist_perc.append('perc_cand_' + str(idx))
    #     print(candlist_perc)

    ##find highest percentage and build if statement to assign winner
    winner_perc = max(candlist_perc)

    if winner_perc == perc_cand_1:
        cand_winner = cand_1

    elif winner_perc == perc_cand_2:
        cand_winner = cand_2

    elif winner_perc == perc_cand_3:
        cand_winner = cand_3

    elif winner_perc == perc_cand_4:
        cand_winner = cand_4

    else:
        cand_winner = "missing candidate"
   
   #format candidate percentages using function 
    perc_cand_1 = perc_formatter(perc_cand_1)
    perc_cand_2 = perc_formatter(perc_cand_2)
    perc_cand_3 = perc_formatter(perc_cand_3)
    perc_cand_4 = perc_formatter(perc_cand_4)
        

# #---------------------------------------------------------
# #-----assign variables to analysis & print to terminal
# #---------------------------------------------------------

votes_text = (f"Total Votes: {votes_all}")
print(votes_text)
print(f"----------------------------")
cand_1_text = (f"{cand_1}: {perc_cand_1} ({votes_cand_1})")
cand_2_text = (f"{cand_2}: {perc_cand_2} ({votes_cand_2})")
cand_3_text = (f"{cand_3}: {perc_cand_3} ({votes_cand_3})")
cand_4_text = (f"{cand_4}: {perc_cand_4} ({votes_cand_4})")
print(cand_1_text)
print(cand_2_text)
print(cand_3_text)
print(cand_4_text)
print(f"----------------------------")
winner_text = (f"Winner: {cand_winner}")
print(winner_text)
print(f"----------------------------")



#=======================================================
#Write to text file
#=======================================================
output_path = os.path.join("analysis", "PyPoll analysis.txt")

with open(output_path, 'w') as f:

    f.write("Election Results" + "\n")
    f.write("----------------------------" + "\n")
    f.write(votes_text + "\n")
    f.write("----------------------------" + "\n")
    f.write(cand_1_text + "\n")
    f.write(cand_2_text + "\n")
    f.write(cand_3_text + "\n")
    f.write(cand_4_text + "\n")
    f.write("----------------------------" + "\n")
    f.write(winner_text + "\n")
    f.write("----------------------------")
    

# #---------------------------------------------------------
# #-----METHOD 2 Create FUNCTION
# #---------------------------------------------------------
# # Define the function and have it accept the 'elec_data' as its sole parameter
# def print_percentages(elec_data):
#     # For readability, it can help to assign your values to variables with descriptive names
#     voterID = str(elec_data[0])
#     county = str(elec_data[1])
#     candidate = int(elec_data[2])
    
#     # Total matches can be found by adding wins, losses, and draws together
#     # total_matches = wins + losses + draws


# #---------------------------------------------------------
# #-----METHOD 1 Create  [list] and print voter total
# #---------------------------------------------------------

        
# with open(elec_path, 'r') as elec_file: 
#     elec_reader = csv.reader(elec_file, delimiter = ",")
#     elec_header = next(elec_reader)

#     for row in csv.reader(elec_file, delimiter = ","):
#         voter_list.append(row[0])
#         county_list.append(row[1])
#         candidate_list.append(row[2])

#         voter_sum= len(voter_list)
    
#     print(f"Total Votes: {voter_sum}")
