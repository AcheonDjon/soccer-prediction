import pandas as pd
df = pd.DataFrame({
    'A': [2, 1, 2, 3, 3, 5, 4],
    'B': [1, 2, 3, 5, 4, 2, 5],
    'C': [5, 8, 9, 4, 2, 3, 6]
}, index=[2, 3, 1, 5, 4, 0, 6])

# Sort df by its index
df.sort_index(inplace=True)
print(df)
