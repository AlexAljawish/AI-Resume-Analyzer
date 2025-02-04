import React, { useState } from "react";
import ResumeUpload from "./components/ResumeUpload";
import ResumeAnalyzer from "./components/ResumeAnalyzer";
import "./index.css";

const App = () => {
  const [resumeText, setResumeText] = useState("");

  return (
    <div className="app-container">
      <h1>AI Resume Analyzer</h1>
      <ResumeUpload onUpload={setResumeText} />
      {resumeText && <ResumeAnalyzer resumeText={resumeText} />}
    </div>
  );
};

export default App;
