import pandas as pd

# Load the preprocessed messages CSV
df = pd.read_csv("data/combined_messages.csv")

import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize

# Tokenize the messages
df['tokenized_messages'] = df['message'].apply(lambda x: word_tokenize(x))

# Display the tokenized messages
print(df[['message', 'tokenized_messages']].head())

import re

def normalize_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

# Apply normalization
df['normalized_messages'] = df['message'].apply(normalize_text)

# Display the normalized messages
print(df[['message', 'normalized_messages']].head())

# Select relevant columns
structured_df = df[['channel', 'normalized_messages']]  

# Save the structured data to a new CSV
structured_df.to_csv("data/structured_messages.csv", index=False, encoding='utf-8-sig')

print("Structured data saved to 'data/structured_messages.csv'")