import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Load data
clustered_data = pd.read_csv("clustered_code_reviews.csv")
centroids = pd.read_csv("cluster_centroids.csv", header=None)

# Extract cleaned text and cluster assignments
cleaned_texts = clustered_data['cleaned_text']
clusters = clustered_data['cluster']

# Vectorize text using TF-IDF
tfidf_vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(cleaned_texts)

# Get feature names (terms)
feature_names = tfidf_vectorizer.get_feature_names_out()

# Analyze clusters
for cluster_id in range(centroids.shape[0]):
    print(f"\nCluster {cluster_id}:")
    cluster_data = clustered_data[clustered_data['cluster'] == cluster_id]
    
    if cluster_data.empty:
        print(" - No data points in this cluster.")
        continue  # Skip empty clusters
    
    # Find the top terms for the cluster centroid
    cluster_centroid = centroids.iloc[cluster_id]
    top_terms_idx = np.argsort(-cluster_centroid.values)[:10]  # Top 10 terms
    top_terms = [feature_names[i] for i in top_terms_idx]
    print(f"Top Terms: {', '.join(top_terms)}")
    
    # Sample a few data points from the cluster
    print("Sample Reviews:")
    sample_data = cluster_data['cleaned_text'].sample(min(3, len(cluster_data)), random_state=42)
    for review in sample_data:
        print(f" - {review[:100]}...")  # Print first 100 characters of each review
