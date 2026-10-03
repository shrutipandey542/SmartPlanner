import pandas as pd

# Load dataset
df = pd.read_csv("Dataset/event_management.csv")

# Display first 5 records
print("First 5 Records:")
print(df.head())

# Display number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Dataset information
print("\nDataset Information:")
print(df.info())