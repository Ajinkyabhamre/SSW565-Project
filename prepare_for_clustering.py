import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import pickle

# Load the cleaned data
file_path = "cleaned_code_reviews.csv"
data = pd.read_csv(file_path)

# Step 1: TF-IDF Vectorization
print("Applying TF-IDF vectorization...")
tfidf_vectorizer = TfidfVectorizer(
    max_features=5000,  # Use top 5000 words
    stop_words='english',  # Remove English stopwords
    ngram_range=(1, 2)  # Use unigrams and bigrams
)
tfidf_matrix = tfidf_vectorizer.fit_transform(data['cleaned_text'])

# Save the TF-IDF vectorizer for future use
with open('tfidf_vectorizer.pkl', 'wb') as f:
    pickle.dump(tfidf_vectorizer, f)

print(f"TF-IDF matrix shape: {tfidf_matrix.shape}")

# Step 2: Dimensionality Reduction (Optional)
print("Reducing dimensions using Truncated SVD...")
svd = TruncatedSVD(n_components=50, random_state=42)  # Reduce to 50 components
reduced_matrix = svd.fit_transform(tfidf_matrix)

# Save the reduced matrix for clustering
with open('reduced_matrix.pkl', 'wb') as f:
    pickle.dump(reduced_matrix, f)

print(f"Reduced matrix shape: {reduced_matrix.shape}")
