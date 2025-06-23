import json
import glob
import pandas as pd

all_messages = []

json_files = glob.glob("data/raw/*_messages.json")
print("Found files:", json_files)  # Debug line

for file in json_files:
    with open(file, 'r', encoding='utf-8') as f:
        messages = json.load(f)
        all_messages.extend(messages)

# Convert to DataFrame for easy processing
df = pd.DataFrame(all_messages)

# Save combined file
df.to_csv("data/combined_messages.csv", index=False, encoding='utf-8-sig')

print(f"Combined {len(df)} messages from {len(json_files)} files.")
