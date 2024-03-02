import pandas as pd


regularteamsdata = pd.read_csv('./data/NSL_regular_season_data.csv')

# home_rating1 = 1500
# away_rating2 = 1500

def outcome(row):
    if row['HomeScore'] > row['AwayScore']:
        return 1
    elif row['HomeScore'] == row['AwayScore']:
        if row['Home_xG'] > row['Away_xG']:
            return 1
        else:
            return 0 
        
    else:
        return 0

def ELORATING(team1_rating, team2_rating, team1_result, k_factor=32):
    
      expected_result_team1 = 1 / (1 + 10 ** ((team2_rating - team1_rating) / 400))

    # Calculate the new Elo rating for team 1
      new_rating_team1 = team1_rating + k_factor * (team1_result - expected_result_team1)

    # Since the sum of the team's ratings should remain constant, the change in team 1's rating should be
    # subtracted from team 2's rating.
      new_rating_team2 = team2_rating + k_factor * ((1 - team1_result) - (1 - expected_result_team1))

      return new_rating_team1, new_rating_team2

# print(ELORATING(home_rating1, away_rating2, 0))


#iterate through regularteamsdata

#start elo dictionary {'team' : 'latest elo rating' } 
#call it elo_dictionary
elo_dict = {}

#for each game, the start and away elo rating is computed before and after the game adf dj
for row_index, row_data in regularteamsdata.iterrows():
    
    # creating a new column called home elo that contains the values of a starting home team elo rating
    
    #if it's not in the elo rating dictionary it will return 1500


    home_elo_start = elo_dict.get(row_data['HomeTeam'],1500)
    away_elo_start = elo_dict.get(row_data['AwayTeam'],1500)


    #updating the original dataframe at the nth row with the variables defined aboved
    regularteamsdata.at[row_index,'home_elo_start'] = home_elo_start
    regularteamsdata.at[row_index,'away_elo_start'] = away_elo_start
    
     #get outcome of for each game 
    out_come = outcome(row_data)

     #get new elo rating based on outcome 
    new_home_rating, new_away_rating = ELORATING(home_elo_start,away_elo_start, out_come) 
     #A->B with B winning, rating = 1486 and 1516
    
     #add or update new team ratings
    regularteamsdata.at[row_index,'home_elo_end'] = new_home_rating
    regularteamsdata.at[row_index,'away_elo_end'] = new_away_rating

     #update elo dictionary with the latest rating for home and away team 
    elo_dict[row_data['HomeTeam']] = new_home_rating

    elo_dict[row_data['AwayTeam']] = new_away_rating 


#drop the index
regularteamsdata.reset_index(drop=True,inplace=True)

#finally save the dataframe to a new file 

regularteamsdata.to_csv('./data/NSL_regular_season_final_model_input.csv',index=False)

elo_final_ratings_df= pd.DataFrame(elo_dict, index=[0])

print(regularteamsdata)

elo_final_ratings_df.to_csv('./data/NSL_regular_season_final_elo_ratings.csv')