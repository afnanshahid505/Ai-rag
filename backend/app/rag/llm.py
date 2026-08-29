import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = "gemini-3.7-flash"


def generate_questions(contexts):
    prompt = """
You are an AI technical interviewer.

Based ONLY on the resume contexts provided below, generate exactly 10
technical interview questions.

Requirements:
- Generate exactly 10 questions.
- Cover different parts of the candidate's resume.
- Avoid repeating the same project or technology unnecessarily.
- Questions should be suitable for a technical interview.
- Do not answer the questions.
- Return ONLY valid JSON.
- Use this exact format:

{
    "questions": [
        {
            "id": 1,
            "topic": "topic name",
            "question": "question text"
        }
    ]
}

Resume contexts:

"""

    for item in contexts:
        prompt += f"""
Topic: {item["topic"]}

Context:
{item["context"]}

--------------------
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    text = response.text.strip()

    # Remove markdown code fences if Gemini adds them
    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)