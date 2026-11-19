
# Day 04 – Generative AI & LLMs

## Overview

This project is a Python-based AI Text Assistant developed as part of the VisionRoot AI Engineer Internship Training Program.

The application integrates the Google Gemini API to perform natural language processing tasks through a command-line interface.

## Learning Objectives

- Understand Generative AI and Large Language Models (LLMs).
- Learn about tokens, context windows, and temperature.
- Understand system instructions and user prompts.
- Explore structured JSON responses.
- Identify LLM limitations and hallucinations.
- Integrate an LLM API into a Python application.

## Features

### 1. Question Answering
Generates clear and relevant answers to user questions.

### 2. Text Summarization
Summarizes user-provided text into concise bullet points.

### 3. Text Rewriting
Rewrites text in professional English while preserving its original meaning.

### 4. Structured JSON Output
Requests structured responses containing:
- Topic
- Summary
- Keywords

## Technologies Used

- Python
- Google Gemini API
- Google Gen AI SDK
- python-dotenv
- JSON

## Project Structure

```text
Day-04/
├── main.py
├── test_gemini.py
├── list_models.py
├── requirements.txt
├── README.md
└── .env
```

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file inside the `Day-04` directory:

```env
GEMINI_API_KEY=your_api_key_here
```

Keep the API key private and exclude `.env` from version control.

## Running the Application

From the repository root:

```powershell
.\.venv\Scripts\python.exe .\Week-01\Day-04\main.py
```

## Application Menu

```text
1. Question Answering
2. Text Summarization
3. Text Rewriting
4. Structured JSON Output
5. Exit
```

## Error Handling

The application handles:
- Missing API keys
- Empty user input
- Invalid menu selections
- API rate limits
- Temporary model unavailability
- Invalid JSON responses

## Testing Status

- Gemini API connection: Successful
- Question Answering: Tested successfully
- Text Rewriting: Tested successfully
- Text Summarization: Implemented
- Structured JSON Output: Implemented; successful API response pending

Some API requests returned temporary 503 and 504 errors due to service availability or request timeouts.

## Conclusion

This project demonstrates how to integrate a Large Language Model into a Python application to perform common text-processing tasks using prompt engineering and structured output generation.
