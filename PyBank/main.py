#modules
import os
import csv

#file path
budget_csv = "budget_data.csv"

#list for total months
months = []

#variables
total_revenue = 0
greatest_increase = 0
greatest_decrease = 0
prev_revenue = 0
rev_change = 0
sum_rev_change = 0

#open csv
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    
    # Loop through the data
    for row in csv.reader(csvfile):
        
        #add months
        months.append(row[0])
        
        #find totals
        total_months = len(months)
        total_revenue = total_revenue + float(row[1])

        #average change
        rev_change =  float(row[1]) - prev_revenue
        sum_rev_change = sum_rev_change + rev_change       
        prev_revenue = float(row[1])

        #greatest increase/decrease
        if (rev_change > greatest_increase):
            greatest_increase = rev_change
            greatest_inc_date = str(row[0])
        
        if (rev_change < greatest_decrease):
            greatest_decrease = rev_change
            greatest_dec_date = str(row[0])

    
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_revenue}")
print(f"Average Change: ${(sum_rev_change) / (total_months)}")
print(f"Greatest Increase in Profits: {greatest_inc_date} {greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_dec_date} {greatest_decrease}")

file = open("output.txt", "w")
file.write("Financial Analysis\n")
file.write("----------------------------\n")
file.write(f"Total Months: {total_months}\n")
file.write(f"Total: ${total_revenue}\n")
file.write(f"Average Change: ${(sum_rev_change) / (total_months)}\n")
file.write(f"Greatest Increase in Profits: {greatest_inc_date} {greatest_increase}\n")
file.write(f"Greatest Decrease in Profits: {greatest_dec_date} {greatest_decrease}\n")
file.close()

