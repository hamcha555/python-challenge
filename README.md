# python-challenge

#PyBank

The total number of months included in the dataset
1) I began by creating a list of the month column and used len() operation minus one to determine nubmer of months in dataset.


The net total amount of "Profit/Losses" over the entire period
1) I created a list from the second column of data and format to float data type.  Once I was able to do this I could sum the list and determine Total Profit/Losses.


Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
1) I created loop to calculate difference between months using a for loop and range into a list.  Initiatlly tried to apply for loop on the list instead of a range and could not use list index to call data for calculation.  I did not undertand that running loop on list will not use list index and will use list value.  Also learned that I could use enumerate operation to apply index against list.
2) Summed the list of differenced and calculated the average


The greatest increase in profits (date and amount) over the entire period
<<<<<<< HEAD
The greatest decrease in profits (date and amount) over the entire period
1) use max/min operator to find max/min
2) use index to locate corresponding month
3) print in terminal

In addition, your final script should both print the analysis to the terminal and export a text file with the results.
1) print analysis in text file and in terminal


#PyPoll


I started the project but the data set was so large that I created a sample file to run and test python script quickly.  Since county data was irrelevant to the homework instructions I focused on candidates and votes.  By creating lists for each candidates votes.  


The total number of votes cast
I was able to sum up the lengths of each list to get total number of votes


A complete list of candidates who received votes
I created a seperate read operation to build candidate list and applied dictionary function to remove duplicates form the candidate list to determine complete list of candidates


The percentage of votes each candidate won
Using the candidate lists, I counted votes using len() operation and calculated percentages.  I also created a function **perc_formatter(x)** to format percentages to match homework example.


The total number of votes each candidate won
I used sum() operation on candidate lists to tally vote counts.

The winner of the election based on popular vote.
I had to go back to line 116 to manually build list for candidate vote percentages.  I used max() operation on this list and and if else statement to match the max against the winning candidate.  I tried to use a for loop to create the candidate vote percentage list, but could not and have a question if it is possible for the object of a function to be a concatentage string and variable


In addition, your final script should both print the analysis to the terminal and export a text file with the results.
Similar to the pyBank exercise, I printed analysis to the terminal and exported text file to the analysis folder
