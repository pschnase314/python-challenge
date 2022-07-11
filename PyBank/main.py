#import libraries used
import os
import csv

#find the data file
csvfile=os.path.join("Resources","budget_data.csv")

#initialize arrays for month names and profit/loss that month
months=[]
profit=[]

#open data file
with open(csvfile,encoding="utf") as f:
    csvreader=csv.reader(f,delimiter=",")
    #read data for months and profit/loss
    for row in csvreader:
        months.append(row[0])
        profit.append(row[1])

#open output file for writing (overwriting it if it already exists)
outputPath=os.path.join("analysis","analysis.txt")
out=open(outputPath,"w")

#print header to terminal and file
print("Financial Analysis")
print("Financial Analysis",file=out)
print("----------------------------")
print("----------------------------",file=out)

#calculate and print number of months (excluding the header)
n=len(months)-1
print(f"Total Months:  {n}")
print(f"Total Months:  {n}",file=out)
#turn profits into numbers.  
#The ranges start with 1 instead of 0 because months[0] and profit[0] are headers for the columns.
for i in range(1,n+1):
    profit[i]=int(profit[i])
#add up and print total profits
total=sum(profit[1:n+1])
print(f"Total:  ${total}")
print(f"Total:  ${total}",file=out)
#dp is difference in profits from month to month
dp=[]
for i in range(1,n):
    dp.append(profit[i+1]-profit[i])
#initialize minimum and maximum change in profits
maxP=dp[0]
minP=dp[0]
#initialize months with minimum and maximum change in profits
maxM=months[1]
minM=months[1]
#find months with minimum and maximum change in profits
for i in range(0,n-1):
    if dp[i]>maxP:
        maxP=dp[i]
        maxM=months[i+2]
    elif dp[i]<minP:
        minP=dp[i]
        minM=months[i+2]
#average change in profits is just difference between the first and last months' profits divided by number of changes in profits.  All other terms in the sum cancel out.
#print average change in profits
print(f"Average Change: ${round((profit[n]-profit[1])/(n-1),2)}")
print(f"Average Change: ${round((profit[n]-profit[1])/(n-1),2)}",file=out)
#print greatest increase and decrease in profits
print(f"Greatest Increase in Profits: {maxM} (${maxP})")
print(f"Greatest Increase in Profits: {maxM} (${maxP})",file=out)
print(f"Greatest Decrease in Profits: {minM} (${minP})")
print(f"Greatest Decrease in Profits: {minM} (${minP})",file=out)
#close output file
out.close()