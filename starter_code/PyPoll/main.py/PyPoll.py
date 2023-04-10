import csv
import os

#variable to save the file to a path.
electiondata_csv = os.path.join ("PyPoll","Resources","election_data.csv")

#var
total_votes = 0
candidate_options = []
candidate_votes = {}
county_names = []
county_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
largest_county_turnout = ""
largest_county_vote = 0


with open(electiondata_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter =",")
    header = next(csvreader)
    # Read the header
    header = next(csvreader)
  
    for row in csvreader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        county_name = row[1]
        # If the candidate does not match any existing candidate add it the
        # the candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1

        # county does not match any existing county in the county list.
        if county_name not in county_names:
            county_names.append(county_name)
            county_votes[county_name] = 0
       
        county_votes[county_name] += 1

with open("PyPoll.py1", "w") as txt_file:
    
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)
    
    for county in county_votes:
      
        county_vote = county_votes[county]
        county_percent = float(county_vote) / float(total_votes) * 100
        county_results = (
            f"{county}: {county_percent:.1f}% ({county_vote:,})\n")
        print(county_results, end="")
        txt_file.write(county_results)
        if (county_vote > largest_county_vote):
            largest_county_vote = county_vote
            largest_county_turnout = county

    largest_county_turnout = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"-------------------------\n")
    print(largest_county_turnout)
 
    txt_file.write(largest_county_turnout)

    for candidate_name in candidate_votes:

        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)

        txt_file.write(candidate_results)
        #winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
 
    txt_file.write(winning_candidate_summary)