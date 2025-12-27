import pickle
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# Load vectorizer and model
with open("src/tfidf_vectorizer.pkl", "rb") as f:
    tfidf = pickle.load(f)

with open("src/spam_model.pkl", "rb") as f:
    model = pickle.load(f)


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.split()
    text = [word for word in text if word not in stopwords.words('english')]
    return ' '.join(text)



def predict_spam_with_confidence(message):
    cleaned = clean_text(message)
    vectorized = tfidf.transform([cleaned])
    
    prediction = model.predict(vectorized)[0]
    confidence = model.predict_proba(vectorized).max() * 100

    label = "Spam 🚨" if prediction == 1 else "Not Spam ✅"
    return label, round(confidence, 2)




