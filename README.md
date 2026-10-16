# CLI Chatbot Experiments

Two introductory API lessons from Aiolearn coursework, refactored to avoid embedding secrets or invalid network endpoints.

## Gemini API example

```bash
python -m pip install -r requirements.txt
# Set GEMINI_API_KEY using your terminal or OS secret manager before running.
python gemini_chatbot.py
```

Optionally set `GEMINI_MODEL` to a model available to your account. The default is `gemini-2.5-flash`; model availability and API pricing may change.

## Local chat client

`local_chat_client.py` expects a separately running HTTP server with a `/chat?text=...` route. **The server implementation is not included.** Set `LOCAL_CHAT_URL` if necessary. The example defaults to `http://127.0.0.1:8000/chat`.

## Security

- Store API keys in environment variables; never in GitHub files or screenshots.
- `.env` files are ignored by Git.
- Original course code was reorganized with AI assistance. This is a learning project, not a hosted chatbot service.
