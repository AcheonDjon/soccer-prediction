def win_probability(elo_a, elo_b):
    """
    Calculate the probability of Team A winning based on Elo ratings of Team A and Team B.

    Parameters:
        elo_a (float): Elo rating of Team A.
        elo_b (float): Elo rating of Team B.

    Returns:
        float: Probability of Team A winning.
    """
    return 1 / (1 + 10 ** ((elo_b - elo_a) / 400))

# Example Elo ratings
elo_team_a = 1500
elo_team_b = 1500

# Calculate win probability
probability_team_a_wins = win_probability(elo_team_a, elo_team_b)
print("Probability of Team A winning:", probability_team_a_wins)
print("Probability of Team B winning:", 1 - probability_team_a_wins)