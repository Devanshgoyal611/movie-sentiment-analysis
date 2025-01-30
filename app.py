from flask import Flask, render_template, request, jsonify
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import WhitespaceTokenizer
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

app = Flask(__name__)

# Load model and vectorizer
with open('Saved_model\logistic_regression.pkl', 'rb') as f:
    model = pickle.load(f)

with open('Saved_model\vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Negation words to keep
negation_words = {'not', "don't", "couldn't", "didn't", "doesn't", "hadn't", "hasn't", 
                  "haven't", "isn't", "mightn't", "mustn't", "needn't", "shouldn't", 
                  "wasn't", "weren't", "won't", "wouldn't"}

# Prepare stopwords
nltk_stopwords = set(stopwords.words('english'))
custom_stopwords = nltk_stopwords - negation_words

def cleaner(x):
    x = re.sub(r'<.*?>', '', x)
    x = re.sub(r'[\([{})\]!@#$,"%^*?:;~]', ' ', x)
    x = re.sub(r"\\|[0-9]|/|-|_|'|\.", '', x)
    x = re.sub(r'\s+', ' ', x)
    return x.lower()

def preprocess_text(text):
    # Clean text
    cleaned = cleaner(text)
    
    # Tokenize
    tokenizer = WhitespaceTokenizer()
    tokens = tokenizer.tokenize(cleaned)
    
    # Remove stopwords (keep negation words)
    filtered = [word for word in tokens if word not in custom_stopwords]
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(word) for word in filtered]
    
    return ' '.join(lemmatized)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['review']
    processed_text = preprocess_text(text)
    vector = vectorizer.transform([processed_text])
    prediction = model.predict(vector)[0]
    sentiment = 'Positive' if prediction == 1 else 'Negative'
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)