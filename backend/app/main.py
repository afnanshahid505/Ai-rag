from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.interview_service import generate_interview_questions


app = FastAPI()


# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "AI Interview API is running"
    }


@app.get("/interview/questions")
def get_interview_questions():

    questions = generate_interview_questions()

    return {
        "success": True,
        "questions": questions
    }