import pandas as pd
from collections import Counter

# Load the auto-evaluated predictions
predicted_data = pd.read_csv('auto_evaluated_checkins.csv')

# Analyze distribution of predicted attributes
attribute_counts = Counter(predicted_data['predicted_attribute'])
print("Attribute Distribution:")
for attribute, count in attribute_counts.items():
    print(f"{attribute}: {count}")

# Dynamically determine the number of samples
sample_size = min(10, len(predicted_data))

# Randomly sample predictions for manual inspection
if sample_size > 0:
    sample_predictions = predicted_data.sample(sample_size, random_state=42)
    print("\nSample Predictions:")
    print(sample_predictions)
else:
    print("\nNo data available for sampling.")
