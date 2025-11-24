import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

# Paths (adjust as needed for your folder setup)
TRAIN_PATH = "../../data/processed/train.csv"
TEST_PATH = "../../data/processed/test.csv"
MODEL_DIR = "../../models/"
VECTORIZER_PATH = os.path.join(MODEL_DIR, "tfidf_vectorizer.joblib")
MODEL_PATH = os.path.join(MODEL_DIR, "logreg_model.joblib")

os.makedirs(MODEL_DIR, exist_ok=True)

def load_data():
    train = pd.read_csv(TRAIN_PATH)
    test = pd.read_csv(TEST_PATH)
    return train, test

def vectorize(train_texts, test_texts):
    vectorizer = TfidfVectorizer(max_features=10000)
    X_train = vectorizer.fit_transform(train_texts)
    X_test = vectorizer.transform(test_texts)
    return X_train, X_test, vectorizer

def train_and_evaluate(X_train, y_train, X_test, y_test):
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Classification Report:\n", classification_report(y_test, y_pred))
    print("Accuracy:", accuracy_score(y_test, y_pred))
    return model

if __name__ == "__main__":
    # 1. Load data
    train_df, test_df = load_data()

    # 2. DROP rows with missing clean_comment before splitting
    before_train = len(train_df)
    before_test = len(test_df)
    train_df = train_df.dropna(subset=['clean_comment'])
    test_df = test_df.dropna(subset=['clean_comment'])
    after_train = len(train_df)
    after_test = len(test_df)
    print(f"Dropped {before_train - after_train} missing comments from TRAIN set.")
    print(f"Dropped {before_test - after_test} missing comments from TEST set.")

    # 3. Prepare features and labels
    X_train_texts = train_df["clean_comment"]
    y_train = train_df["category"]
    X_test_texts = test_df["clean_comment"]
    y_test = test_df["category"]

    # Optional: Double-check there are no NaNs left
    print("Missing in train:", X_train_texts.isnull().sum())
    print("Missing in test :", X_test_texts.isnull().sum())

    # 4. Vectorize text
    X_train, X_test, vectorizer = vectorize(X_train_texts, X_test_texts)

    # 5. Train and evaluate model
    model = train_and_evaluate(X_train, y_train, X_test, y_test)

    # 6. Save model and vectorizer
    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)
    print("Model and vectorizer saved to 'models/' directory.")
