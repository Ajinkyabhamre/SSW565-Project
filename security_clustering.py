import pickle
from sklearn.cluster import KMeans
import pandas as pd

# Load the reduced matrix
with open('security_reduced_matrix.pkl', 'rb') as f:
    reduced_matrix = pickle.load(f)

# Apply K-Means clustering
print("Clustering data using K-Means...")
kmeans = KMeans(n_clusters=8, random_state=42)  # 8 clusters
cluster_labels = kmeans.fit_predict(reduced_matrix)

# Save the model
with open('security_kmeans_model.pkl', 'wb') as f:
    pickle.dump(kmeans, f)

# Load the original data for labeling
data = pd.read_csv("cleaned_security_reviews.csv")
data['cluster'] = cluster_labels

# Save the clustered data
data.to_csv("security_clustered_reviews.csv", index=False)
print("Clustered data saved as 'security_clustered_reviews.csv'.")
