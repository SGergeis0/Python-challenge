import csv

with open('budget_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  


    months = []
    total_profit = []
    monthly_profit_change = []



    for row in reader:
        months.append(row[0]) 
        total_profit.append(int(row[1]))



total_months = len(months)
profit_or_loss = sum(total_profit)
for i in range(1, total_months):
    change = total_profit[i] - total_profit[i-1]
    monthly_profit_change.append(change)



revenue_change = sum(monthly_profit_change)/ len(monthly_profit_change)

greatest_increase = max(monthly_profit_change)
greatest_decrease = min(monthly_profit_change)

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${profit_or_loss}")
print(f"Average Change: ${revenue_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease} (${greatest_decrease})")

