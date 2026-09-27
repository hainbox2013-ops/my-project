# AI Chat Bot 🤖

A simple AI chatbot written in Python using the OpenAI Responses API.

## Features
- Interactive terminal chat
- Conversation memory during the current run
- Environment-variable API key
- No secret keys committed to Git

## Setup

1. Install Python 3.10+.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Copy `.env.example` to `.env`.
4. Put your OpenAI API key in `.env`.
5. Run:
   `python bot.py`

Type `exit` or `quit` to stop.

## Security

Never put your API key directly in source code or commit the `.env` file.
