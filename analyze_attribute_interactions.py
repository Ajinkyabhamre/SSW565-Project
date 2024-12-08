import pandas as pd

# Load the categorized data
data = pd.read_csv("categorized_security_reviews.csv")

# Count reviews by attribute
attribute_counts = data["attribute"].value_counts()
print("\nAttribute Distribution:")
print(attribute_counts)

# Analyze interactions between attributes
print("\nSample Reviews by Attribute:")
for attribute in data["attribute"].unique():
    print(f"\nAttribute: {attribute}")
    sample_reviews = data[data["attribute"] == attribute]["cleaned_description"].sample(3, random_state=42)
    for review in sample_reviews:
        print(f" - {review}")
