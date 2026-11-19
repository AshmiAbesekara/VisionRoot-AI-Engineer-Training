
import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

load_dotenv(Path(__file__).with_name(".env"))

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
   model="gemini-3.7-flash",
    contents="Explain Generative AI in one simple sentence."
)

print("Gemini Response:")
print(response.text)

