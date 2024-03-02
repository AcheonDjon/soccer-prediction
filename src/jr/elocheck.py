import pandas as pd 

elo_dict = pd.read_csv('./data/NSL_regular_season_final_elo_ratings.csv')

print(int(elo_dict['TUC']))