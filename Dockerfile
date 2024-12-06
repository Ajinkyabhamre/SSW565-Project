# Use an official Python image as a base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download necessary NLTK data
RUN python -m nltk.downloader punkt stopwords punkt_tab

# Copy the project files
COPY . .

# Command to run the application
CMD ["python", "data_cleaning.py"]
