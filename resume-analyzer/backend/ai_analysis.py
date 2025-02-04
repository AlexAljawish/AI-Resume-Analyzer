import spacy
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

# Define a blacklist of common words to ignore
BLACKLIST = {"name", "skills", "customer", "linkedin", "github", "email", "contact", "phone", "resume"}

EMAIL_REGEX = r'\S+@\S+'
URL_REGEX = r'https?://\S+|www\.\S+'
NON_ALPHA_REGEX = r'[^a-zA-Z0-9+#.]'

def preprocess_text(text):
    """Cleans and preprocesses text."""
    text = re.sub(EMAIL_REGEX, '', text)  # Remove emails
    text = re.sub(URL_REGEX, '', text)    # Remove URLs
    doc = nlp(text)

    # Extract meaningful words (nouns, verbs) and remove stop words
    extracted_words = {token.lemma_.lower() for token in doc if token.pos_ in {"NOUN", "VERB"} and not token.is_stop}
    
    # Remove blacklist words and non-alphabetic characters
    extracted_words = {word for word in extracted_words if word not in BLACKLIST and not re.search(NON_ALPHA_REGEX, word)}

    return " ".join(extracted_words)

def analyze_resume(resume_text, job_description):
    """Analyzes the resume against the job description using TF-IDF and Cosine Similarity."""
    cleaned_resume = preprocess_text(resume_text)
    cleaned_job_desc = preprocess_text(job_description)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([cleaned_resume, cleaned_job_desc])
    
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0] * 100  # Convert to percentage
    
    return {
        "extracted_skills": cleaned_resume.split(),
        "improvements": ", ".join(set(cleaned_job_desc.split()) - set(cleaned_resume.split())),
        "match_percentage": round(similarity, 2),
    }
