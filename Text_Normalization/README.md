# Text Normalization

A Python-based text normalization project that demonstrates common NLP preprocessing techniques.

The goal of this project is to clean and normalize raw text before using it for tasks such as text classification, sentiment analysis, information retrieval, similarity search, and other NLP applications.

## Features

The text normalization pipeline includes:

1. **Lowercasing**
   - Converts text into lowercase for consistent processing.

2. **URL and Email Protection**
   - Replaces URLs and email addresses with tokens before applying destructive preprocessing.

3. **Contraction Expansion**
   - Converts contractions into their full forms.
   - Example: `can't` → `cannot`

4. **Emoji Handling**
   - For sentiment analysis, emojis can be converted into text.
   - For other NLP tasks, emojis can be removed.

5. **Punctuation Removal**
   - Removes punctuation marks when required.

6. **Special Character Removal**
   - Removes unwanted special characters.

7. **Repeated Character Normalization**
   - Reduces excessive repeated characters.
   - Example: `goooo` → `goo`

8. **Extra Space Removal**
   - Removes unnecessary spaces and normalizes whitespace.

9. **Optional Spell Correction**
   - Uses TextBlob to correct spelling mistakes.

## Technologies Used

- Python
- Regular Expressions (`re`)
- `string`
- `contractions`
- `emoji`
- `TextBlob`

## Installation

Install the required libraries:

```bash
pip install contractions emoji textblob
