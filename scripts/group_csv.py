import pandas as pd

# Load your flat CSV
df = pd.read_csv('data/Labeled_data.csv')  # adjust path if needed

# Heuristic: define a new sentence when label == 'B-PRICE' and the token includes a comma
sentence_boundaries = df['label'].eq('B-PRICE') & df['token'].str.contains(',')

# Create a sentence ID
sentence_id = sentence_boundaries.cumsum()

# Group by sentence ID
grouped = df.groupby(sentence_id)

# Convert to list of sentences
sentences = []
for _, group in grouped:
    tokens = group['token'].tolist()
    labels = group['label'].tolist()
    sentence = list(zip(tokens, labels))
    sentences.append(sentence)

print(f"✅ Reconstructed {len(sentences)} labeled sentences.")
