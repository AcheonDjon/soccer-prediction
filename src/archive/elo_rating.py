import csv

def calculate_elo_rating(winner_rating, loser_rating):
    K = 32  # Elo rating constant
    expected_winner_score = 1 / (1 + 10 ** ((loser_rating - winner_rating) / 400))
    expected_loser_score = 1 - expected_winner_score
    updated_winner_rating = winner_rating + K * (1 - expected_winner_score)
    updated_loser_rating = loser_rating + K * (0 - expected_loser_score)
    return updated_winner_rating, updated_loser_rating

elo_ratings = {}

with open('regular.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        team1 = row[0]
        team2 = row[1]
        result = row[2]  # Assuming the result is '1' for team1 win and '0' for team2 win

        if team1 not in elo_ratings:
            elo_ratings[team1] = 1500  # Initial Elo rating for team1
        if team2 not in elo_ratings:
            elo_ratings[team2] = 1500  # Initial Elo rating for team2

        if result == '1':
            elo_ratings[team1], elo_ratings[team2] = calculate_elo_rating(elo_ratings[team1], elo_ratings[team2])
        else:
            elo_ratings[team2], elo_ratings[team1] = calculate_elo_rating(elo_ratings[team2], elo_ratings[team1])

# Print the Elo ratings for each team
for team, rating in elo_ratings.items():
    print(f"{team}: {rating}")