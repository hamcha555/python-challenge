# MAKE SURE First we'll import the os module
# This will allow us to create file paths across operating systems
# MAKE SURE Module for reading CSV files
import os
import csv

#---------------------------------------------------------
#-----pull csv file data-----
#---------------------------------------------------------
budget_path = os.path.join('resources','budget_data.csv')

#Check for correct path
print(budget_path)

with open(budget_path, 'r') as budget_file:
    budget_reader = csv.reader(budget_file)


# Shows object in memory has been created
    print(budget_reader)

#---------------------------------------------------------
#-----Count the total number of months included in the dataset
#---------------------------------------------------------
    Total_Months = len(list(budget_reader)) - 1
    print(f"Total Months: {Total_Months}")

#---------------------------------------------------------
#-----Create p and l trying to create list for just PL column

        
with open(budget_path, 'r') as budget_file: 
    budget_reader = csv.reader(budget_file, delimiter = ",")
    
    pl_list = []
    pl_total = 0

    # skip first line of list
    next(budget_file)
    for row in budget_file:
        row.rstrip()
        pl_list.append(row)
        
        print(pl_list)

        # float(pl_list())


        
        # pl_total= sum(float(pl_list, 1))
        # # print(pl_total)

        # # pl_total = sum(pl_list[1:])
        # # print(pl_total)    