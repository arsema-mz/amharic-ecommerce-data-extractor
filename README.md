# README: Building an Amharic E-commerce Data Extractor

## Project Overview

In this project, I transformed messy Telegram posts into a smart FinTech engine that helps identify the best vendors for loan opportunities in the Ethiopian e-commerce landscape. My goal was to ingest data from various Telegram channels, preprocess it, and extract meaningful entities for further analysis.

## Tasks Overview

### Task 1: Data Ingestion and Data Preprocessing

#### Objective
I set up a data ingestion system to fetch messages from multiple Ethiopian-based Telegram e-commerce channels and prepared the raw data for entity extraction.

#### Steps

1. **Channel Selection**:
   - I identified and connected to at least 5 relevant Telegram channels to gather data.

2. **Message Ingestion**:
   - I implemented a custom scraper to collect text, images, and documents as they were posted in real time.

3. **Data Preprocessing**:
   - I tokenized and normalized the text data while addressing Amharic-specific linguistic features.
   - I cleaned and structured the data into a unified format, separating metadata (e.g., sender, timestamp) from message content.

4. **Data Storage**:
   - I stored the preprocessed data in a structured format for further analysis.

### Task 2: Label a Subset of Dataset in CoNLL Format

#### Objective
I labeled a portion of the provided dataset in the CoNLL format, which is commonly used for Named Entity Recognition (NER) tasks.

#### Steps

1. **Dataset Utilization**:
   - I used the "Message" column of the larger dataset, which contains text descriptions of various products and entities.

2. **CoNLL Format**:
   - I labeled each token (word) on its own line, followed by its entity label.
   - I ensured blank lines separate individual sentences/messages.

3. **Entity Types**:
   - I assigned labels based on the following entity types:
     - **B-Product**: Beginning of a product entity (e.g., "Baby bottle").
     - **I-Product**: Inside a product entity (e.g., the word "bottle" in "Baby bottle").
     - **B-LOC**: Beginning of a location entity (e.g., "Addis Ababa", "Bole").
     - **I-LOC**: Inside a location entity (e.g., the word "Ababa" in “Addis Ababa”).
     - **B-PRICE**: The beginning of a price entity (e.g., "ዋጋ 1000 ብር").
     - **I-PRICE**: Inside a price entity (e.g., the word "1000" in “ዋጋ 1000 ብር”).
     - **O**: Tokens that are outside any entities.

4. **Labeling**:
   - I labeled at least 30 messages from the provided dataset and saved my work in a plain text file in the CoNLL format.

