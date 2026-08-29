from rag.pdf_loader import extract_layout_from_pdf
from rag.chunks import layout_aware_chunks
from rag.embeddings import generate_embeddings
from rag.vector_store import create_index, search_index
from rag.interview_topics import INTERVIEW_TOPICS
from rag.llm import generate_questions


def generate_interview_questions():

    # -----------------------------
    # 1. Extract resume text
    # -----------------------------

    pdf_path = "../data/resume.pdf"

    text = extract_layout_from_pdf(pdf_path)

    # -----------------------------
    # 2. Create chunks
    # -----------------------------

    chunks = layout_aware_chunks(text)

    # -----------------------------
    # 3. Create embeddings
    # -----------------------------

    embeddings = generate_embeddings(chunks)

    # -----------------------------
    # 4. Create FAISS index
    # -----------------------------

    index = create_index(embeddings)

    # -----------------------------
    # 5. Retrieve context for each topic
    # -----------------------------

    contexts = []

    for topic in INTERVIEW_TOPICS:

        query_embedding = generate_embeddings(
            [topic["query"]]
        )[0]

        retrieved_chunks = search_index(
            query_embedding,
            index,
            chunks,
            k=3
        )

        context = "\n\n".join(retrieved_chunks)

        contexts.append({
            "topic": topic["topic"],
            "context": context
        })

    # -----------------------------
    # 6. ONE Gemini request
    # -----------------------------

    questions = generate_questions(contexts)

    return questions