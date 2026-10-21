import pandas as pd
import os
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# ==============================
# LOAD DATASET
# ==============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(
    BASE_DIR,
    "..",
    "..",
    "cve_training_data.csv"
)

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully!")
print(df.head())
print("\nColumns:")
print(df.columns)


# ==============================
# PREPARE DATA
# ==============================

X = df[["CVSS_Score"]]
y = df["Severity"]


# ==============================
# TRAIN TEST SPLIT
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==============================
# RANDOM FOREST MODEL
# ==============================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# ==============================
# TEST MODEL
# ==============================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel trained successfully!")
print("Accuracy:", accuracy)


# ==============================
# SAVE MODEL
# ==============================

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "severity_model.pkl"
)

joblib.dump(model, MODEL_PATH)

print("\nModel saved successfully!")
print("Location:", MODEL_PATH)