import pandas as pd

# Load categorized data
data = pd.read_csv("categorized_security_reviews.csv")

# Analyze interactions
print("Interaction Between Security and Other Attributes:")
non_security_reviews = data[data["attribute"] != "Security"]
for attribute in non_security_reviews["attribute"].unique():
    related_reviews = non_security_reviews[non_security_reviews["cleaned_description"].str.contains("security", case=False)]
    print(f"\n{attribute}: {len(related_reviews)} reviews mention 'security'")
    sample_reviews = related_reviews["cleaned_description"].sample(3, random_state=42)
    for review in sample_reviews:
        print(f" - {review}")

print("\nAnalysis Complete. Insights are provided above.")
