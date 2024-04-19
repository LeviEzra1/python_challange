import os
import csv

BDC = os.path.join("budget_data.csv")

 #print(BDC)

BD = []

with open(BDC) as csvfile:
    BDR=csv.DictReader(csvfile)
for row in BDR: 
    BD.append({"Month": row["Date"], "Amount": int(row["Profit/Losses"]),"change": 0})

total_months=len(BD)

Previous_A=BD[0]["amount"]

for i in range(total_months):
    BD[i]["change"]=BD[i]["amount"] - Previous_A
    Previous_A=BD[i]["amount"]
#print(BD)

Total_A=sum(row["amount"] for row in BD)

TRC=sum(row["change"] for row in BD)
Average=round(TRC/(total_months-1),2)
 #print(Average)

GI=max(BD, key=lambda x:x["change"])
#this code was found by study group (sorry i forgot the name)
GD=min(BD, key=lambda x:x["change"])

Final_R=[("PBA"), 
    (f'Total Months: {total_months}'),
    (f'total: {Total_A}'),
    (f'Average Change: {Average}'),
    (f'Greatest Increase: {GI["month"]} ${GI["change"]}'),
    (f'Greatest Decrease: {GD["month"]} ${GD["change"]}')]
print(Final_R)

TXTf=os.path.join("TXTf.txt")
with open(TXTf, "w") as textfile:
    print("PBA",file=textfile)
    print("---------------------", file=textfile)
    print(f'Total Months: {total_months}', file=textfile)
    print(f'Total: {Total_A}',file=textfile)
    print(f'Average Change: {Average}',file=textfile)
    print(f'Greatest Increase: {GI["month"]} ${GI["change"]}', file=textfile)
    print(f'Greatest Decrease: {GD["month"]} ${GD["change"]}', file=textfile)