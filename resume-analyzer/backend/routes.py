from flask import Blueprint, request, jsonify
from resume_parser import extract_resume_text
from ai_analysis import analyze_resume

resume_routes = Blueprint("resume_routes", __name__)

@resume_routes.route("/upload", methods=["POST"])
def upload_resume():
    """Handles resume file upload and extraction."""
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    text = extract_resume_text(file)
    return jsonify({"text": text})

@resume_routes.route("/analyze", methods=["POST"])
def analyze():
    """Handles resume analysis against job description."""
    data = request.get_json()
    resume_text = data.get("resume_text", "").strip()
    job_description = data.get("job_description", "").strip()

    if not resume_text or not job_description:
        return jsonify({"error": "Missing required fields"}), 400

    analysis = analyze_resume(resume_text, job_description)
    return jsonify(analysis)
