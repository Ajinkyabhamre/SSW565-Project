import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Clustered Data
file_path = "clustered_code_reviews.csv"  # Adjust the path if necessary
data = pd.read_csv(file_path)

# Step 2: Calculate Cluster Counts
cluster_counts = data['cluster'].value_counts().sort_index()  # Count data points in each cluster
total_points = len(data)  # Total number of data points

# Step 3: Calculate Percentage Distribution
cluster_percentages = (cluster_counts / total_points) * 100  # Convert to percentages

# Step 4: Display Results
print("Cluster Distributions:")
result_df = pd.DataFrame({
    'Cluster': cluster_counts.index,
    'Count': cluster_counts.values,
    'Percentage (%)': cluster_percentages.values
})
print(result_df)

# Step 5: Visualize Results (Bar Chart)
plt.figure(figsize=(10, 6))
plt.bar(cluster_counts.index, cluster_counts.values, color='blue', alpha=0.7)
plt.xticks(cluster_counts.index)
plt.xlabel("Cluster ID")
plt.ylabel("Number of Data Points")
plt.title("Cluster Distributions")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the plot or show it
plt.savefig("cluster_distribution.png")
plt.show()
