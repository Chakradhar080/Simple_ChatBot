# backend/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .bots import OpenAIBot, GeminiBot, GroqBot

# Initialize bots
openai_bot = OpenAIBot()
gemini_bot = GeminiBot()
groq_bot = GroqBot()

app = FastAPI(title="Multi-Provider Chatbot API")

class ChatRequest(BaseModel):
    provider: str
    message: str

@app.get("/")
async def root():
    return {"message": "Chatbot API running! Use /chat"}

@app.post("/chat")
async def chat(request: ChatRequest):
    provider = request.provider.lower()
    if provider == "openai":
        return {"response": openai_bot.get_response(request.message)}
    elif provider == "gemini":
        return {"response": gemini_bot.get_response(request.message)}
    elif provider == "groq":
        return {"response": groq_bot.get_response(request.message)}
    else:
        raise HTTPException(status_code=400, detail="Invalid provider")
