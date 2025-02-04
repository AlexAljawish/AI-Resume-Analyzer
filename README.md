# AI Resume Analyzer

An AI-powered resume analyzer that uses Natural Language Processing (NLP) to help job seekers optimize their resumes for specific job descriptions. This application extracts skills from the resume, compares them with the job description, and calculates a match percentage to help candidates improve their resumes.

## Features

- **Resume Upload**: Upload your resume in PDF format.
- **Job Description Input**: Enter the job description to match with your resume.
- **Skill Extraction**: Extracts and displays relevant skills from the resume.
- **Match Percentage**: Calculates the match percentage between the resume and job description.
- **Improvement Suggestions**: Provides suggestions for improving your resume.

## Technologies Used

- **Backend**: Python, Flask
  - **Libraries**: `spaCy`, `flask`, `sklearn`
- **Frontend**: React.js
  - **Libraries**: Axios for API requests
  - **CSS**: TailwindCSS for styling
- **Natural Language Processing (NLP)**: Used to extract skills and analyze resumes.

## How It Works

The **AI Resume Analyzer** leverages NLP models to compare the content of a resume with a job description. The application works in two steps:

1. **Extracting Skills**: The system processes the resume and extracts nouns and proper nouns, which are likely to represent skills, experiences, and qualifications.
2. **Matching**: The job description is then parsed to extract important skills and requirements. The extracted skills from the resume are compared with those in the job description to generate a **match percentage**.
   
The application will also provide suggestions for improvement based on the difference between the extracted skills and the job requirements.

## Usage

The AI Resume Analyzer provides job seekers with an easy-to-use interface to compare their resumes with job descriptions. This tool extracts skills from the uploaded resume and compares them against the required skills in the job description. It helps identify areas for improvement and provides a match percentage to assist in resume optimization.

### Steps:
1. **Upload your resume**: Click on the "Choose File" button to upload your resume in PDF format.
2. **Enter job description**: Paste the job description for the role you're applying to.
3. **Click on "Analyze Resume"**: The app will process the resume and job description, displaying a match percentage and extracted skills.
4. **Suggestions for Improvement**: The app will also provide a list of improvements to increase the match percentage with the job description.

## Future Improvements

- **Improved Skill Extraction**: Enhance the accuracy of skill extraction using more advanced NLP models.
- **Resume Formatting Support**: Support various formats for resume uploads.
- **Additional Job Matching Criteria**: Include additional job requirements such as experience, education, etc.
- **Machine Learning Integration**: Implement machine learning algorithms to provide deeper insights and recommendations.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you find any bugs or would like to suggest improvements.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature-name`
5. Create a new pull request.

---

Happy to see you use the AI Resume Analyzer! 🌟

---

### Contact

- **Author**: [Alex Aljawish](https://github.com/AlexAljawish)
- **Email**: alexaljawish@gmail.com
- **GitHub**: [AlexAljawish](https://github.com/AlexAljawish)
