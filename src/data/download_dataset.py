import os
import pandas as pd
import requests

DATA_URL = "https://raw.githubusercontent.com/Himanshu-1703/reddit-sentiment-analysis/main/data/reddit.csv"
SAVE_PATH = "../../data/raw/reddit.csv"

os.makedirs("../../data/raw", exist_ok=True)

def download_csv(url, save_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(save_path, "wb") as f:
        f.write(response.content)

def show_stats(csv_path):
    df = pd.read_csv(csv_path)
    print("Nombre de commentaires :", len(df))
    print("Distribution des labels :\n", df["category"].value_counts())
    return df

if __name__ == "__main__":
    download_csv(DATA_URL, SAVE_PATH)
    show_stats(SAVE_PATH)
