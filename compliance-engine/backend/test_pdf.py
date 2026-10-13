
from pathlib import Path
from app.services.document_service import extract_pdf_text

pdf_path = (
    Path(__file__).resolve().parent
    / "uploads"
    / "79f96287-7152-4bbe-954a-6bfd3a244cc8.pdf"
)

result = extract_pdf_text(pdf_path)

print("Pages:", result["page_count"])
print("Characters:", result["character_count"])
print("\nExtracted text:\n")
print(result["text"][:1000])
