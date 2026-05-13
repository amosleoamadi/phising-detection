import pandas as pd
from utils.url_features import extract_url_features
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

data = pd.read_csv("dataset/Dataset.csv")

urls = data["url"]
labels = data["label"]

features = [extract_url_features(url) for url in urls]
vectorizer = DictVectorizer(sparse=False)

X = vectorizer.fit_transform(features)

y = labels

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression()

model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print("Accuracy:", accuracy)

joblib.dump(model, "models/model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print(data.head())
print(data.columns)
print(labels)