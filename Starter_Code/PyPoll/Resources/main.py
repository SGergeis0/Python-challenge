import csv

#open csv, skip header and name rows
with open('election_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) 

    total_votes = 0
    total_candidates = {}

    for row in reader:
        candidate = row[2]
        total_votes += 1
        total_candidates[candidate] = total_candidates.get(candidate, 0) + 1


results = []
for candidate, votes in total_candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, percentage, votes))

winner = max(results, key=lambda x: x[2])


print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, percentage, votes in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner[0]}")
print("-------------------------")

