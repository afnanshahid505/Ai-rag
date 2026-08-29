import pymupdf


def extract_layout_from_pdf(pdf_path: str) -> list[dict]:

    doc = pymupdf.open(pdf_path)

    blocks = []

    for page_number, page in enumerate(doc):

        page_dict = page.get_text("dict")

        for block in page_dict["blocks"]:

            if "lines" not in block:
                continue

            for line in block["lines"]:

                line_text = ""

                font_sizes = []
                font_names = []
                font_flags = []

                for span in line["spans"]:

                    text = span["text"].strip()

                    if not text:
                        continue

                    line_text += text + " "

                    font_sizes.append(span["size"])
                    font_names.append(span["font"])
                    font_flags.append(span["flags"])

                line_text = line_text.strip()

                if not line_text:
                    continue

                blocks.append({
                    "text": line_text,
                    "page": page_number,
                    "bbox": line["bbox"],
                    "font_size": max(font_sizes) if font_sizes else 0,
                    "font": font_names[0] if font_names else "",
                    "flags": font_flags[0] if font_flags else 0,
                })

    doc.close()

    return blocks