import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# ==========================================
# 1. Load Dataset
# ==========================================

df = pd.read_csv("Dataset/event_management.csv")

print("Dataset Loaded Successfully!")
print("Original Shape:", df.shape)


# ==========================================
# 2. Convert Event_Date
# ==========================================

df["Event_Date"] = pd.to_datetime(df["Event_Date"])

df["Event_Year"] = df["Event_Date"].dt.year
df["Event_Month"] = df["Event_Date"].dt.month
df["Event_Day"] = df["Event_Date"].dt.day


# Remove unnecessary columns
df = df.drop("Event_Date", axis=1)
df = df.drop("Event_ID", axis=1)


# ==========================================
# 3. Encode Categorical Columns
# ==========================================

categorical_columns = [
    "Event_Type",
    "Venue",
    "Status",
    "Organizer"
]

encoders = {}

for column in categorical_columns:

    encoder = LabelEncoder()

    df[column] = encoder.fit_transform(df[column])

    encoders[column] = encoder


# ==========================================
# 4. Separate Features and Target
# ==========================================

X = df.drop("Budget_USD", axis=1)

y = df["Budget_USD"]


print("\nFeatures:")
print(X.columns)

print("\nTarget:")
print("Budget_USD")


# ==========================================
# 5. Train-Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


print("\nTraining Records:", len(X_train))
print("Testing Records:", len(X_test))


# ==========================================
# 6. Create Random Forest Model
# ==========================================

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# ==========================================
# 7. Train Model
# ==========================================

print("\nTraining Model...")

model.fit(X_train, y_train)

print("Model Training Completed!")


# ==========================================
# 8. Prediction
# ==========================================

y_pred = model.predict(X_test)


# ==========================================
# 9. Model Evaluation
# ==========================================

mae = mean_absolute_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print("Mean Absolute Error:", mae)
print("R2 Score:", r2)


# ==========================================
# 10. Save Model
# ==========================================

joblib.dump(model, "event_budget_model.pkl")

print("\nModel saved as event_budget_model.pkl")


# ==========================================
# 11. Save Encoders
# ==========================================

joblib.dump(encoders, "event_encoders.pkl")

print("Encoders saved as event_encoders.pkl")

print("\nTraining Completed Successfully!")