from sklearn.preprocessing import StandardScaler

# Example features (not normalized)
features = [
    [10, 20, 30],
    [15, 25, 35],
    [20, 30, 40]
]

# Initialize StandardScaler
scaler = StandardScaler()

# Fit scaler to the data and transform the features
normalized_features = scaler.fit_transform(features)

# Print normalized features
print("Normalized Features:")
print(normalized_features)
