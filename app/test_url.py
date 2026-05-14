# train_url_model.py
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from app.utils.url_features import extract_url_features

# Load your dataset
df = pd.read_csv("dataset/url_dataset.csv")  # has columns: URL, features..., Results

# Extract features and labels using your OWN extractor
print("Extracting features from URLs... (this may take a moment)")
features_list = []
for url in df['URL']:
    features_list.append(extract_url_features(url))

# Use DictVectorizer to convert dicts to matrix
vectorizer = DictVectorizer(sparse=False)
X = vectorizer.fit_transform(features_list)
y = df['Results'].values

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train with class balancing
model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
model.fit(X_train, y_train)

# Evaluate
print("\nClassification Report:\n", classification_report(y_test, model.predict(X_test)))

# Save model and vectorizer
joblib.dump(model, "models/url_model.pkl")
joblib.dump(vectorizer, "models/url_vectorizer.pkl")

print("\nModel and vectorizer saved successfully!")