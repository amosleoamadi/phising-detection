import pandas as pd
import joblib
import re
import nltk
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, recall_score, precision_score, f1_score
from imblearn.over_sampling import SMOTE   # <-- NEW

# Download nltk data (run once)
nltk.download('punkt_tab')
nltk.download('stopwords')

# Load dataset
data = pd.read_csv("dataset/spam.csv", encoding="latin1")

# Keep only useful columns
data = data[["v1", "v2"]]

# Rename columns
data.columns = ["label", "message"]

# Stopwords
stop_words = set(stopwords.words("english"))

# Text cleaning function (keeps URLs)
def cleaning_data(text):
    text = text.lower()
    # Extract URLs as special tokens
    urls = re.findall(r'https?://\S+|www\.\S+', text)
    for i, url in enumerate(urls):
        text = text.replace(url, f" URL_TOKEN_{i} ")
    # Remove mentions
    text = re.sub(r'@\S+', '', text)
    # Remove punctuation but keep URL placeholders
    text = "".join(ch for ch in text if ch not in string.punctuation or ch in '._')
    # Tokenize
    words = nltk.word_tokenize(text)
    # Keep URL placeholders, remove stopwords
    words = [w for w in words if w not in stop_words or w.startswith('URL_TOKEN_')]
    return " ".join(words)

# Apply cleaning
data["clean_message"] = data["message"].apply(cleaning_data)

# Extract cleaned messages and labels
messages = data["clean_message"]
labels = data["label"]

# Convert text into numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(messages)
y = labels

# Split dataset (keep test set imbalanced for realistic evaluation)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y   # stratify preserves class ratio
)

# ---- SMOTE: balance only the training set ----
# Find minority class name automatically
minority_class = y_train.value_counts().idxmin()

smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Train model on balanced data
model = LogisticRegression(class_weight="balanced", max_iter=1000)   # max_iter increased
model.fit(X_train_resampled, y_train_resampled)

# Predict on original test set (imbalanced)
predictions = model.predict(X_test)

# Explicit metrics for the scam/spam class
recall = recall_score(y_test, predictions, pos_label=minority_class)
precision = precision_score(y_test, predictions, pos_label=minority_class)
f1 = f1_score(y_test, predictions, pos_label=minority_class)

accuracy = model.score(X_test, y_test)

# Save model and vectorizer
joblib.dump(model, "models/model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("\nModel and vectorizer saved successfully!")