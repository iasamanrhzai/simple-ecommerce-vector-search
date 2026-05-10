import re
import pandas as pd


def clean_text(text):

    text = str(text)

    text = re.sub(r"<.*?>", "", text)

    text = text.replace("\n", " ")

    return text.strip()


def load_dataset(path):

    df = pd.read_csv(path)

    df = df.fillna("")

    df = df.drop_duplicates(
        subset=["Uniq Id"]
    )

    return df
