import pandas as pd

# Load the clustered data
clustered_data = pd.read_csv("security_clustered_reviews.csv")

# Manually map clusters to attributes
cluster_to_attribute = {
    0: "Security",
    1: "Security",
    2: "Performance",
    3: "Security",
    4: "Modifiability",
    5: "Security",
    6: "Documentation",
    7: "Modifiability"
}

# Map attributes to clusters
clustered_data["attribute"] = clustered_data["cluster"].map(cluster_to_attribute)

# Save the updated dataset
clustered_data.to_csv("categorized_security_reviews.csv", index=False)
print("Categorized clusters saved as 'categorized_security_reviews.csv'.")
