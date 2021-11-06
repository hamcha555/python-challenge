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


The greatest decrease in profits (date and amount) over the entire period

