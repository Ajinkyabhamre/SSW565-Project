import pandas as pd

# Load the clustered code reviews
clustered_data = pd.read_csv('clustered_code_reviews.csv')
print("Clustered Code Reviews:")
print(clustered_data.head())
print("\nCluster Distribution:")
print(clustered_data['cluster'].value_counts())

# Load the cluster centroids
centroids_data = pd.read_csv('cluster_centroids.csv')
print("\nCluster Centroids:")
print(centroids_data.head())
