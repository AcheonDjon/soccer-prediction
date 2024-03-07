import pandas as pd


def load_csv_dataset(file_path):
    """
    Load a CSV data set from a file using pandas
    :param file_path: The path to the CSV file
    :return: A pandas DataFrame representing the data set
    """
    dataset = pd.read_csv(file_path, delimiter= ",",header=0)
    return dataset


# Load the dataset
file_path = './data/elo_ratings.csv'
dataset = load_csv_dataset(file_path)


# Determine how many times home team Elo start score is greater than away start score
count = len(dataset[dataset['home_elo_start'] >= dataset['away_elo_start']])
        
#out of which how many times the home team won
home_win = len(dataset[(dataset['home_elo_start'] >= dataset['away_elo_start']) & (dataset['HomeScore'] >= dataset['AwayScore'])])
print(home_win/count)