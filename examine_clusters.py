import pandas as pd

# Load the clustered data
clustered_file = "clustered_code_reviews.csv"
data = pd.read_csv(clustered_file)

# Parameters
n_samples = 5  # Number of samples to display per cluster

# Display sample data for each cluster
clusters = data['cluster'].unique()
for cluster in sorted(clusters):
    print(f"Cluster {cluster}:")
    cluster_data = data[data['cluster'] == cluster].sample(n=min(n_samples, len(data[data['cluster'] == cluster])))
    print(cluster_data['cleaned_text'].tolist())
    print("\n" + "-" * 50 + "\n")

