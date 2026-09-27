import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
app = Flask(__name__)

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")
client = OpenAI(api_key=api_key) if api_key else None

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/chat")
def chat():
    if not client:
        return jsonify({"error": "OPENAI_API_KEY is not configured."}), 500

    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    if not message:
        return jsonify({"error": "Message is empty."}), 400

    try:
        response = client.responses.create(
            model=model,
            instructions="You are a friendly, helpful AI assistant. Answer clearly.",
            input=message,
        )
        return jsonify({"reply": response.output_text})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=False)
