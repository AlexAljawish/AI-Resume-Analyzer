import requests

url = "http://127.0.0.1:5000/analyze"
data = {
    "resume_text": "I have experience in Python, Flask, and AI development.",
    "job_description": "Looking for a candidate with experience in Python, Flask, and NLP."
}

response = requests.post(url, json=data)
print(response.json())  # Print the response from Flask API
