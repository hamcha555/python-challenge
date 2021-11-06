# MAKE SURE First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# MAKE SURE Module for reading CSV files
import csv

#Create dictionary to hold month & p and l
p_and_l_dict = {
        "month": "null",
        "p_and_l": "null"
}

#---------------------------------------------------------
#-----pull csv file data-----
#---------------------------------------------------------

#csvpath = os.path.join('..', 'resources', 'accounting.csv')
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
# #---------------------------------------------------------
# #-----Create p and l dictionairy Sum and print the net total amount of "Profit/Losses" over the entire period
# #-----Context opening file----------------------------------------------------

# with open(budget_path, 'r') as budget_file:
#     budget_reader = csv.reader(budget_file)

#     for row in budget_reader:
#         p_and_l_dict["month"] = row[0]
#         p_and_l_dict["p_and_l"] = row[1]
    
#     print(p_and_l_dict["month"])
#     print(p_and_l_dict["p_and_l"])
#     print(p_and_l_dict)


#---------------------------------------------------------
#-----Sum and print the net total amount of "Profit/Losses" over the entire period
#---------------------------------------------------------

with open(budget_path, 'r') as budget_file:
    budget_reader = csv.reader(budget_file)

    Total_p_and_l = sum(list(budget_reader[1])

# #---------------------------------------------------------
#-----Print the total number of months included in the dataset
#---------------------------------------------------------

#   print(f"Total: {Total_p_and_l}")

#---------------------------------------------------------
#-----Create p and l dictionairySum and print the net total amount of "Profit/Losses" over the entire period
#---------------------------------------------------------


#---------------------------------------------------------
#-----Store csv data as 1) list OR 2) ZIPPED LIST OR 3) dictionary OR 4) Comprehension
#---------------------------------------------------------

    # for row in budget_reader:
    #     month = print(f"{row[0]}, ")