# AI Interview Platform

An AI-powered interview platform that generates personalized technical interview questions from a candidate's uploaded resume using Retrieval-Augmented Generation (RAG).

## Features

- Resume PDF upload and layout-aware text extraction
- Section-based resume chunking
- Embedding generation and FAISS vector similarity search
- RAG-based resume context retrieval
- Google Gemini API for personalized question generation
- Generates 10 interview questions in a single LLM request
- FastAPI backend with JSON REST APIs
- React frontend for conducting interviews
- Gemini-based candidate answer evaluation with scores and feedback

## RAG Pipeline

Resume → PDF Extraction → Chunking → Embeddings → FAISS → Relevant Context → Gemini → Interview Questions

For answer evaluation:

Candidate Answer + Question + Resume Context → Gemini → Score + Feedback

## Tech Stack

**Frontend:** React.js, Vite  
**Backend:** Python, FastAPI, Uvicorn  
**AI:** Google Gemini API, RAG  
**Vector Search:** FAISS  
**Embeddings:** Sentence Transformers  
**PDF Processing:** PyMuPDF

## Project Goal

The goal is to build a resume-aware AI interviewer that generates questions based on the candidate's actual skills, projects, experience, education, and certifications instead of relying on generic interview questions.