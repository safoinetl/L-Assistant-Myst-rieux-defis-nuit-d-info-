Project Overview
This project is a chatbot API developed using Flask, which leverages pre-trained language models from Hugging Face's Transformers library to process user messages, detect emotions, and generate context-aware responses. The chatbot also logs user messages and detected emotions in an SQLite database. A React.js frontend can be used to consume this API, providing an interactive user experience.

Prerequisites
Ensure you have the following installed on your system:

Python (version 3.7+)
Node.js (version 14+)
pip (Python package manager)
Backend Setup (Flask API)
1. Clone the Repository
First, clone the project repository to your local machine:

bash
git clone <your-repo-url>
cd <your-repo-directory>
2. Create a Virtual Environment (Optional but recommended)
Set up a Python virtual environment to keep your dependencies organized:

3. Install Dependencies
Install the required Python libraries:

bash
pip install -r requirements.txt
requirements.txt:

makefile
flask
transformers
huggingface_hub
flask-cors
torch
langdetect
sqlite3  # Python's built-in SQLite module
4. Run the Backend Server
Run the Flask app to start the server:

bash
python app.py
The API will be available at http://localhost:5000.

API Endpoints
1. Root Endpoint (/)
Method: GET
Description: Checks if the API is running.
Response:
json
{
  "message": "Welcome to Richatt Chatbot!",
}
2. Chat Endpoint (/chat)
Method: GET / POST
Description: Accepts user input, detects the emotion, generates a response, and logs data to the database.
Request (POST):
json
{
  "message": "im feeling sad, what should i do ?"
}
Response:
json
{
	"detected_language": "en",
	"emotion": "sadness",
	"emotion_detection_time": 0.03907918930053711,
	"emotion_response": "I'm here to help. Things will get better. 🌈",
	"generation_time": 22.391197681427002,
	"response": "Let me help you with that. Remember that your feelings are valid and temporary. Here are some suggestions that might help:\n1) Try to say something like \"You need a little sympathy for this situation\" or \"Your life has been difficult in the past so it was okay if I helped but don't be afraid of how much else can happen because there will always still remain hope inside yourself! You have just started right now as well...don't panic about things yet!! If anything happens unexpectedly please let us know asap - we would love not only helping our customers get their money back on time even though they lost cash (or more importantly lose all savings),but also getting them out from under stressful situations by providing practical solutions rather than throwing away bad habits!\n2 ) Tell someone who could give you: \"I am here at work today trying hard"
}
3. User Data Endpoint (/userdata)
Method: GET
Description: Retrieves the last 100 user messages and their detected emotions.
Response:
json
{
  "user_data": [
    {
      "id": 1,
      "message": "Hello, how are you?",
      "emotion": "joy",
      "timestamp": "2024-12-06T12:34:56"
    },
    ...
  ],
  "count": 100
}
Frontend Setup (React.js)
1. Create a React App
If you don't have a React app already, create one using create-react-app:

bash
npx create-react-app chatbot-frontend
cd chatbot-frontend
2. Install Axios for API Requests
Run the following command to install axios, which is used to make HTTP requests from the React app:

bash
npm install axios
3. Implement the Chat Interface
Create a component to handle user input and display the chatbot's response. Below is an example React component (ChatComponent.js):

javascript
import React, { useState } from 'react';
import axios from 'axios';

function ChatComponent() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    setLoading(true);
    try {
      const res = await axios.post('http://localhost:5000/chat', { message });
      setResponse(res.data.response);
    } catch (error) {
      console.error("Error sending message:", error);
      setResponse("Sorry, there was an error.");
    }
    setLoading(false);
    setMessage('');
  };

  return (
    <div>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type your message..."
      />
      <button onClick={sendMessage} disabled={loading}>
        {loading ? 'Sending...' : 'Send'}
      </button>
      {response && <p>Bot: {response}</p>}
    </div>
  );
}

export default ChatComponent;
4. Run the React App
Ensure the React app is running:

bash
npm start
The app will be available at http://localhost:3000.

Installation Guide for the Full Project
Backend:

Clone the repository and set up the environment.
Install dependencies with pip install -r requirements.txt.
Run the server with python app.py.
Frontend:

Create a React app and install axios.
Run the React app with npm start.
Example README.md
Here's an example README.md file for your project:

markdown
# Richatt Chatbot

## Project Overview

Richatt Chatbot is a Flask-based chatbot API that uses pre-trained language models to interact with users and provide emotion-aware responses. It is designed for seamless integration with a React.js frontend.

## Installation

### Backend
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
Set up a Python virtual environment:

bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install the dependencies:

bash
pip install -r requirements.txt
Run the server:

bash
python app.py
Frontend
Create a React app:

bash
npx create-react-app chatbot-frontend
cd chatbot-frontend
Install axios:

bash
npm install axios
Start the React app:

bash
npm start
Usage
Send messages through the React interface to receive emotion-aware responses from the Flask backend.
View logs of user data via the /userdata endpoint.
License
MIT License

yaml

---

This documentation should help you set up and understand both the backend and the React frontend for your chatbot project.