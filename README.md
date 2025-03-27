# Duplicate Question Pairs Detector

Duplicate Question Pairs Detector is an NLP and machine learning project that predicts whether two input questions are duplicates. The project leverages text preprocessing, feature extraction (token-based and fuzzy matching), and a pre-trained machine learning model to perform duplicate detection. The model is trained on the [Quora Question Pairs dataset](https://www.kaggle.com/c/quora-question-pairs) and uses `model.pkl`, `cv.pkl`, and `stopwords.pkl` for predictions.

## Table of Contents
- [Overview](#overview)
- [Project Components](#project-components)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview
This project leverages NLP techniques and machine learning to identify duplicate question pairs. By preprocessing text (lowercasing, decontracting, punctuation removal), extracting features (common words, token similarity, fuzzy match scores), and applying a trained model, the system accurately classifies whether two questions are duplicates.

## Project Components

- **app.py**  
  Implements a Streamlit interface that:
  - Loads the pre-trained model from `model.pkl`.
  - Accepts two questions as input.
  - Uses helper functions to extract features and create a query vector.
  - Displays the prediction result ("Duplicate" or "Not Duplicate").

- **helper.py**  
  Contains functions for:
  - **Text Preprocessing:** Normalizes input text (lowercasing, decontracting, punctuation removal, etc.).
  - **Feature Extraction:** Computes basic, token-based, length-based, and fuzzy matching features.
  - **Query Vector Creation:** Combines extracted features with bag-of-words representations from the CountVectorizer (`cv.pkl`).

- **Model Files:**  
  - `model.pkl`: Trained machine learning model.
  - `cv.pkl`: Serialized CountVectorizer (or similar) for generating BoW features.
  - `stopwords.pkl`: Pickled list of stopwords used during preprocessing.

- **Training Notebook:**  
  The Jupyter Notebook (`initial_with_advance_feature.ipynb`) includes data exploration, preprocessing, feature engineering, model training, and serialization of model files.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/duplicate-question-detector.git
   cd duplicate-question-detector
Create a Virtual Environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Ensure your requirements.txt includes: streamlit, beautifulsoup4, distance, fuzzywuzzy, numpy, and scikit-learn.

Place the Required Files:

Ensure model.pkl, cv.pkl, and stopwords.pkl are in the project root directory.

Usage
Run the Application:

bash
Copy
Edit
streamlit run app.py
Interact with the Interface:

Enter two questions.

Click "Find" to see the prediction result.

Dataset
This project uses the Quora Question Pairs dataset, available on Kaggle.

Code Structure
graphql
Copy
Edit
duplicate-question-detector/
│
├── app.py                                 # Streamlit interface
├── helper.py                              # Utility functions for preprocessing and feature extraction
├── model.pkl                              # Trained machine learning model
├── cv.pkl                                 # CountVectorizer for BoW features
├── stopwords.pkl                          # List of stopwords
├── initial_with_advance_feature.ipynb     # Notebook for training and experimentation
├── requirements.txt                       # Python dependencies
└── docs/
    ├── Duplicate_Question_Pairs_Detector_Documentation.md  # Detailed documentation (Markdown)
    └── Duplicate_Question_Pairs_Detector_Documentation.pdf   # Converted PDF documentation
Contributing
Contributions are welcome. To contribute:

Fork the repository.

Create a new branch for your changes.

Commit your changes with clear messages.

Submit a pull request.
