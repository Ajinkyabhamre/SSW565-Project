import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns
import pickle


# Load preprocessed data
with open('reduced_matrix.pkl', 'rb') as f:
    reduced_matrix = pickle.load(f)

# Elbow Method to determine the optimal number of clusters
print("Applying the Elbow Method...")
inertia_values = []
range_clusters = range(2, 15)

for k in range_clusters:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(reduced_matrix)
    inertia_values.append(kmeans.inertia_)

# Plot Elbow Curve
plt.figure(figsize=(8, 5))
plt.plot(range_clusters, inertia_values, marker='o', linestyle='-', color='b')
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia (Sum of Squared Distances)")
plt.title("Elbow Method for Optimal k")
plt.grid(True)
plt.savefig("elbow_method_plot.png")
print("Elbow Method plot saved as 'elbow_method_plot.png'.")

# Calculate Silhouette Scores
print("Calculating Silhouette Scores...")
silhouette_scores = []
for k in range_clusters:
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(reduced_matrix)
    silhouette_scores.append(silhouette_score(reduced_matrix, labels))

# Plot Silhouette Scores
plt.figure(figsize=(8, 5))
plt.plot(range_clusters, silhouette_scores, marker='o', linestyle='-', color='g')
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Scores for Different k")
plt.grid(True)
plt.savefig("silhouette_scores_plot.png")
print("Silhouette Scores plot saved as 'silhouette_scores_plot.png'.")

print("Check the plots to decide the optimal number of clusters.")
