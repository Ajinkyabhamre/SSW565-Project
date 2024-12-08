import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Load the data
file_path = "Security_Code_Review_Project-2.csv"

# Handle encoding issues
try:
    data = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    data = pd.read_csv(file_path, encoding='ISO-8859-1')

print("Basic Info:")
print(data.info())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Display sample data
print("\nSample Data:")
print(data.head())

# Define a text cleaning function
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    tokens = word_tokenize(text)  # Tokenize the text
    tokens = [word for word in tokens if word not in stopwords.words('english')]  # Remove stopwords
    return ' '.join(tokens)

# Apply text cleaning to the 'description' column
data['cleaned_description'] = data['description'].apply(clean_text)

# Save the cleaned data for future analysis
data.to_csv('cleaned_security_reviews.csv', index=False)
print("\nCleaned data saved as 'cleaned_security_reviews.csv'.")
