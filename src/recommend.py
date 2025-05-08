import pickle
from sklearn.metrics.pairwise import cosine_similarity

MODEL_PATH = 'model.pkl'

def load_model(model_path=MODEL_PATH):
    with open(model_path, 'rb') as f:
        data, tfidf, tfidf_matrix = pickle.load(f)
    return data, tfidf, tfidf_matrix

def get_recommendations(title, data, tfidf_matrix, top_n=10):
    if title not in data['primaryTitle'].values:
        return []

    idx = data[data['primaryTitle'] == title].index[0]
    cosine_sim = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()

    # Get top_n+1 because first result is the same movie
    similar_indices = cosine_sim.argsort()[-(top_n+1):][::-1]
    recommended_indices = [i for i in similar_indices if i != idx][:top_n]

    return data.iloc[recommended_indices][['primaryTitle', 'averageRating']]