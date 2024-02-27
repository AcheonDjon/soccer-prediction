
#Author: Jonathan Ramchandran
#Date: 2024-02-26
#Version: 1.0

#Load regular season data
import pandas as pd
from src.jr.utils import calculate_elo_rating

from src.jr.utils import game_outcome


dataset= pd.read_csv("./data/regular_season_data.csv", delimiter= ",",header=0)

#Sort the data by game id
# dataset.sort_values(by=['game_id'], inplace=True)

#set the outcome for each game
dataset['Outcome'] = dataset.apply(game_outcome, axis=1)


#caclulate the elo rating for each team
dataset["Home_Elo_Start"]= 1500
dataset["Away_Elo_Start"]= 1500
dataset["Home_Elo_End"]= 1500
dataset["Away_Elo_End"]= 1500

dataset.apply(lambda row: calculate_elo_rating(row,row["Home_Elo_Start"], row["Away_Elo_Start"], row["Outcome"]), axis=1)

print(dataset.head(20))

#save the elo ratings to a new file - call it elo_ratings_regular_round.csv
dataset.to_csv("./data/elo_ratings_regular_round_jr.csv", index=False)


#seprate out the final rating of the teams {team: rating} - call it elo_ratings_final.csv


#save the final ratings to a new file - will use this to predict the final round - use pandas to save the file