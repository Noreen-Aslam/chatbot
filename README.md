# Gemini Chatbot with Chainlit

A conversational AI chatbot powered by **Google Gemini 2.0** and built using **Chainlit**. It supports math-related queries via a custom agent and general conversation via Gemini's language model.

---

## Features

- Asynchronous chatbot for fast responses
- Maintains chat history per session
- Handles math queries with a custom agent (`my_agents.computer`)
- Safe response extraction to avoid crashes
- Easy to configure with `.env` file for Gemini API key

---

## Requirements

- Python 3.11 or later
- Chainlit
- Google Generative AI SDK (`google-generativeai`)
- `python-dotenv`

Install dependencies:

```bash
pip install -r requirements.txt
