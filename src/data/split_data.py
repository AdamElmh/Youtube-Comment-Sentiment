import pandas as pd
from sklearn.model_selection import train_test_split

CLEAN_PATH = "../../data/processed/reddit_clean.csv"
TRAIN_PATH = "../../data/processed/train.csv"
TEST_PATH = "../../data/processed/test.csv"

def split(csv_path, train_path, test_path, test_size=0.2, random_state=42):
    df = pd.read_csv(csv_path)
    train, test = train_test_split(df, test_size=test_size, stratify=df["category"], random_state=random_state)
    train.to_csv(train_path, index=False)
    test.to_csv(test_path, index=False)
    print("Taille jeu train :", len(train))
    print("Taille jeu test :", len(test))

if __name__ == "__main__":
    split(CLEAN_PATH, TRAIN_PATH, TEST_PATH)
