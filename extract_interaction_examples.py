import pandas as pd

# Load the cleaned security reviews
file_path = 'cleaned_security_reviews.csv'
data = pd.read_csv(file_path)

# List of architectural attributes
attributes = ['security', 'documentation', 'performance', 'modifiability']

# Initialize a dictionary to store examples
interaction_examples = {attr: [] for attr in attributes if attr != 'security'}

# Extract examples
for _, row in data.iterrows():
    desc = row['description'].lower()
    for attr in interaction_examples:
        if 'security' in desc and attr in desc:
            interaction_examples[attr].append(row['description'])

# Display and save examples
for attr, examples in interaction_examples.items():
    print(f"\nAttribute: {attr.capitalize()}")
    for example in examples[:3]:  # Display up to 3 examples
        print(f" - {example}")

    # Save examples to files
    with open(f'interaction_examples_{attr}.txt', 'w') as f:
        f.write('\n'.join(examples))

print("\nInteraction examples saved in separate text files for each attribute.")
