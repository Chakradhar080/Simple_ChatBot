# frontend/streamlit_app.py
import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 AI Chatbot")
st.write("Talk to your AI assistant powered by OpenAI, Gemini, or Groq.")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).markdown(msg["content"])

if prompt := st.chat_input("Type your message..."):
    st.chat_message("user").markdown(prompt)
    st.session_state["messages"].append({"role": "user", "content": prompt})

    try:
        response = requests.post(BACKEND_URL, json={"message": prompt, "provider": "openai"})
        if response.status_code == 200:
            bot_reply = response.json().get("response", "⚠️ No response from bot")
        else:
            bot_reply = f"⚠️ Error: {response.text}"
    except Exception as e:
        bot_reply = f"⚠️ Connection error: {str(e)}"

    st.chat_message("assistant").markdown(bot_reply)
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})
