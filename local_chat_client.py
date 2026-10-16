"""Client for an optional local /chat server; server is NOT included."""
import os
import requests


def main() -> None:
    url = os.getenv("LOCAL_CHAT_URL", "http://127.0.0.1:8000/chat")
    prompt = input("Question: ").strip()
    if not prompt:
        print("Question cannot be empty.")
        return
    try:
        result = requests.get(url, params={"text": prompt}, timeout=15)
        result.raise_for_status()
        print(result.text)
    except requests.RequestException:
        print("Request failed. Is the local chat server running at LOCAL_CHAT_URL?")


if __name__ == "__main__":
    main()
