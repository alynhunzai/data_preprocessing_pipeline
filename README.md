# Data Preprocessing Pipeline

A lightweight, zero-dependency text preprocessing pipeline for preparing text data for machine learning applications.

## Overview

This project provides a simple yet effective pipeline to clean and normalize raw text data. It removes special characters, normalizes whitespace, and converts text to lowercase—all without external dependencies.

## Requirements

- **Python 3.6+** (no additional libraries required)

## Setup

1. **Clone or download this repository**
    ``` https://github.com/alynhunzai/data_preprocessing_pipeline ```
2. **Prepare your input data:**
    - Place all `.txt` files in the `data/raw/` directory
    - Create the directory if it doesn't exist:
      ```bash
      mkdir -p data/raw data/processed
      ```

3. **Verify Python installation:**
    ```bash
    python --version
    ```

## Usage

Run the pipeline with:

```bash
python main.py
```

### What happens:
1. The pipeline reads all `.txt` files from `data/raw/`
2. Applies text cleaning operations (removes special characters, normalizes spacing, converts to lowercase)
3. Saves the processed data to `data/processed/cleaned_data.json`

### Output format:

The output JSON file contains an array of objects with `original` and `cleaned` text:

```json
[
  {
      "user_id": "user_101",
      "product_id": "prod_55A",
      "original_review": "This laptop is AWESOME!!! I absolutely love it. <br> Fast shipping too...",
      "cleaned_review": "this laptop is awesome i absolutely love it fast shipping too"
  }
]
```

## Project Structure

```
data_preprocessing_pipeline/
├── data/
│   ├── raw/           # Place input .txt files here
│   └── processed/     # Output files saved here
├── core/
│   ├── file_handler.py
│   └── text_cleaner.py
├── main.py
└── README.md
```
