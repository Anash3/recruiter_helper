import pdfplumber
from pathlib import Path


def extract_text(pdf_path: str) -> str:
    """
    Extracts text from a PDF file.
    """
    pdf_file = Path(pdf_path)
    if not pdf_file.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    text_content = []
    try:
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    text_content.append(text)
    except Exception as e:
        print(f"Error processing PDF {pdf_path}: {e}")
        return ""

    return "\n".join(text_content)
