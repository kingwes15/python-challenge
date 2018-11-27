import os
import csv

csvreadfile = os.path.join("budget_data.csv")
txtwritefile = os.path.join("budget_data_summary.txt")

months = []
date = []
ProfitLoss = []
MoM = []


with open(csvreadfile, "r", newline= "") as readfile:
    budget_data = csv.reader(readfile, delimiter = ",")
    net  = 0
    netprofit = 0
    avg_months = 0
    headerline = next(budget_data)
    for summary in budget_data:

        date.append(summary[0])
        months.append(summary)
        net += int(summary[1])
        ProfitLoss.append(int(summary[1]))
        maxprofit = max(ProfitLoss)
        minprofit = min(ProfitLoss)
        maxdate = date[ProfitLoss.index(maxprofit)]
        mindate = date[ProfitLoss.index(minprofit)]
        i = len(ProfitLoss)
        if len(ProfitLoss) > 1:
            change = ProfitLoss[i - 1] - ProfitLoss[i - 2]
            MoM.append(change)
            netprofit += int(MoM[i - 2])
            avg_months = len(months) - 1
            avg_change = round(netprofit / avg_months, 2)
            maxMoM = max(MoM)
            minMoM = min(MoM)

with open(txtwritefile, "w", newline= "") as budget_data_summary: #writefile:
    budget_data_summary.write("Financial Analysis \n")
    budget_data_summary.write("---------------------------- \n")
    budget_data_summary.write(f"Total Months: {len(months)} \n" )
    budget_data_summary.write(f"Total: ${net} \n")
    budget_data_summary.write(f"Average Change: ${avg_change} \n")
    budget_data_summary.write(f"Greatest Increase in Profits: {maxdate} (${maxMoM}) \n")
    budget_data_summary.write(f"Greatest Decrease in Profits: {mindate} (${minMoM}) \n")


#print(budget_data_summary)

with open(txtwritefile, "r") as readsummary:
   summaryread = readsummary.read()
   print(summaryread)

