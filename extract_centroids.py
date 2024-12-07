import pickle
import pandas as pd

# Load the KMeans model and clustered data
model_file = "kmeans_model.pkl"
with open(model_file, 'rb') as file:
    kmeans = pickle.load(file)

# Load the original cleaned dataset
cleaned_file = "clustered_code_reviews.csv"
data = pd.read_csv(cleaned_file)

# Get cluster centroids
centroids = kmeans.cluster_centers_

# Save centroids to CSV for easier inspection
centroids_df = pd.DataFrame(centroids)
centroids_file = "cluster_centroids.csv"
centroids_df.to_csv(centroids_file, index=False)

print(f"Cluster centroids saved as '{centroids_file}'.")
