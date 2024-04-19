import os
import csv

EDC=os.path.join("election_data.csv")
#print(EDC)
#while working on this part of the sheet that if your 
#txt/csv file in in the same folder you only have to name 
#the file itself and not the path! NEET ALL THAT WORK IN THE PREVIOUS PAGE FOR NOTHING :D
with open(EDC, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csvheader=next(csvreader)
    candidate_roster=[candidate[2] for candidate in csvreader]
#print(candidate_roster)

VT=len(candidate_roster)

CV=[[candidate,candidate_roster.count(candidate)] for candidate in set(candidate_roster)]
CS=sorted(CV, key=lambda x:x[1], reverse=True)
#print(CS)
print("Election Results")
print("------------------------------------")
for candidate in CS:
    percentage=(candidate[1]/VT)*100
    print("--------------------------------------")
    print(f'{candidate[0]}:{percentage:6.3f}%({candidate[1]})')
# Thank you stack overflow and "Xpert Learning Assistant"

print("------------------------------------------------")
print(f'{CS[0][0]} is the winner! Congradulations')