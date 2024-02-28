

import pandas as pd 

def load_final_data():
    """
    Load the final round data set from a file using pandas
    :return: A pandas DataFrame representing the data set
    """
    dataset = pd.read_csv('data/NSL_Knockout_Round_Games.csv', delimiter= ",",header=0)
    return dataset


df = load_final_data()
print(df.head())


def load_final_elo_ratings():
    """
    Load the final round Elo ratings from a file using pandas
    :return: A pandas DataFrame representing the Elo ratings
    """
    dataset = pd.read_csv('data/elo_ratings.csv', delimiter= ",",header=0)
    return dataset


#use the final elo to rating to get win probablity

df['home_elo_rating'] = df.apply(lambda row: 1 if row['HomeScore'] > row['AwayScore'] else 0, axis=1)