import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def load_and_prepare_data(basics_path, ratings_path):
    basics = pd.read_csv(basics_path, sep='\t', dtype=str, na_values='\\N', compression='gzip')
    ratings = pd.read_csv(ratings_path, sep='\t', dtype=str, na_values='\\N', compression='gzip')

    basics = basics[basics['titleType'] == 'movie']
    animation = basics[basics['genres'].fillna('').str.contains('Animation', case=False)]

    merged = pd.merge(animation, ratings, on='tconst', how='left')
    merged = merged[['tconst', 'primaryTitle', 'genres', 'averageRating']].dropna()
    return merged.reset_index(drop=True)

def train_model(data):
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(data['genres'].fillna(''))
    return tfidf, tfidf_matrix

def save_model(data, tfidf, tfidf_matrix, model_path='model.pkl'):
    with open(model_path, 'wb') as f:
        pickle.dump((data, tfidf, tfidf_matrix), f)
