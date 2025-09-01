# backend/bots.py
import os
from openai import OpenAI
import google.generativeai as genai
from groq import Groq
from dotenv import load_dotenv

load_dotenv()  # load .env keys

# ---------------- OPENAI BOT ----------------
class OpenAIBot:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def get_response(self, message: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": message}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"⚠️ OpenAI Error: {str(e)}"

# ---------------- GEMINI BOT ----------------
class GeminiBot:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def get_response(self, message: str) -> str:
        try:
            response = self.model.generate_content(message)
            return response.text
        except Exception as e:
            return f"⚠️ Gemini Error: {str(e)}"

# ---------------- GROQ BOT ----------------
class GroqBot:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def get_response(self, message: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[{"role": "user", "content": message}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"⚠️ Groq Error: {str(e)}"
