import os
import PyPDF2
import spacy
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ensure upload directory exists
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load NLP model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file):
    """Extract text from an uploaded PDF file."""
    try:
        reader = PyPDF2.PdfReader(file)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        return text.strip() if text else "No readable text found in PDF."
    except Exception as e:
        return f"Error extracting text: {str(e)}"

def analyze_resume(resume_text, job_description):
    """Analyze the resume text against the job description."""
    resume_doc = nlp(resume_text)
    job_doc = nlp(job_description)

    resume_skills = {token.lemma_.lower() for token in resume_doc if not token.is_stop and token.is_alpha}
    job_requirements = {token.lemma_.lower() for token in job_doc if not token.is_stop and token.is_alpha}

    matching_skills = resume_skills.intersection(job_requirements)
    match_percentage = (len(matching_skills) / len(job_requirements)) * 100 if job_requirements else 0

    return {
        "extracted_skills": list(resume_skills),
        "improvements": list(job_requirements - resume_skills),
        "match_percentage": round(match_percentage, 2),
    }

@app.route("/upload", methods=["POST"])
def upload_resume():
    """Handle file upload and text extraction."""
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    text = extract_text_from_pdf(file)
    return jsonify({"extracted_text": text})

@app.route("/analyze", methods=["POST"])
def analyze():
    """Analyze resume against job description."""
    data = request.json
    resume_text = data.get("resume_text", "")
    job_description = data.get("job_description", "")

    if not resume_text or not job_description:
        return jsonify({"error": "Missing resume text or job description"}), 400

    result = analyze_resume(resume_text, job_description)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
