🤖 **Multi-Provider AI Chatbot**

This project is a **multi-provider AI chatbot** **system** that allows users to interact with OpenAI, Google Gemini, and Groq AI models through a single web interface. The backend is powered by **FastAPI**, providing REST endpoints for chat interactions, while the frontend is built with **Streamlit**, offering a clean and interactive user interface.

Key features include:

1. Support for multiple AI providers (OpenAI, Gemini, Groq).
2. Easy-to-use chat interface with persistent session messages.
3. Fully modular backend with separate bot wrappers for each provider.
4. Environment variable management for secure API keys.
5. Designed to be extendable for additional AI providers or cloud deployment.

**Tech Stack**:

**Backend**: Python, FastAPI

**Frontend**: Streamlit

**APIs**: OpenAI, Google Gemini, Groq

**Environment Management**: .env

**Ideal For**:

Developers learning AI API integration
Multi-provider chatbot projects
Rapid prototyping of conversational AI systems

---

**Table of Contents**



1. Project Overview
2. Features 
3. Folder Structure 
4. Requirements  
5. Setup & Installation
6. Running the Project
7. Environment Variables 
8. API Endpoints
9. Future Enhancements
10. References

---

**Project Overview**

This project is a full-stack AI chatbot system:

**Backend**: FastAPI handles requests, connects to AI provider APIs (OpenAI, Gemini, Groq).  
**Frontend**: Streamlit provides an interactive web interface for users to chat with the AI.  
**Purpose**: Demonstrates multi-provider AI integration in a professional, modular architecture suitable for deployment.

---

**Features**

1. Chat with AI using multiple providers: OpenAI, Gemini, Groq.  
2. Interactive web-based frontend using Streamlit.  
3. Modular backend for easy addition of new AI providers.  
4. Error handling and response fallback.  
5. Session-based chat history.  

---

**Folder Structure**

**chatbot_project**/

│── .env # API keys

│── requirements.txt # Python dependencies

│── README.md # Project documentation

│

├── backend/

│ │── main.py # FastAPI backend entry point

│ │── bots.py # Unified bot wrapper (OpenAI, Gemini, Groq)

│

└── frontend/

│── streamlit\_app.py # Streamlit frontend interface

---

**Requirements**

Python 3.11+  
pip  
Virtual environment (recommended)  


**Python packages are listed in `requirements.txt`:**

fastapi
uvicorn
requests
python-dotenv
openai
google-generativeai
groq
streamlit

---

**Setup & Installation**



1. Clone the repository

  git clone <repository-url>

  cd chatbot\_project

2. Create virtual environment

  python -m venv venv

3. Activate virtual environment
Windows:
  venv\\Scripts\\activate

Linux/Mac:
  source venv/bin/activate

4. Install dependencies
  
  pip install -r backend/requirements.txt

  pip install streamlit


5. Create .env file in the root folder with your API keys:

  OPENAI_API_KEY=your_openai_api_key
  GEMINI_API_KEY=your_gemini_api_key
  GROQ_API_KEY=your_groq_api_key

---

**Running the Project**

1. Start the Backend

  cd backend

  uvicorn main:app --reload

Backend will run at:

  http://127.0.0.1:8000

2. Start the Frontend

Open a new terminal (keep backend running):

  2.1 venv\\Scripts\\activate
  2.2 pip install streamlit
  2.3 streamlit --version
  2.4 streamlit run frontend/streamlit\_app.py

Frontend will open in your default browser.

---

**Environment Variables**

Variable	Description

OPENAI_API_KEY	OpenAI API key

GEMINI_API_KEY	Gemini AI API key

GROQ_API_KEY	Groq AI API key

---

**API Endpoints**

Root
GET /
Response:
{"message": "Chatbot API is running! Use /chat endpoint."}

Chat
POST /chat
Request Body:

{
     "provider": "openai",
     "message": "Hello, AI!"
}

Response:
{
     "response": "Hello! How can I assist you today?"
}

---

**Future Enhancements**

* Add authentication for users.
* Persistent chat history stored in a database.
* Real-time WebSocket chat for better UX.
* Additional AI providers and models.
* Deploy as a cloud application with Docker/Kubernetes.

---

**References**

* FastAPI Documentation
* Streamlit Documentation
* OpenAI Python SDK
* Google Gemini AI
* Groq AI SDK
