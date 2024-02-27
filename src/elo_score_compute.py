import pandas as pd 


def load_csv_dataset(file_path):
    dataset = pd.read_csv(file_path, delimiter= ",", header=0)
    return dataset  

def get_game_id(game_id_string):
    game_id = game_id_string.split('_')[2]
    return int(game_id)


def determine_outcome(row):
    if row['HomeScore'] > row['AwayScore']:
        return 1 #home win
    #adding resolution for draws
    elif row['HomeScore'] == row['AwayScore']:
           if row['Home_xG'] >= row['Away_xG']:
              return 1 #home win        
           else:
              return 0 #away win
    else:
        return 0 
    

#calcualte elo rating
    def calculate_elo_rating(df, elo_ratings, k):
        for index, row in df.iterrows():
            home_team = row['HomeTeam']
            away_team = row['AwayTeam']
            home_elo = elo_ratings[home_team]
            away_elo = elo_ratings[away_team]
            outcome = determine_outcome(row)

            # Calculate expected outcome
            home_expected = 1 / (1 + 10 ** ((away_elo - home_elo) / 400))
            away_expected = 1 - home_expected

            # Update Elo ratings
            home_new_elo = home_elo + k * (outcome - home_expected)
            away_new_elo = away_elo + k * ((1 - outcome) - away_expected)

            # Update Elo ratings in the dictionary
            elo_ratings[home_team] = home_new_elo
            elo_ratings[away_team] = away_new_elo

        return elo_ratings

#start here     
df = load_csv_dataset('data/regular.csv')

#add a new column to the dataframe
df['game_ordered_id'] = df['game_id'].apply(get_game_id)

#sort the data frame by the game they played
df.sort_values(by=['game_ordered_id'], inplace=True)

#set starting elo rating for away and home team to 1500

unique_hometeams = df['HomeTeam'].unique()

#create a dictionary for all teams with initial rating of 1500
elo_ratings = {team: 1500 for team in unique_hometeams}

#iterate through the rows of the dataframe
for index , each_row in df.iterrows():
    print(f"The home team {each_row['HomeTeam']} is playing against Away Team {each_row['AwayTeam']} and the game id is {each_row['game_ordered_id']}" )

    #Calcualate Home Team Elo Rating after each game  
    # Constants
    k = 25  # K-factor for Elo ratings
    actual_outcome = determine_outcome(each_row)

    #get current elo rating 
    home_elo = elo_ratings.get(each_row['HomeTeam'])
    away_elo = elo_ratings.get(each_row['AwayTeam'])

    df.at[index, 'home_elo_start'] = home_elo
    df.at[index, 'away_elo_start'] = away_elo

    # Calculate expected outcome
    home_expected = 1 / (1 + 10 ** ((away_elo - home_elo) / 400))
    away_expected = 1 - home_expected

    # Update Elo ratings
    home_new_elo = home_elo + k * (actual_outcome - home_expected)
    away_new_elo = away_elo + k * ((1 - actual_outcome) - away_expected)

    # Update Elo ratings in the dictionary
    elo_ratings[each_row['HomeTeam']] = home_new_elo    
    elo_ratings[each_row['AwayTeam']] = away_new_elo
 
    df.at[index, 'home_elo_end'] = home_new_elo
    df.at[index, 'away_elo_end'] = away_new_elo

#save the dataframe to a csv file
df.to_csv('data/elo_ratings.csv', index=False)
      
#sort the elo ratings in descending order
sorted_elo_ratings = dict(sorted(elo_ratings.items(), key=lambda item: item[1], reverse=True))


#convert the dictionary to a dataframe
elo_ratings_df = pd.DataFrame(list(sorted_elo_ratings.items()),columns = ['Team','Elo_Rating'])
    #Calculate Away Team Elo Rating after each game 

# # merge two dictionaries
# elo_ratings_with_original = {**elo_ratings, **sorted_elo_ratings}

# #convert 

print(elo_ratings_df)



def compute_probability(elo_A, elo_B):
    """
    Compute the probability of team A winning based on their Elo ratings.

    Parameters:
    elo_A (float): Elo rating of team A.
    elo_B (float): Elo rating of team B.

    Returns:
    float: Probability of team A winning.
    """
    return 1 / (1 + 10 ** ((elo_B - elo_A) / 400))

# Compute probability of team A winning
probability_team_A = compute_probability(sorted_elo_ratings.get('SFS'), sorted_elo_ratings.get('DES'))
# Probability of team B winning is 1 - probability_team_A
probability_team_B = 1 - probability_team_A

# Print probabilities
print("Probability of Team A winning:", probability_team_A)
print("Probability of Team B winning:", probability_team_B)

 

