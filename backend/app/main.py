from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.interview_service import generate_interview_questions
import os
from fastapi import File, UploadFile, HTTPException
import uuid
import shutil


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


@app.post("/interview/upload-resume"){
async def upload_resume(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type only PDF files are allowed")
    upload_dir= "data/uploads"
    os.makedirs(upload_dir,exist_ok=True)
    filename=f"{uuid.uuid4()}.pdf"
    pdf_path=os.path.join(upload_dir,filename)
    with open(pdf_path,"wb") as f:
        shutil.copyfileobj(file.file,f)
        try:
            questions = generate_interview_questions(pdf_path)
            return {
                "success": True,
                "questions": questions
                "fileName": filename
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error generating interview questions: {str(e)}")
        finally:
            if os.path.exists(pdf_path):
                os.remove(pdf_path)
    
}