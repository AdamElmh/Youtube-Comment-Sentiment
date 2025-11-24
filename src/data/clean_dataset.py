import pandas as pd
import re

RAW_PATH = "../../data/raw/reddit.csv"
CLEAN_PATH = "../../data/processed/reddit_clean.csv"

def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    text = text.lower()
    return text.strip()

def clean_dataset(raw_path, save_path):
    df = pd.read_csv(raw_path)
    df["clean_comment"] = df["clean_comment"].astype(str).apply(clean_text)
    df.to_csv(save_path, index=False)
    print("Exemple nettoyé :", df["clean_comment"].iloc[0][:100])

if __name__ == "__main__":
    clean_dataset(RAW_PATH, CLEAN_PATH)
