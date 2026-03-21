import pandas as pd
# Load dataset
df = pd.read_csv("email.csv")
print(df.head())
# Convert labels to binary
df['spam'] = df['Category'].apply(lambda x: 1 if x == 'spam' else 0)
# Split data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    df['Message'], df['spam'], test_size=0.25, random_state=42
)
# Use TF-IDF vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
# Train model
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)
# Sample emails
emails = [
    "Congratulations! You've been selected for a free vacation. Claim now!",
    "Hi, are we still on for the meeting at 5 PM today?",
    "Limited time offer! Get cashback on your credit card usage.",
    "Can you send me the notes from today's lecture?"
]
emails_tfidf = vectorizer.transform(emails)
print("Predictions:", model.predict(emails_tfidf))
# Model accuracy
X_test_tfidf = vectorizer.transform(X_test)
print("Accuracy:", model.score(X_test_tfidf, y_test))
# Pipeline 
from sklearn.pipeline import Pipeline
clf = Pipeline([
    ('vectorizer', TfidfVectorizer(stop_words='english')),
    ('nb', MultinomialNB())
])
clf.fit(X_train, y_train)
print("Pipeline Accuracy:", clf.score(X_test, y_test))
print("Pipeline Predictions:", clf.predict([
    "You have won a lottery of ₹10,00,000! Click here to claim now.",
    "Hey, let's grab coffee after class."
]))