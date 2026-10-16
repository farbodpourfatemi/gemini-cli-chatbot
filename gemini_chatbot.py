"""Minimal Gemini API CLI; set GEMINI_API_KEY and optional GEMINI_MODEL."""
import os
import requests

BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models/"


def ask_gemini(prompt: str, api_key: str, model: str) -> str:
    if not prompt.strip():
        raise ValueError("Prompt must not be empty")
    response = requests.post(
        f"{BASE_URL}{model}:generateContent",
        headers={"x-goog-api-key": api_key, "Content-Type": "application/json"},
        json={"contents": [{"parts": [{"text": prompt}]}]},
        timeout=45,
    )
    response.raise_for_status()
    data = response.json()
    texts = [part.get("text", "") for candidate in data.get("candidates", [])
             for part in candidate.get("content", {}).get("parts", [])]
    return "\n".join(text for text in texts if text) or "No text returned by the model."


def main() -> None:
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        print("Set GEMINI_API_KEY as an environment variable. Never commit it to GitHub.")
        return
    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    prompt = input("Question: ")
    try:
        print(ask_gemini(prompt, key, model))
    except (requests.RequestException, ValueError, KeyError) as exc:
        print(f"Request failed: {type(exc).__name__}. Check model name, key and quota.")


if __name__ == "__main__":
    main()
