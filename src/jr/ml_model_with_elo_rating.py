#load the dataset

    
#add elo ratings to the dataset using the function from the previous calculation
#add two new columns to the dataframe


#define outcome function and store it in a new column
#handle "draw" in a way that makes sense for the model


# Setup y and X
# X - drop columns that are not needed for the model like game_ordered_id, outcome and upto the 5th column


# Normalize the data using StandardScaler - why do we need to normalize the data?
#ignore this for now and see if it is necessary

# Split the dataset for training and testing using train_test_split in sklearn.model_selection


# Train the xgboost model as classifier (do we need to model as a classifier or a regressor?)


# Hyperparameter tuning


# Predict the outcome of the regular round games with the trained model


# Print the accuracy of the model

# Save the model to a file as a pickle object to be used later

# Print the features that are important for the model and save it to a file for future reference in a file called important_features.csv

# Print the time taken to train the model









