import os
import csv

#variable to save the file to a path
budgetdata_csv = os.path.join ("PyBank","Resources","budget_data.csv")

#Var
dates_list = []
Total_Month = 0
Net_Total = 0
Total_difference = []
previous_value = 0
current_value = 0
Value = 0
Average_Change =[]
Greatest_Increase = []
Greatest_Decrease = []
net_change_list = []


with open(budgetdata_csv,newline = '') as csvfile:
    File = csv.reader(csvfile,delimiter =",")
    listOfMonth = []
    for line in File:
        listOfMonth.append(line)
#Total Month    
    finalList = listOfMonth[1:]


for items in finalList:
    dates_list.append(items[0])
    Total_Month += 1
    Net_Total  += int(items[1])
#Total Difference
    Total_difference.append(int(items[1]))
#Average Difference
for x in range(Total_Month-1) :

    Average_Change.append(Total_difference[x+1]-Total_difference[x])  

Average_change_final = sum(Average_Change)/len(Average_Change)

#Greatest Increase in Profit
Greatest_Increase = [dates_list[Average_Change.index(max(Average_Change))],max(Average_Change)]
#Greatest Decrease in Profit
Greatest_Decrease = [dates_list[Average_Change.index(min(Average_Change))],min(Average_Change)]


with open("PyBank.py1", "w") as txt_file:


    print("Financial Analysis")
    print("_________________________________")
    print("Total Month   :",Total_Month)
    print("Net Total     :", Net_Total)
    print("Average Change :",Average_change_final)
    print("Greatest Increase in Profit :",Greatest_Increase)
    print("Greatest Decrease in Profit:",Greatest_Decrease)





        
        


       
        


    


        