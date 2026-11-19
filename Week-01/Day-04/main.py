
import os
import json
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import APIError


load_dotenv(Path(__file__).resolve().parent / ".env")

api_key = os.getenv("GEMINI_API_KEY")
MODEL_NAME = "gemini-3.7-flash"

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(timeout=60000)
)


def generate_response(prompt, json_schema=None):
    config = types.GenerateContentConfig(
        temperature=0.3,
        system_instruction=(
            "You are a helpful and professional AI text assistant. "
            "Provide accurate, clear, and concise responses. "
            "Do not invent information."
        )
    )

    if json_schema is not None:
        config.response_mime_type = "application/json"
        config.response_json_schema = json_schema

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=config
        )

        if not response.text:
            print("Error: Gemini returned an empty response.")
            return None

        return response.text

    except APIError as error:
        print(f"\nGemini API Error: {error.code}")

        if error.code == 503:
            print("The model is temporarily busy. Try again later.")
        elif error.code == 429:
            print("API rate limit exceeded. Try again later.")
        elif error.code == 404:
            print("Model not available. Check MODEL_NAME.")
        else:
            print(error.message)

        return None

    except Exception as error:
        print(f"\nUnexpected error: {error}")
        return None


def answer_question(question):
    prompt = (
        "Answer the following question clearly and accurately "
        "using simple English.\n\n"
        f"Question:\n{question}"
    )

    return generate_response(prompt)


def summarize_text(text):
    prompt = (
        "Summarize the following text.\n"
        "Requirements:\n"
        "- Use 3 to 5 bullet points.\n"
        "- Preserve the main ideas.\n"
        "- Do not add unsupported information.\n\n"
        f"Text:\n{text}"
    )

    return generate_response(prompt)


def rewrite_text(text):
    prompt = (
        "Rewrite the following text in professional English.\n"
        "Requirements:\n"
        "- Improve grammar and clarity.\n"
        "- Preserve the original meaning.\n"
        "- Use a polite, professional tone.\n"
        "- Do not add new information.\n\n"
        f"Original text:\n{text}"
    )

    return generate_response(prompt)


def generate_json_summary(text):
    schema = {
        "type": "object",
        "properties": {
            "topic": {
                "type": "string"
            },
            "summary": {
                "type": "string"
            },
            "keywords": {
                "type": "array",
                "items": {
                    "type": "string"
                }
            }
        },
        "required": ["topic", "summary", "keywords"]
    }

    prompt = (
        "Analyze the following text and identify its main "
        "topic, a concise summary, and relevant keywords. "
        "Use only information supported by the text.\n\n"
        f"Text:\n{text}"
    )

    response = generate_response(
        prompt,
        json_schema=schema
    )

    if response is None:
        return None

    try:
        return json.loads(response)

    except json.JSONDecodeError:
        print("Error: Gemini returned invalid JSON.")
        return None


def main():
    print("\n=== Day 04 - AI Text Assistant ===")

    while True:
        print("\nSelect a task:")
        print("1. Question Answering")
        print("2. Text Summarization")
        print("3. Text Rewriting")
        print("4. Structured JSON Output")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "5":
            print("\nThank you for using AI Text Assistant!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please select 1-5.")
            continue

        user_text = input("\nEnter your text: ").strip()

        if not user_text:
            print("Error: Input cannot be empty.")
            continue

        print("\nProcessing your request...")

        if choice == "1":
            result = answer_question(user_text)

            if result is not None:
                print("\n--- AI Answer ---")
                print(result)

        elif choice == "2":
            result = summarize_text(user_text)

            if result is not None:
                print("\n--- AI Summary ---")
                print(result)

        elif choice == "3":
            result = rewrite_text(user_text)

            if result is not None:
                print("\n--- Rewritten Text ---")
                print(result)

        elif choice == "4":
            result = generate_json_summary(user_text)

            if result is not None:
                print("\n--- Structured JSON Output ---")
                print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
