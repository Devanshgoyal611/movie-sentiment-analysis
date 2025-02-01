# 🎬 IMDB Movie Review Sentiment Analysis

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green?logo=flask)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A machine learning web application that predicts sentiment (positive/negative) from movie reviews using a Linear SVC model.

## 📂 Data Used

[![IMDB Dataset of 50K Movie Reviews](https://img.shields.io/badge/Dataset-Kaggle-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

## 📁 Project Structure

```text
.
├── app.py                 # Flask web application
├── data_ingestion.py      # Script to store raw data in SQLite
├── model_training.ipynb   # Jupyter notebook for EDA and modeling
├── Cleaned_movies.db      # Cleaned/preprocessed data
├── movies.db              # Raw movie data
├── requirements.txt       # Dependency list
├── model.pkl              # Trained Linear SVC model
└── vectorizer.pkl         # TF-IDF vectorizer
```

## 🚀 About `app.py`

The core Flask application features:

✨ **Key Functionality**:
- Text input interface with real-time results
- Advanced text processing pipeline:
  - 🧹 HTML/Special character removal
  - 📝 Custom stopword filtering
  - 🔍 Lemmatization with WhitespaceTokenizer
- 🤖 Integration with trained Linear SVC model
- 🔄 AJAX-powered predictions without page reload

⚙️ **Technical Highlights**:
- JSON API endpoint (`/predict`)
- NLTK-based text preprocessing
- TF-IDF vectorization
- Error handling for user inputs

## 🌟 Features

| Category              | Details                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| 🖥️ Web Interface      | Responsive design with CSS styling                                     |
| 🔧 Text Processing    | Custom cleaning pipeline preserving negation words                     |
| 🧠 Machine Learning   | Linear SVC model with >89% accuracy                                    |
| 🗄️ Data Management    | SQLite integration for raw/cleaned data                                |
| 🧩 Modularity         | Separation of concerns (data processing vs web interface)              |

## 🛠️ Technologies Used

- **Core**: ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
- **Web Framework**: ![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask)
- **ML**: ![scikit-learn](https://img.shields.io/badge/-scikit--learn-F7931E?logo=scikit-learn)
- **NLP**: ![NLTK](https://img.shields.io/badge/-NLTK-40B5A4)
- **Database**: ![SQLite](https://img.shields.io/badge/-SQLite-003B57?logo=sqlite)

## ▶️ How to Run the Application

### Prerequisites
- Python 3.8+
- pip package manager

### ⚙️ Installation

1. **Clone repository**
   ```bash
   git clone https://github.com/Devanshgoyal611/movie-sentiment-analysis.git
   cd movie-sentiment-analysis
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download NLTK data**
   ```bash
   python -m nltk.downloader stopwords wordnet
   ```

### 🏃♂️ Running the Application

```bash
python app.py
```

🌐 Access the application at: `http://localhost:5000`

### 🖱️ Usage Guide
1. Enter movie review text in the textarea
2. Click "Analyze Sentiment" button
3. View results in colored box below:
   - 🟢 Green: Positive sentiment
   - 🔴 Red: Negative sentiment

**Note**: Ensure `model.pkl` and `vectorizer.pkl` are present in root directory before running. To retrain model, execute all cells in `model.ipynb`.
```