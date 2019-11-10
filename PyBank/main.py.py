# Import module os
import os
# Import module for reading CSV files
import csv

# Specify the path of the file to work with
budget_data = os.path.join("budget_data.csv")

# Variables... setting counters. "If you are looping through your rows 
# and adding a total to the previous row, then you will need to start them at 0.
total_months = 0
total = 0
value = 0
change = 0
dates = []
profits = []

# Opening and reading the CSV file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Reading the header row. It is "next", so the code do not read the header in the csv 
    # and I just take into account from the second line -info I need-)
    csv_header = next(csvreader)

    # Reading the first row 
    first_row = next(csvreader) 
    # Reading the total months (It will jump through all the first column)
    total_months = total_months + 1
    # Reading the total AMOUNT (It will jump through all the values in 
    # position 1... since the second row -> will concatenate all the values
    # in column B from row 2)
    total = total + int(first_row[1])
    # 
    value = int(first_row[1])
    
    # Going through each row of data after the header
    # It will skip the header 
    for row in csvreader:
        # Track the dates
        dates.append(row[0])
        
        # Calculate the change in the position 1 of each 
        # row, then add it to the changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        # The total number of months included in the dataset
        total_months = total_months + 1

        # The net total amount of "Profit/Losses" over the entire period
        total = total + int(row[1])

    # The greatest increase in profits (date and amount) over the entire period:
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    # The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    # The average of the changes in "Profit/Losses" over the entire period
    avg_change = sum(profits)/len(profits)
    

# Printing info
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change:  ${round(avg_change,2)}")
print(f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {worst_date} (${greatest_decrease})")

# Export a file (txt format) with the results
output = open("output_textformat.txt", "w")

output.write("Financial Analysis\n")
output.write("----------------------------\n")
output.write(f"Total Months: {total_months}\n")
output.write(f"Total: ${total}\n")
output.write(f"Average Change: ${round(avg_change,2)}\n")
output.write(f"Greatest Increase in Profits: {greatest_date} ${greatest_increase}\n")
output.write(f"Greatest Decrease in Profits: {worst_date} ${greatest_decrease}\n")