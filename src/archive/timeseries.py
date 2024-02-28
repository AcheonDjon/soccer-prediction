import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error
import xgboost as xgb

# Generate time series dataset
start_date = '2023-09-01'
end_date = '2024-01-01'
dates = pd.date_range(start=start_date, end=end_date, freq='W-SAT')
data = pd.DataFrame( {'Date': dates, 'y': np.random.randint(1, 100, len(dates))} )

# Create a feature for peak season in late November and early December
data['Peak_Season'] = 0
data.loc[(data['Date'].dt.month == 11) & (data['Date'].dt.day >= 20), 'Peak_Season'] = 1
data.loc[(data['Date'].dt.month == 12) & (data['Date'].dt.day <= 10), 'Peak_Season'] = 1

# Assuming you have additional features 'X' and target variable 'y'

# Create lag features if needed
data['Lag_1'] = data['y'].shift(1)

# Split data into training and testing sets
train_size = int(len(data) * 0.8)
train_data, test_data = data.iloc[:train_size], data.iloc[train_size:]

# Define X and y
X_train, y_train = train_data.drop(['Date', 'y'], axis=1), train_data['y']
X_test, y_test = test_data.drop(['Date', 'y'], axis=1), test_data['y']

# Train XGBoost model without lag
model_no_lag = xgb.XGBRegressor()
model_no_lag.fit(X_train, y_train)

# Predict for 20 periods without lag
forecast_no_lag = model_no_lag.predict(X_test)

# Train XGBoost model with lag
model_with_lag = xgb.XGBRegressor()
model_with_lag.fit(X_train.drop('Peak_Season', axis=1), y_train)

# Create lagged test data
X_test_with_lag = X_test.copy()
X_test_with_lag['Lag_1'] = test_data['y'].shift(1)

# Predict for 20 periods with lag
forecast_with_lag = model_with_lag.predict(X_test_with_lag.drop('Peak_Season', axis=1))

# Calculate MAPE over peak periods
peak_periods_no_lag = y_test[X_test['Peak_Season'] == 1]
peak_periods_with_lag = y_test[X_test['Peak_Season'] == 1]

mape_no_lag = mean_absolute_percentage_error(peak_periods_no_lag, forecast_no_lag[X_test['Peak_Season'] == 1])
mape_with_lag = mean_absolute_percentage_error(peak_periods_with_lag, forecast_with_lag[X_test['Peak_Season'] == 1])

print("MAPE without lag:", mape_no_lag)
print("MAPE with lag:", mape_with_lag)