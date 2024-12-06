import pandas as pd

# Load the cleaned dataset
file_path = "cleaned_code_reviews.csv"
data = pd.read_csv(file_path)

# Display basic information about the dataset
print("Basic Info:")
print(data.info())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Display a sample of the data
print("\nSample Data:")
print(data.head())

# Check the distribution of text lengths (optional visualization)
data['text_length'] = data['cleaned_text'].apply(lambda x: len(str(x)))
print("\nText Length Distribution:")
print(data['text_length'].describe())

# Plot histogram of text lengths
import matplotlib.pyplot as plt

plt.hist(data['text_length'], bins=30, edgecolor='k', alpha=0.7)
plt.title("Distribution of Cleaned Text Lengths")
plt.xlabel("Text Length")
plt.ylabel("Frequency")
plt.show()

# Check for unique values in the main columns
print("\nUnique Values in 'cleaned_text':", data['cleaned_text'].nunique())
