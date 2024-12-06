import pandas as pd
from sklearn.cluster import KMeans
import pickle

# Load preprocessed data
with open('reduced_matrix.pkl', 'rb') as f:
    reduced_matrix = pickle.load(f)

# Perform K-Means clustering for k = 8
print("Clustering data using K-Means with k = 8...")
kmeans = KMeans(n_clusters=8, random_state=42)
labels = kmeans.fit_predict(reduced_matrix)

# Save the cluster labels
clustered_data = pd.DataFrame({
    'cleaned_text': pd.read_csv('cleaned_code_reviews.csv')['cleaned_text'],
    'cluster': labels
})

# Save clustered data to CSV
clustered_data.to_csv('clustered_code_reviews.csv', index=False)
print("Clustered data saved as 'clustered_code_reviews.csv'.")

# Save the KMeans model for later use
with open('kmeans_model.pkl', 'wb') as f:
    pickle.dump(kmeans, f)
print("KMeans model saved as 'kmeans_model.pkl'.")
