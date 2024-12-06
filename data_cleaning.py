# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize  # Importing word_tokenize
import re
import string

nltk.download('punkt')
nltk.download('stopwords')

file_path = "Code_Review_Project.csv"

# Load data
data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Step 2: Load the data
file_path = "Code_Review_Project.csv"
data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Step 3: Focus on relevant columns
# Extract 'subject' and 'description' columns
data = data[['subject', 'description']]

# Combine 'subject' and 'description' into a single column
data['combined_text'] = data['subject'] + " " + data['description']

# Step 4: Normalize the text
def normalize_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove special characters, punctuation, and numbers
    text = re.sub(f"[{string.punctuation}]", " ", text)  # Remove punctuation
    text = re.sub(r'\d+', '', text)  # Remove numbers
    return text

# Apply normalization to the combined_text column
data['normalized_text'] = data['combined_text'].apply(normalize_text)

# Step 5: Tokenize and remove stopwords
# Define stopwords
stop_words = set(stopwords.words('english'))

def remove_stopwords(text):
    # Tokenize text
    words = word_tokenize(text)
    # Remove stopwords
    filtered_words = [word for word in words if word not in stop_words]
    return " ".join(filtered_words)

# Apply stopword removal
data['cleaned_text'] = data['normalized_text'].apply(remove_stopwords)

# Step 6: Save the cleaned data
# Retain only the cleaned_text column for further processing
cleaned_data = data[['cleaned_text']]
cleaned_data.to_csv("cleaned_code_reviews.csv", index=False)

print("Data cleaning and preprocessing completed. Cleaned data saved to 'cleaned_code_reviews.csv'.")
