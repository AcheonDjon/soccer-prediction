# dataset.rename(columns={'away_score': 'AwayScore'}, inplace=True)

# home_wins = dataset[dataset['HomeScore'] > dataset['AwayScore']]
# away_wins = dataset[dataset['HomeScore'] < dataset['AwayScore']]
# draws = dataset[dataset['HomeScore'] == dataset['AwayScore']]

# home_wins_count = len(home_wins)
# away_wins_count = len(away_wins)
# draws_count = len(draws)

# print(f"Home team wins: {home_wins_count}")
# print(f"Away team wins: {away_wins_count}")
# print(f"Draws: {draws_count}")
# print(home_wins_count+away_wins_count+draws_count)

# # Calculate the number of home team wins where the expected goals (xG) for the home team is greater than the expected goals for the away team

# home_xg_wins = dataset[(dataset['Home_xG'] > dataset['Away_xG']) & (dataset['HomeScore'] >= dataset['AwayScore'])]
# home_xg_wins_count = len(home_xg_wins)

# home_xg_wins_probability = home_xg_wins_count / len(dataset)
