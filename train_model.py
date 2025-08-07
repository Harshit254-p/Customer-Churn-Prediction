import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load data
df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Clean data
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df.dropna(subset=["TotalCharges"], inplace=True)

# Encode features
df["Churn"] = df["Churn"].map({"No": 0, "Yes": 1})
df["gender"] = df["gender"].map({"Female": 0, "Male": 1})
df["SeniorCitizen"] = df["SeniorCitizen"].apply(lambda x: 1 if x == 1 else 0)

# Select features
features = ["gender", "SeniorCitizen", "MonthlyCharges", "TotalCharges"]
X = df[features]
y = df["Churn"]

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "churn_model/model.pkl")
print("✅ Model saved to churn_model/model.pkl")
