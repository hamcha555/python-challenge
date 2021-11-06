# MAKE SURE First we'll import the os module
# This will allow us to create file paths across operating systems
# MAKE SURE Module for reading CSV files
import os
import csv
from typing import Counter, DefaultDict

#---------------------------------------------------------
#-----pull csv file data-----
#---------------------------------------------------------
budget_path = os.path.join('resources','budget_data.csv')

# #Check for correct path
# print(budget_path)

# variables
month_sum = 0
pl_sum = 0
pldiff = 0
pldiff_sum = 0
pldiff_avg = 0
pl_max = 0
pl_min = 0
pl_max_ind = 0
pl_min_ind = 0
pl_max_month = ""
pl_min_month = ""
month_text = ""
profit_text = ""
profit_avg_text = ""
profit_max_text = ""
profit_min_text = ""

# lists
month_list = []
pl_list = []
pl_list_reverse = []
pldiff_list = []


#---------------------------------------------------------
# print analysis header in terminal
print(f"Financial Analysis")
print(f"----------------------------")
    

#---------------------------------------------------------
#-----Create Profit and Lost [list] and print total
#---------------------------------------------------------
with open(budget_path, 'r') as budget_file: 
    budget_reader = csv.reader(budget_file, delimiter = ",")
    budget_header = next(budget_reader)

    for row in csv.reader(budget_file, delimiter = ","):
        pl_list.append(row[1])
        month_list.append(row[0])

        #format list datatype to float
        pl_list = list(map(int, pl_list))
        
        # sum PL list
        pl_sum = sum(pl_list)
        month_sum = len(month_list)

month_text = (f"Total month: {month_sum}")
print(month_text)

profit_text = (f"Total: ${pl_sum}")
print(profit_text)

#=======================================================
## In order to run loop to start at the end, run reverse operaion on  pl_list 
#=======================================================
pl_list_reverse = pl_list[:]
pl_list_reverse.reverse()

# pldiff_a = 0 
# pldiff_b = 0
# # # print(pl_list[month_sum-1])

# pldiff = pl_list_reverse[0] - pl_list_reverse[1]
# print(pldiff)

# # enumerate(ints) creates a tuple with the value and index together
# for idx, val in enumerate(pl_list_reverse):
#     print(idx, val)

## CANNOT USE INDEX as this calls the value of the list in order.
## in this case "i" is NOT index.  For loop will ouput value
# for i in (pl_list_reverse):
#     pldiff = pl_list_reverse[i] - pl_list_reverse[i + 1]
#     print(pldiff)
#     pldiff_list.append(pldiff)

#     # pldiff_sum = pldiff_sum + pldiff
    
# idx = range(0, (len(month_list)- 1))
# print(idx)

# # enumerate(ints) creates a tuple with the value and index together
# for idx, val in enumerate(pl_list_reverse):
#     idx = range(0, (len(month_list)- 1))
#     pldiff = pl_list_reverse[idx] - pl_list_reverse[idx + 1]
#     pldiff_list.append(pldiff)

# enumerate(ints) creates a tuple with the value and index together in order to use operators on index
# List in the for loop
for idx in range(0, ((month_sum)-1)):
    pldiff = pl_list_reverse[idx] - pl_list_reverse[idx + 1]
    pldiff_list.append(pldiff)

#print(pldiff_list)

pldiff_avg = sum(pldiff_list) / ((month_sum) - 1)
pldiff_formatter = "{0:.2f}"
pldiff_avg_output = pldiff_formatter.format(pldiff_avg)

profit_avg_text = (f"Profit & Loss Average: ${pldiff_avg_output}")
print(profit_avg_text)


#=======================================================
#get max and min of pl_list
#=======================================================
pl_max = max(pl_list)
pl_min = min(pl_list)

#get the index of pl_max & pl_min
pl_max_ind = pl_list.index(pl_max)
pl_min_ind = pl_list.index(pl_min)

#get month of max and min
pl_max_month = month_list[pl_max_ind]
pl_min_month = month_list[pl_min_ind]

profit_max_text = (f"Greatest Increase in Profits: {pl_max_month} (${pl_max})")
print(profit_max_text)
profit_min_text = (f"Greatest Decrease in Profits: {pl_min_month} (${pl_min})")
print(profit_min_text)

#=======================================================
#Write to text file
#=======================================================
output_path = os.path.join("analysis", "PyBank analysis.txt")

with open(output_path, 'w') as f:

    f.write("Financial Analysis" + "\n")
    f.write("----------------------------" + "\n")
    f.write(month_text + "\n")
    f.write(profit_text + "\n")
    f.write(profit_avg_text + "\n")
    f.write(profit_max_text + "\n")
    f.write(profit_min_text)