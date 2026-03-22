# Import libraries
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
# Download NLTK data
nltk.download('stopwords')
# STEP 1: LOAD DATASET
df = pd.read_csv("sentiment_analysis.csv")
# Keep only required columns
df = df[['text', 'sentiment']]
# Clean data
df = df.dropna()
df['sentiment'] = df['sentiment'].str.lower()
# STEP 2: TEXT CLEANING (NLTK)
stop_words = set(stopwords.words('english'))
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)
df['cleaned'] = df['text'].apply(clean_text)
# STEP 3: LABEL ENCODING (FIXED)
y = df['sentiment'].map({
    'positive': 1,
    'neutral': 2,
    'negative': 0
})
# Remove invalid rows BEFORE vectorization (fixes your error)
df = df[y.notnull()]
y = y[y.notnull()]
# STEP 4: FEATURE EXTRACTION (TF-IDF)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['cleaned'])
# STEP 5: TRAIN MODEL (sklearn)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = MultinomialNB()
model.fit(X_train, y_train)
# STEP 6: EVALUATION
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
# STEP 7: PREDICTION FUNCTION
def predict_sentiment(text):
    cleaned = clean_text(text)
    vector = vectorizer.transform([cleaned])
    ml_result = model.predict(vector)[0]
    # ML prediction
    if ml_result == 1:
        ml_label = "Positive"
    elif ml_result == 2:
        ml_label = "Neutral"
    else:
        ml_label = "Negative"
    # TextBlob prediction 
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        tb_label = "Positive"
    elif polarity == 0:
        tb_label = "Neutral"
    else:
        tb_label = "Negative"
    return ml_label, tb_label
# STEP 8: TEST
print("\nCustom Predictions:\n")
samples = [
    "I love this app!",
    "It is okay, nothing special",
    "Worst experience ever"
]
for s in samples:
    ml, tb = predict_sentiment(s)
    print(f"Text: {s}")
    print(f"ML Prediction: {ml}")
    print(f"TextBlob Prediction: {tb}")
    print("-" * 40)