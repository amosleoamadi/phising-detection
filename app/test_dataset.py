import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load dataset
data = pd.read_csv("dataset/spam.csv", encoding="latin1")

# Extract messages and labels
messages = data["v2"]
labels = data["v1"]

# Convert text into numbers
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(messages)
y = labels

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create ML model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(classification_report(y_test, predictions))

accuracy = model.score(X_test, y_test)

print("Accuracy:", accuracy)

# Save model
joblib.dump(model, "models/model.pkl")

# Save vectorizer
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("Model and vectorizer saved successfully!")
print(data.head())