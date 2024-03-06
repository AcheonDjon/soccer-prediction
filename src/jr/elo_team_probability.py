import pandas as pd
import math

# Load the final predict CSV file
df = pd.read_csv('final_predict.csv')

# Calculate the final Elo rating of the two teams
team1_elo = df['team1_elo'].iloc[-1]
team2_elo = df['team2_elo'].iloc[-1]

# Compute the winning probability
winning_prob = 1 / (1 + math.pow(10, (team2_elo - team1_elo) / 400))

print(f"The winning probability of team 1 is: {winning_prob:.2%}")
print(f"The winning probability of team 2 is: {(1 - winning_prob):.2%}")