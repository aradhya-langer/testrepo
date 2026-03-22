import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore
from sklearn.linear_model import LogisticRegression # type: ignore

def train_model(df):

    X = df["Description"]
    y = df["Category"]

    vec = TfidfVectorizer()
    Xv = vec.fit_transform(X)

    model = LogisticRegression()
    model.fit(Xv, y)

    return model, vec
