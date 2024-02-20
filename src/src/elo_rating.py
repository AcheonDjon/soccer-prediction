import numpy as np

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

def calculate_expected_outcome(features_A, features_B, elo_A, elo_B, coefficients):
    """
    Calculate the expected outcome of a match using logistic regression.

    Parameters:
    features_A (ndarray): Features of team A.
    features_B (ndarray): Features of team B.
    elo_A (float): Elo rating of team A.
    elo_B (float): Elo rating of team B.
    coefficients (ndarray): Coefficients for the logistic regression model.

    Returns:
    float: Expected outcome of the match.
    """
    z = np.dot(coefficients, np.concatenate(([1], features_A - features_B, [elo_B - elo_A])))
    return 1 / (1 + np.exp(-z))

def update_elo_ratings(actual_outcome, elo_A, elo_B, expected_outcome, k):
    """
    Update the Elo ratings of two teams after a match.

    Parameters:
    actual_outcome (int): Actual outcome of the match (1 for team A win, 0 for team B win).
    elo_A (float): Elo rating of team A.
    elo_B (float): Elo rating of team B.
    expected_outcome (float): Expected outcome of the match.
    k (int): K-factor for Elo ratings.

    Returns:
    tuple: Updated Elo ratings of team A and team B.
    """
    elo_A_new = elo_A + k * (actual_outcome - expected_outcome)
    elo_B_new = elo_B + k * (expected_outcome - actual_outcome)
    return elo_A_new, elo_B_new

# Example features for two teams (normalized)
features_team_A = np.array([0.2, 0.5, 0.8, 0.3, 0.6, 0.7, 0.4, 0.9, 0.1, 0.6])
features_team_B = np.array([0.3, 0.6, 0.7, 0.4, 0.9, 0.2, 0.8, 0.5, 0.6, 0.3])

# Initial Elo ratings
elo_team_A = 1500
elo_team_B = 1500

# Coefficients for logistic regression model
coefficients = np.random.rand(12)  # Assuming you have 10 features and 2 additional for Elo ratings

# Constants
k = 32  # K-factor for Elo ratings
actual_outcome = 1  # 1 for Team A win, 0 for Team B win

# Calculate expected outcome
expected_outcome = calculate_expected_outcome(features_team_A, features_team_B, elo_team_A, elo_team_B, coefficients)

# Update Elo ratings
elo_team_A_new, elo_team_B_new = update_elo_ratings(actual_outcome, elo_team_A, elo_team_B, expected_outcome, k)

# Print updated Elo ratings
print("Updated Elo ratings:")
print("Team A:", elo_team_A_new)
print("Team B:", elo_team_B_new)

# # Example Elo ratings for two teams
# elo_team_A = 1500
# elo_team_B = 1600

# Compute probability of team A winning
probability_team_A = compute_probability(elo_team_A_new, elo_team_B_new)
# Probability of team B winning is 1 - probability_team_A
probability_team_B = 1 - probability_team_A

# Print probabilities
print("Probability of Team A winning:", probability_team_A)
print("Probability of Team B winning:", probability_team_B)
