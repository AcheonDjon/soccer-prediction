import pandas as pd
import pickle

df = pd.read_csv('./data/regular_season_data.csv',delimiter=',',header=0)

def game_home_attribute(team_name):
    d2 = df[df['HomeTeam'] == team_name]
    d3 = d2[['Home_xG','Home_shots','Home_corner','Home_PK_Goal','Home_PK_shots','Home_ToP']].mean()

    return d3.to_frame().T

    # Rest of the code...

def game_away_attribute(team_name): 
    d2 = df[df['AwayTeam'] == team_name]
    d3 = d2[['Away_xG','Away_shots','Away_corner','Away_PK_Goal','Away_PK_shots']].mean()
    return d3.to_frame().T

def merge_home_away(home_team_name,away_team_name):
    home = game_home_attribute(home_team_name)
    away = game_away_attribute(away_team_name)
    home.columns = ['Home_xG','Home_shots','Home_corner','Home_PK_Goal','Home_PK_shots','Home_ToP']
    away.columns = ['Away_xG','Away_shots','Away_corner','Away_PK_Goal','Away_PK_shots']


    return pd.concat([home,away],axis=1)

def home_team_analysis(home_team_name, away_team_name):
     
    hta = merge_home_away(home_team_name,away_team_name)
    
    hta['home_elo_start'] = 1250
    hta['away_elo_start'] = 1500
    hta['home_elo_end'] = 600
    hta['away_elo_end'] = 600

    hta = hta[['Home_xG', 'Away_xG', 'Home_shots', 'Away_shots', 'Home_corner', 'Away_corner', 'Home_PK_Goal', 'Away_PK_Goal', 'Home_PK_shots', 'Away_PK_shots', 'Home_ToP', 'home_elo_start', 'away_elo_start', 'home_elo_end', 'away_elo_end']]

    return hta

#print(game_home_attribute('ANC'))


#load soccer model to predict the outcome of the game
with open('grid_search_results.pkl', 'rb') as file:
    model = pickle.load(file)

group_round = pd.read_csv('./data/NSL_Group_Round_Games.csv',delimiter=',',header=0)  

for index, row in group_round.iterrows():
    home_team = row['HomeTeam']
    away_team = row['AwayTeam']
    print(f"home_team = {home_team}, away_team = {away_team}")
    team_a = game_home_attribute(home_team)
    team_b = game_away_attribute(away_team)

    hta = home_team_analysis(home_team,away_team)
    
    predict = model.predict(hta)
    
    print(f"predition = {model.predict_proba(hta)}")
