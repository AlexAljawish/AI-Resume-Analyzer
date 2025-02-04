import spacy
import re
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer

nlp = spacy.load("en_core_web_sm")

BLACKLIST = {"name", "email", "contact", "phone", "resume", "linkedin", "github", "www", "com"}

def clean_text(text):
    """Remove unwanted symbols, emails, and URLs from the text."""
    text = re.sub(r'\S+@\S+', '', text)  # Remove emails
    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # Remove URLs
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabetic characters
    return text.lower()

def extract_keywords(text):
    """Extract important keywords using TF-IDF and NLP"""
    text = clean_text(text)
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if token.pos_ in {"NOUN", "VERB", "ADJ"} and token.text.lower() not in BLACKLIST]

    # Use TF-IDF to get top words
    vectorizer = TfidfVectorizer(stop_words="english", max_features=10)
    tfidf_matrix = vectorizer.fit_transform([" ".join(tokens)])
    keywords = vectorizer.get_feature_names_out()

    return list(set(tokens) | set(keywords))  # Merge both approaches

def analyze_match(resume_text, job_description):
    """Compare resume and job description for match percentage"""
    resume_keywords = set(extract_keywords(resume_text))
    job_keywords = set(extract_keywords(job_description))

    match_count = len(resume_keywords.intersection(job_keywords))
    match_percentage = (match_count / len(job_keywords)) * 100 if job_keywords else 0

    return {
        "extracted_skills": list(resume_keywords),
        "improvements": list(job_keywords - resume_keywords),
        "match_percentage": round(match_percentage, 2),
    }
