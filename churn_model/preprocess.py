import pandas as pd

def preprocess_input(data):
    """
    Converts raw input data into the required DataFrame for prediction.
    """
    df = pd.DataFrame([data])

    # Ensure proper types
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["gender"] = df["gender"].map({"Female": 0, "Male": 1})
    df["SeniorCitizen"] = df["SeniorCitizen"].apply(lambda x: 1 if x in [1, "1", "Yes", "yes", True] else 0)

    return df[["gender", "SeniorCitizen", "MonthlyCharges", "TotalCharges"]]
