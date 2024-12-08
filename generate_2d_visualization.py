import pandas as pd
import pickle
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Load reduced features and cluster assignments
with open('reduced_features.pkl', 'rb') as f:
    reduced_features = pickle.load(f)

clustered_data = pd.read_csv('clustered_code_reviews.csv')

# Apply t-SNE for 2D projection
print("Applying t-SNE for 2D visualization...")
tsne = TSNE(n_components=2, random_state=42, perplexity=30, n_iter=1000)
reduced_2d = tsne.fit_transform(reduced_features)

# Create a DataFrame for visualization
visualization_df = pd.DataFrame(reduced_2d, columns=['x', 'y'])
visualization_df['cluster'] = clustered_data['cluster']

# Plot the clusters
plt.figure(figsize=(10, 8))
scatter = plt.scatter(
    visualization_df['x'], visualization_df['y'], 
    c=visualization_df['cluster'], cmap='tab10', alpha=0.7, s=50
)
plt.colorbar(scatter, label='Cluster')
plt.title('t-SNE Visualization of Clusters')
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.savefig('tsne_2d_visualization.png')
print("2D visualization saved as 'tsne_2d_visualization.png'.")
