#Import Libraries
import os
import csv

#create datafield from csv file
budget = os.path.join("budget_data.csv")

#values
total_months = 0
total_profit_loss = 0
value = 0
change = 0
dates = []
profits = []

#open and read file
with open('budget_data.csv')as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

	#read header row
    csv_header = next(csvreader)
	
	#read first row
    for row in csvreader:
        first_row = next(csvreader)
        total_months += 1
        total_profit_loss += int(first_row[1])
        value = int(first_row[1])

        #track dates
        dates.append(row[0])

        #track change in value
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])

        #total months
        total_months += 1

	#total profit and loss
        total_profit_loss = total_profit_loss + int(row[1])

#greatest increase
greatest_profit = max(profits)
greatest_index = profits.index(greatest_profit)
greatest_date = dates[greatest_index]

#greatest loss
greatest_loss = min(profits)
worst_index = profits.index(greatest_loss)
worst_date = dates[worst_index]

#average change 
ave_change = sum(profits)/len(profits)

#display findings
print("Financial Analysis")
print("---------------------")
print(f"total months: {str(total_months)}")
print(f"total: {str(total_profit_loss)}")
print(f"average change: {str(round(ave_change, 2))}")
print(f"Greatest Increase in Profits: {greatest_date} ({str(greatest_profit)})")
print(f"Greatest Decrease in Profits: {worst_date} ({str(greatest_loss)})")

#Exporing to .txt file
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_profit_loss)}")
line5 = str(f"Average Change: ${str(round(ave_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_profit)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_loss)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
