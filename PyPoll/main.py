import os
import csv

csvreaderfile = os.path.join("election_data.csv")
txtwriterfile = os.path.join("election_data_summary.txt")

candidates = []
votes = []
won_votes = {}
unique = []

with open(csvreaderfile, "r", newline= "") as readfile:
    election_data = csv.reader(readfile, delimiter = ",")

    headerline = next(election_data)
    for count in election_data:
        votes.append(count[0])
        candidates.append(count[2])
        VoterID, County, Candidate = count
        won_votes[Candidate] = won_votes.get(Candidate, 0) + 1
        max_votes = max(won_votes.values())
        winner = [ppls_choice for ppls_choice, most_votes in won_votes.items() if most_votes == max_votes]

for ppl in candidates:
    if ppl not in unique:
        unique.append(ppl)


i = 0
with open(txtwriterfile, "w", newline= "") as election_data_summary:
    election_data_summary.write(f"Election Results \n")
    election_data_summary.write(f"------------------------- \n")
    election_data_summary.write(f"Total Votes: {len(votes)}\n")
    election_data_summary.write(f"------------------------- \n")
    for results in unique:
        election_data_summary.write(f"{unique[i]}: {format(float(won_votes[unique[i]]) / float(len(votes)) * 100, '.3f')}% ({won_votes[unique[i]]})\n")
        i += 1
    election_data_summary.write(f"------------------------- \n")
    election_data_summary.write(f"Winner: {winner[0]} \n")
    election_data_summary.write(f"------------------------- \n")


with open(txtwriterfile, "r") as readsummary:
   summaryread = readsummary.read()
   print(summaryread)