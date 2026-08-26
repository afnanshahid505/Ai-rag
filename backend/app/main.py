from rag.pdf_loader import extract_text_from_pdf
from rag.chunks import chunk_text
from rag.embeddings import generate_embeddings
pdf_path="../data/resume.pdf"
text=extract_text_from_pdf(pdf_path)
words=text.split()
print(len(words))
chunks=chunk_text(text)
print("total chunks", len(chunks))
embeddings=generate_embeddings(chunks)
print(embeddings.shape)
