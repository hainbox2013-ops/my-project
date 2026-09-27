import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY is missing. Add it to your .env file.")

client = OpenAI(api_key=api_key)
previous_response_id = None

print("🤖 AI Chat Bot")
print("Type 'exit' or 'quit' to stop.\n")

while True:
    try:
        user_message = input("You: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nBye! 👋")
        break

    if not user_message:
        continue

    if user_message.lower() in {"exit", "quit"}:
        print("Bye! 👋")
        break

    request = {
        "model": model,
        "instructions": "You are a helpful, friendly AI assistant. Answer clearly and concisely.",
        "input": user_message,
    }

    if previous_response_id:
        request["previous_response_id"] = previous_response_id

    try:
        response = client.responses.create(**request)
        previous_response_id = response.id
        print(f"Bot: {response.output_text}\n")
    except Exception as exc:
        print(f"Error: {exc}\n")
