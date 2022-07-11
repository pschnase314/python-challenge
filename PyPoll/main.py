#import libraries used
import os
import csv

#locate files for input and output
csvfile=os.path.join("Resources","election_data.csv")
outputFile=os.path.join("analysis","results.txt")

#initialize list of names that each vote is for
votes=[]
#open file and read just the names of candidates the votes are for (ballot IDs and counties don't matter for this excercise)
with open(csvfile, encoding="utf") as f:
    csvreader=csv.reader(f,delimiter=",")
    for row in csvreader:
        votes.append(row[2])

#calculate number of votes excluding the header
n=len(votes)-1
#create a set from the list of names of candidates
#a set only includes one copy of each element, but does not have ordering
#votes[1:-1] is the list of names excluding the header (votes[0]) going all the way to the end of the list (votes[-1])
nameSet=set(votes[1:-1])
#we want ordering, so make a list of the unique names by turning the set back to a list
names=list(nameSet)
#sort the names in place to put them in the right order
names.sort()

#initialize number of votes for each candidate
counts=[]

#open file for output (overwriting it if it exists already)
results=open(outputFile,"w")
#print header
print("Election Results")
print("Election Results",file=results)
print("-------------------------")
print("-------------------------",file=results)
#print number of votes
print(f"Total Votes:  {n}")
print(f"Total Votes:  {n}",file=results)
print("-------------------------")
print("-------------------------",file=results)
#calculate and print name, percent of votes attained, and number of total votes
#votes.count(name) counts instances of name in votes array.  The number of times I call it might take a while for older hardware or for large numbers of votes, but the whole script ran in less than a second on my computer with the data provided.
#for loop iterates once per unique name
for name in names:
    print(f"{name}:  {round(votes.count(name)/n*100,3)}%  ({votes.count(name)})")
    print(f"{name}:  {round(votes.count(name)/n*100,3)}%  ({votes.count(name)})",file=results)
    counts.append(votes.count(name))
#find the candidate with the most votes
i=counts.index(max(counts))
print("-------------------------")
print("-------------------------",file=results)
#print the winner
print(f"Winner:  {names[i]}")
print(f"Winner:  {names[i]}",file=results)
print("-------------------------")
print("-------------------------",file=results)
#close the file
results.close()