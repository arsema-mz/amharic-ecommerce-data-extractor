# 🛍️ Amharic E-commerce Data Extractor

Transform messy Amharic Telegram e-commerce messages into structured insights using Named Entity Recognition (NER). This project helps identify key entities like **Products**, **Prices**, and **Locations**, laying the foundation for a unified e-commerce intelligence platform.

## 📌 Overview

Telegram is a growing marketplace in Ethiopia. However, it is decentralized and messy. This project extracts structured business data from unstructured Telegram messages in Amharic, enabling EthioMart to build a centralized vendor analysis platform to identify top-performing sellers—especially for financial services like loans.

## 🎯 Objectives

- Build a pipeline to scrape, clean, and preprocess Amharic Telegram messages.
- Manually label Amharic messages for Named Entity Recognition (NER) in CoNLL format.
- Fine-tune transformer-based and spaCy-based NER models to detect:
  - `Product`
  - `Price`
  - `Location`
- Store results for downstream vendor profiling and ranking.
- Explore model interpretability using SHAP/LIME (optional).


## 🧠 Skills & Tools Used

- **Amharic NLP:** Tokenization and preprocessing for Amharic
- **NER Modeling:** spaCy, Hugging Face Transformers (`xlm-roberta-base`)
- **Labeling Format:** CoNLL-style annotations
- **Model Evaluation:** F1-score, precision, recall
- **Visualization (optional):** SHAP, LIME for model explainability

## 🛠️ Setup & Installation

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/amharic-ecommerce-data-extractor.git
   cd amharic-ecommerce-data-extractor
````

2. Create a virtual environment and install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) For Hugging Face login:

   ```bash
   huggingface-cli login
   ```

## 🚀 Usage

* **Telegram Scraper:**

  ```bash
  python scripts/scraper.py
  ```

* **Convert Labeled Data:**

  ```bash
  python scripts/conll_to_dataframe.py
  python scripts/group_csv.py
  ```

* **Train spaCy NER Model:**

  ```bash
  python scripts/train_spacy_ner.py
  ```

* **Inference:**

  ```python
  from spacy import load
  nlp = load("amharic_ner_model")
  doc = nlp("መዚድ ፕላዛ በ 3600 ብር አለ።")
  for ent in doc.ents:
      print(ent.text, ent.label_)
  ```

## 📊 Results

| Entity   | F1-Score (spaCy) |
| -------- | ---------------- |
| Product  | 0.83             |
| Price    | 0.91             |
| Location | 0.78             |

> ✅ Model trained for 10 epochs with decreasing loss. Saved in `amharic_ner_model/`.

## ⚠️ Challenges

* Tokenization issues with comma-joined numbers (e.g., "40,41,42")
* Limited labeled data for fine-tuning large models
* Slow inference with Hugging Face models on local machines

