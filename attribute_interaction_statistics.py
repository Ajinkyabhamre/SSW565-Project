import pandas as pd
from collections import Counter

# Load the cleaned security reviews
file_path = 'cleaned_security_reviews.csv'
data = pd.read_csv(file_path)

# Focus on the 'description' column for interaction analysis
descriptions = data['description']

# List of architectural attributes
attributes = ['security', 'documentation', 'performance', 'modifiability']

# Initialize a dictionary to store interaction counts
interaction_counts = {attr: 0 for attr in attributes}

# Count occurrences of each attribute
for desc in descriptions:
    for attr in attributes:
        if attr in desc.lower():  # Case-insensitive matching
            interaction_counts[attr] += 1

# Display the interaction counts
interaction_df = pd.DataFrame.from_dict(interaction_counts, orient='index', columns=['count'])
print("\nInteraction Counts:")
print(interaction_df)

# Save the results for documentation
interaction_df.to_csv('attribute_interaction_statistics.csv', index_label='attribute')

print("\nInteraction statistics saved as 'attribute_interaction_statistics.csv'.")
