# MAKE SURE First we'll import the os module
# This will allow us to create file paths across operating systems
# MAKE SURE Module for reading CSV files
import os
import csv

#---------------------------------------------------------
#-----pull csv file data-----
#  using activity 2.12-Stu_UdemyZip
#---------------------------------------------------------
budget_path = os.path.join('resources','budget_data.csv')


#Lists to store data
month = []
pl = []

with open(budget_path) as budget_file:
    budget_reader = csv.reader(budget_file, delimiter=",")
    for row in budget_reader:
        #add month
        month.append(row[0])
        print(month)

        #add profit & loss
        pl.append(row[1])
        

#---------------------------------------------------------
#-----Count the total number of months included in the dataset
#---------------------------------------------------------
        Total_Months = len(list(budget_reader)) - 1
        print(f"Total Months: {Total_Months}")

#---------------------------------------------------------
        #calculate total profit
#---------------------------------------------------------
        Total_pl = sum(pl[1:])
        print(f"Total Profit & Loss: {Total_pl}")
