🤖 **Multi-Provider AI Chatbot**



A web-based AI chatbot application with support for \*\*OpenAI\*\*, \*\*Gemini\*\*, and \*\*Groq\*\* models. Users can interact via a frontend interface, while the backend handles API requests to the respective AI providers.



---



**Table of Contents**



\- \[Project Overview](#project-overview)  

\- \[Features](#features)  

\- \[Folder Structure](#folder-structure)  

\- \[Requirements](#requirements)  

\- \[Setup \& Installation](#setup--installation)  

\- \[Running the Project](#running-the-project)  

\- \[Environment Variables](#environment-variables)  

\- \[API Endpoints](#api-endpoints)  

\- \[Future Enhancements](#future-enhancements)  

\- \[References](#references)  



---



\## \*\*Project Overview\*\*



This project is a full-stack AI chatbot system:



\- \*\*Backend:\*\* FastAPI handles requests, connects to AI provider APIs (OpenAI, Gemini, Groq).  

\- \*\*Frontend:\*\* Streamlit provides an interactive web interface for users to chat with the AI.  

\- \*\*Purpose:\*\* Demonstrates multi-provider AI integration in a professional, modular architecture suitable for deployment.



---



**Features**



\- Chat with AI using multiple providers: OpenAI, Gemini, Groq.  

\- Interactive web-based frontend using Streamlit.  

\- Modular backend for easy addition of new AI providers.  

\- Error handling and response fallback.  

\- Session-based chat history.  



---



**Folder Structure**



chatbot\_project/

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



\- Python 3.11+  

\- pip  

\- Virtual environment (recommended)  



**Python packages are listed in `requirements.txt`:**



```txt

fastapi

uvicorn

requests

python-dotenv

openai

google-generativeai

groq

streamlit



**Setup \& Installation**



1. Clone the repository



git clone <repository-url>

cd chatbot\_project



2\. Create virtual environment



python -m venv venv





3\. Activate virtual environment



Windows:



venv\\Scripts\\activate





Linux/Mac:



source venv/bin/activate





4\. Install dependencies



pip install -r backend/requirements.txt

pip install streamlit





5\. Create .env file in the root folder with your API keys:



OPENAI\_API\_KEY=your\_openai\_api\_key

GEMINI\_API\_KEY=your\_gemini\_api\_key

GROQ\_API\_KEY=your\_groq\_api\_key



**Running the Project**



1\. Start the Backend

cd backend

uvicorn main:app --reload





Backend will run at:



http://127.0.0.1:8000



2\. Start the Frontend



Open a new terminal (keep backend running):



&nbsp;	2.1 venv\\Scripts\\activate

&nbsp;	2.2 pip install streamlit

&nbsp;	2.3 streamlit --version

&nbsp;	2.4 streamlit run frontend/streamlit\_app.py





Frontend will open in your default browser.



**Environment Variables**



Variable	Description

OPENAI\_API\_KEY	OpenAI API key

GEMINI\_API\_KEY	Gemini AI API key

GROQ\_API\_KEY	Groq AI API key



**API Endpoints**

Root

GET /





Response:



{"message": "Chatbot API is running! Use /chat endpoint."}



Chat

POST /chat





Request Body:



{

&nbsp; "provider": "openai",

&nbsp; "message": "Hello, AI!"

}





Response:



{

&nbsp; "response": "Hello! How can I assist you today?"

}



**Future Enhancements**



* Add authentication for users.
* Persistent chat history stored in a database.
* Real-time WebSocket chat for better UX.
* Additional AI providers and models.
* Deploy as a cloud application with Docker/Kubernetes.



References



* FastAPI Documentation
* Streamlit Documentation
* OpenAI Python SDK
* Google Gemini AI
* Groq AI SDK
