import pandas as pd

def parse_conll(filepath):
    sentences = []
    sentence = []
    
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                if sentence:
                    sentences.append(sentence)
                    sentence = []
            else:
                token, label = line.split()
                sentence.append((token, label))
    
    if sentence:  # Catch last one if no trailing newline
        sentences.append(sentence)

    return sentences

# Adjust the path to your CoNLL file
conll_data = parse_conll("Labeled_data.con11")

# Preview the first parsed message
for token, label in conll_data[0]:
    print(f"{token} -> {label}")
