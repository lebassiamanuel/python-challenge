import os
import csv

Py_Bank_csv = os.path.join("Resources","budget_data.csv")

#store content in variables
profit = []
monthly_changes = []
date = []

count = 0
profit_total = 0
total_change_in_profits = 0
iprofit = 0

with open(Py_Bank_csv) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)
    csvheader = next(csvreader)
    print(f"csvheader is:  {csvheader}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        count = count + 1

        date.append(row[0])
        profit.append(row[1])
        
        
        profit_total = profit_total + int(row[1])
        fprofit = int(row[1])
        delta_monthly_profits = fprofit - iprofit

        monthly_changes.append(delta_monthly_profits)

        total_change_in_profits = total_change_in_profits + delta_monthly_profits

        iprofit = fprofit

        #Calculate the average change in profits
        average_change_profits = total_change_in_profits/count

        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)

        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        decrease_date = date[monthly_changes.index(greatest_decrease_profits)]


    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(profit_total))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")



with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(profit_total) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")
