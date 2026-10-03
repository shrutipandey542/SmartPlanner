import pandas as pd

# Load dataset
df = pd.read_csv("Dataset/event_management.csv")

print("Original Dataset:")
print(df.head())

# Convert Event_Date to datetime
df["Event_Date"] = pd.to_datetime(df["Event_Date"])

# Extract useful date information
df["Event_Year"] = df["Event_Date"].dt.year
df["Event_Month"] = df["Event_Date"].dt.month
df["Event_Day"] = df["Event_Date"].dt.day

# Remove original date column
df = df.drop("Event_Date", axis=1)

# Remove Event_ID
df = df.drop("Event_ID", axis=1)

print("\nAfter Data Preparation:")
print(df.head())

print("\nNew Dataset Information:")
print(df.info())