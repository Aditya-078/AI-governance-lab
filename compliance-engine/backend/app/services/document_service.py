
from pathlib import Path

import pymupdf
import pytesseract
from PIL import Image
from pypdf import PdfReader
from io import BytesIO

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def extract_pdf_text(file_path: str | Path) -> dict:
    file_path = Path(file_path)

    reader = PdfReader(str(file_path))
    pdf_document = pymupdf.open(str(file_path))

    pages = []
    ocr_pages = 0

    try:
        for index, page in enumerate(reader.pages):
            text = (page.extract_text() or "").strip()

            # Use OCR when normal extraction returns little text.
            if len(text) < 20:
                pix = pdf_document[index].get_pixmap(
                    matrix=pymupdf.Matrix(2, 2),
                    alpha=False
                )
                image = Image.open(
                    BytesIO(pix.tobytes("png"))
                )

                text = pytesseract.image_to_string(
                    image,
                    lang="eng"
                ).strip()

                ocr_pages += 1

            pages.append({
                "page": index + 1,
                "text": text
            })

        full_text = "\n\n".join(
            page["text"] for page in pages if page["text"]
        )

        return {
            "page_count": len(pages),
            "character_count": len(full_text),
            "ocr_pages": ocr_pages,
            "text": full_text,
            "pages": pages
        }

    finally:
        pdf_document.close()
