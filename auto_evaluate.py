import pandas as pd
import pickle

# Load the trained model and vectorizer
with open('classifier_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Load new data for evaluation
new_data = pd.read_csv('new_checkins.csv')  # Replace with your new data file

# Apply TF-IDF vectorization
X_new = vectorizer.transform(new_data['cleaned_text'])

# Predict attributes
predictions = model.predict(X_new)
new_data['predicted_attribute'] = predictions

# Save the results
new_data.to_csv('auto_evaluated_checkins.csv', index=False)
print("Auto-evaluated check-ins saved to 'auto_evaluated_checkins.csv'.")
