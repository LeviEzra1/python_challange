from pathlib import Path
import csv

EDC=Path(__file__).parent.joinpath("election_data.csv")
#print(EDC)
#while working on this part of the sheet that if your 
#txt/csv file in in the same folder you only have to name 
#the file itself and not the path! NEET ALL THAT pytWORK IN THE PREVIOUS PAGE FOR NOTHING :D
with open(EDC, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csvheader=next(csvreader)
    candidate_roster=[candidate[2] for candidate in csvreader]
#print(candidate_roster)

VT=len(candidate_roster)

CV=[[candidate,candidate_roster.count(candidate)] for candidate in set(candidate_roster)]
CS=sorted(CV, key=lambda x:x[1], reverse=True)
#print(CS)

TXTe = Path(__file__).parent.joinpath("TXTe.txt")
with open(TXTe, "w") as textfile:
    print("Election Results", file=textfile)
    print("------------------------------------", file=textfile)
    print(f"Total Votes: {VT}", file=textfile)
    print("------------------------------------", file=textfile)
    for candidate in CS:
        percentage=(candidate[1]/VT)*100
        print(f'{candidate[0]}: {percentage:6.3f}%({candidate[1]})', file=textfile)
    # Thank you stack overflow and "Xpert Learning Assistant"

    print("------------------------------------------------", file=textfile)
    print(f'{CS[0][0]} is the winner! Congradulations', file=textfile)