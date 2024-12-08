import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from collections import Counter

# Load the clustered data
data = pd.read_csv("security_clustered_reviews.csv")

# Load the TF-IDF vectorizer
with open('security_tfidf_vectorizer.pkl', 'rb') as f:
    tfidf_vectorizer = pickle.load(f)

# Analyze each cluster
clusters = data['cluster'].unique()
for cluster in clusters:
    print(f"\nCluster {cluster}:")
    
    # Filter reviews for the cluster
    cluster_data = data[data['cluster'] == cluster]
    
    # Vectorize the text for this cluster
    tfidf_matrix = tfidf_vectorizer.transform(cluster_data['cleaned_description'])
    feature_names = tfidf_vectorizer.get_feature_names_out()
    
    # Get top terms
    term_scores = tfidf_matrix.sum(axis=0).A1
    top_terms = [feature_names[i] for i in term_scores.argsort()[-10:][::-1]]
    print(f"Top Terms: {', '.join(top_terms)}")
    
    # Show sample reviews
    sample_reviews = cluster_data['cleaned_description'].sample(3, random_state=42)
    for review in sample_reviews:
        print(f" - {review}")
