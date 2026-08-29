import re


def clean_line(text: str) -> str:

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def is_heading(block: dict, average_font_size: float) -> bool:

    text = block["text"].strip()

    if not text:
        return False

    words = text.split()

    # Headings are usually short
    if len(words) > 8:
        return False

    # Ignore very long lines
    if len(text) > 80:
        return False

    # Larger font than normal text
    larger_font = block["font_size"] >= average_font_size * 1.15

    # Bold text
    # PyMuPDF flag 16 commonly represents bold
    bold = bool(block["flags"] & 16)

    # Mostly uppercase
    letters = [c for c in text if c.isalpha()]

    uppercase_ratio = (
        sum(c.isupper() for c in letters) / len(letters)
        if letters
        else 0
    )

    mostly_uppercase = uppercase_ratio > 0.7

    return larger_font or bold or mostly_uppercase


def layout_aware_chunks(
    blocks: list[dict],
    max_words: int = 150
) -> list[str]:

    if not blocks:
        return []

    # Calculate average font size
    font_sizes = [
        block["font_size"]
        for block in blocks
        if block["font_size"] > 0
    ]

    average_font_size = (
        sum(font_sizes) / len(font_sizes)
        if font_sizes
        else 10
    )

    sections = []

    current_section = []
    current_heading = None

    for block in blocks:

        text = clean_line(block["text"])

        if not text:
            continue

        if is_heading(block, average_font_size):

            # Save previous section
            if current_section:

                sections.append({
                    "heading": current_heading,
                    "content": current_section
                })

            current_heading = text
            current_section = []

        else:

            current_section.append(text)

    # Save final section
    if current_section:

        sections.append({
            "heading": current_heading,
            "content": current_section
        })

    # Convert sections into chunks
    chunks = []

    for section in sections:

        heading = section["heading"]
        content = section["content"]

        words = []

        if heading:
            words.extend(heading.split())

        for line in content:
            words.extend(line.split())

        start = 0

        while start < len(words):

            end = start + max_words

            chunk_words = words[start:end]

            chunk = " ".join(chunk_words)

            if chunk.strip():
                chunks.append(chunk)

            start = end

    return chunks