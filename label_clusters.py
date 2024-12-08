import pandas as pd

# Load clustered data
file_path = 'clustered_code_reviews.csv'
data = pd.read_csv(file_path)

# Define a mapping of clusters to architectural attributes
cluster_labels = {
    0: 'documentation',
    1: 'security',
    2: 'performance',
    3: 'security',
    4: 'documentation',
    5: 'performance',
    6: 'security',
    7: 'documentation',
}

# Apply the labels
data['attribute'] = data['cluster'].map(cluster_labels)

# Save the labeled dataset
data.to_csv('labeled_data.csv', index=False)
print("Labeled data saved to 'labeled_data.csv'.")
