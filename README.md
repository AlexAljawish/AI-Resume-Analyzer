# AI Resume Analyzer

An **AI-powered Resume Analyzer** that leverages Natural Language Processing (NLP) to help job seekers optimize their resumes by matching them with specific job descriptions. This application extracts key skills from resumes, compares them with the job requirements, and calculates a match percentage to help candidates improve their chances.

## 🚀 Features

- **Resume Upload**: Upload your resume in PDF format for analysis.
- **Job Description Input**: Paste the job description to compare with your resume.
- **Skill Extraction**: Extracts relevant skills from your resume.
- **Match Percentage**: Displays a percentage showing how well your resume matches the job description.
- **Improvement Suggestions**: Provides actionable suggestions to improve your resume’s match with the job.

## ⚙️ Technologies Used

- **Backend**:
  - **Python** (Flask)
  - Libraries: `spaCy`, `flask`, `sklearn`
  
- **Frontend**:
  - **React.js** with TailwindCSS for styling
  - **Axios** for API requests
  
- **NLP**: Utilizes **spaCy** to extract and compare skills between the resume and the job description.

## 🔧 How It Works

The **AI Resume Analyzer** functions in two key steps:

1. **Skill Extraction**:
   - The system processes the uploaded resume, identifying **skills**, **qualifications**, and **experiences** (extracted as nouns and proper nouns).

2. **Matching**:
   - The job description is parsed, and key requirements and skills are extracted. The extracted resume skills are then compared with the job description to compute a **match percentage**.

Additionally, the application provides **suggestions** for improving the resume based on mismatches between the extracted skills and the job requirements.

## 🧑‍💻 Usage

### Steps to Analyze Your Resume:

1. **Upload Your Resume**: Click on the "Choose File" button to upload your resume in **PDF** format.
2. **Enter Job Description**: Paste the job description for the role you're applying to.
3. **Click "Analyze Resume"**: The system will analyze the resume and job description, displaying a match percentage and relevant skills.
4. **Review Improvement Suggestions**: The tool will suggest improvements to increase your resume's match with the job description.

## 🔮 Future Improvements

- **Advanced Skill Extraction**: Enhance NLP models to better identify and categorize skills.
- **File Format Support**: Extend support to other resume file formats (e.g., DOCX, TXT).
- **Broader Job Matching Criteria**: Add additional factors like experience, education, etc.
- **Machine Learning**: Implement ML models to make deeper, more personalized recommendations.

## 🤝 Contributing

We welcome contributions! Here's how you can help improve the project:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature-name`
5. Create a pull request.

---

Thank you for using the **AI Resume Analyzer**! 🌟

---

### Contact

- **Author**: [Ahmad Aljawish](https://github.com/AlexAljawish)
- **Email**: [ahmadaljawish9@gmail.com](mailto:ahmadaljawish9@gmail.com)
- **GitHub**: [AlexAljawish](https://github.com/AlexAljawish)
