import React, { useState } from "react";
import axios from "axios";

const ResumeAnalyzer = ({ resumeText }) => {
  const [jobDescription, setJobDescription] = useState("");
  const [analysis, setAnalysis] = useState(null);

  const analyzeResume = async () => {
    if (!resumeText || !jobDescription) return alert("Please enter a job description.");

    try {
      const res = await axios.post("http://127.0.0.1:5000/analyze", {
        resume_text: resumeText,
        job_description: jobDescription,
      });

      setAnalysis(res.data);
    } catch (error) {
      console.error("Error analyzing resume:", error);
    }
  };

  return (
    <div className="analyze-container">
      <textarea
        placeholder="Enter Job Description"
        onChange={(e) => setJobDescription(e.target.value)}
      />
      <button onClick={analyzeResume}>Analyze</button>

      {analysis && (
        <div className="results">
          <h3>Results:</h3>
          <p><strong>Match Percentage:</strong> {analysis.match_percentage}%</p>
          <p><strong>Extracted Skills:</strong> {analysis.extracted_skills.join(", ")}</p>
          <p><strong>Improvements:</strong> {analysis.improvements.join(", ")}</p>
        </div>
      )}
    </div>
  );
};

export default ResumeAnalyzer;
