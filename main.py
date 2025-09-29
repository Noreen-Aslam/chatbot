import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv
from my_agents import computer  # custom logic

# 🔹 Load environment variables (.env file me GEMINI_API_KEY hona chahiye)
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# 🔹 Configure Gemini
genai.configure(api_key=gemini_api_key)

# 🔹 Initialize model
model = genai.GenerativeModel("gemini-2.0-flash")


# ---- Chainlit Callbacks ---- #

@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])
    await cl.Message(content="Hello! 👋 How can I help you today?").send()


@cl.on_message
async def main_handler(message: cl.Message):
    history = cl.user_session.get("history")

    # Save user message
    history.append({"role": "user", "content": message.content})

    # Agar user ne "math" likha ho to custom agent use karo
    if "math" in message.content.lower():
        response_text = computer(message.content)
    else:
        # Convert history into Gemini format
        formatted_history = [
            {"role": "user", "parts": [{"text": msg["content"]}]} if msg["role"] == "user"
            else {"role": "model", "parts": [{"text": msg["content"]}]}
            for msg in history
        ]

        # 🔹 Gemini ko async tariqe se call karo
        response = await cl.make_async(model.generate_content)(formatted_history)

        # Extract text safely
        response_text = getattr(response, "text", "⚠️ No response from model.")

    # Save assistant response in history
    history.append({"role": "assistant", "content": response_text})
    cl.user_session.set("history", history)

    # Send response back to user
    await cl.Message(content=response_text).send()
