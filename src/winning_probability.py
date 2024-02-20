# import math

# def expected_result(team_a_rating, team_b_rating):
#     """
#     Calculate the expected outcome of a match between two teams based on their Elo ratings.
#     """
#     return 1 / (1 + math.pow(10, (team_b_rating - team_a_rating) / 400))

# # Example usage:
# team_a_rating = 1500
# team_b_rating = 1600

# winning_prob_a = expected_result(team_a_rating, team_b_rating)
# winning_prob_b = 1 - winning_prob_a

# print("Winning probability for Team A:", winning_prob_a)
# print("Winning probability for Team B:", winning_prob_b)

import math

def expected_result2(team_a_rating, team_b_rating, home_advantage=100):
    """
    Calculate the expected outcome of a match between two teams based on their Elo ratings and home advantage.
    """
    return 1 / (1 + math.pow(10, ((team_b_rating ) - (team_a_rating + home_advantage)) / 400))

# Example usage:
team_a_rating = 1500
team_b_rating = 1600
home_advantage = 100  # Adjust as needed

winning_prob_a = expected_result2(team_a_rating, team_b_rating, home_advantage)
winning_prob_b = 1 - winning_prob_a

print("Winning probability for Team A (playing at home):", winning_prob_a)
print("Winning probability for Team B (playing away):", winning_prob_b)

