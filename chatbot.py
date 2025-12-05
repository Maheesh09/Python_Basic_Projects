from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client  = OpenAI(
    api_key=api_key
)

def ask_model(message: str) -> str:
    """
    Send a single message to the model and get back a reply.
    No memory / history yet.

    """
    response = client.chat.completions.create(
        model = "gpt-4.1-mini",
        messages = [
            {"role": "user", "content": "You are a friendly chatbot"},
            {"role": "user", "content": message},
        ],
        max_tokens=200,
    )
    reply = response.choices[0].message.content
    return reply

if __name__ == "__main__":
    user_message = "Hello, how are you?"
    bot_reply = ask_model(user_message)
    print("Bot reply:", bot_reply)