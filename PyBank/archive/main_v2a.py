# MAKE SURE First we'll import the os module
# This will allow us to create file paths across operating systems
# MAKE SURE Module for reading CSV files
import os
import csv
from typing import DefaultDict

#---------------------------------------------------------
#-----pull csv file data-----
#---------------------------------------------------------
budget_path = os.path.join('resources','budget_data.csv')

# #Check for correct path
# print(budget_path)

# lists & variable
months_sum = 0
pl_sum = 0
pl_diff_sum = 0
pl_list = []
pl_list_noheader = []


with open(budget_path, 'r') as budget_file:
    budget_reader = csv.reader(budget_file)

# # Shows object in memory has been created
#     print(budget_reader)

#---------------------------------------------------------
#-----Count the total number of months included in the dataset
#---------------------------------------------------------
    months_sum = len(list(budget_reader)) - 1
    print(f"Total Months: {months_sum}")

#---------------------------------------------------------
#-----Create Profit and Lost [list] and print total
#---------------------------------------------------------

        
with open(budget_path, 'r') as budget_file: 
    budget_reader = csv.reader(budget_file, delimiter = ",")
    
    for row in csv.reader(budget_file, delimiter = ","):
        pl_list.append(row[1])

        pl_list_noheader = list(pl_list)

        # remove header from list
        del(pl_list_noheader[0])

        #format list datatype to float
        pl_list_noheader = list(map(int, pl_list_noheader))
        
        # sum PL list
        pl_sum = sum(pl_list_noheader)

print(f"Total: ${pl_sum}")

print(pl_list_noheader["months_sum"])


