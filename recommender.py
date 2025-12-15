import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommender(name):
    recommended_movies = []

    df = pd.read_csv('movies.csv')

    selected_features = ['genres','keywords','tagline','cast','director']
    
    for feature in selected_features:
        df[feature] = df[feature].fillna('')

    combined_features = df['genres']+' '+df['keywords']+' '+df['tagline']+' '+df['cast']+' '+df['director']

    vectorizer = TfidfVectorizer()

    feature_vectors = vectorizer.fit_transform(combined_features)

    similarity = cosine_similarity(feature_vectors)

    list_of_all_titles = df['title'].tolist()

    find_close_match = difflib.get_close_matches(name,list_of_all_titles)

    close_match = find_close_match[0]

    index_of_movie = df[df.title == close_match].index[0]

    similarity_scores = list(enumerate(similarity[index_of_movie]))

    sorted_similar_movies = sorted(similarity_scores, key = lambda x:x[1], reverse = True)

    for i in sorted_similar_movies[1:11]:
        movie_index = i[0]
        recommended_movies.append(df['title'][movie_index])
    
    return recommended_movies
