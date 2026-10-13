
from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID

from app.services.document_service import extract_pdf_text

router = APIRouter(prefix="/analysis", tags=["Analysis"])

# Temporary in-memory storage.
# Results will be lost when the backend restarts.
analysis_results = {}

UPLOAD_DIR = Path(__file__).resolve().parents[2] / "uploads"


class AnalyzeRequest(BaseModel):
    document_id: str = Field(
        ...,
        description="The document_id returned by POST /upload/"
    )


@router.post("/")
def analyze_document(request: AnalyzeRequest):
    # Validate the document ID.
    try:
        document_id = str(UUID(request.document_id))
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid document ID."
        )

    # Find the uploaded PDF.
    pdf_path = UPLOAD_DIR / f"{document_id}.pdf"

    if not pdf_path.is_file():
        raise HTTPException(
            status_code=404,
            detail="Uploaded document not found."
        )

    # Extract text, including OCR for scanned pages.
    try:
        extracted = extract_pdf_text(pdf_path)
    except Exception:
        raise HTTPException(
            status_code=422,
            detail="Could not process this PDF."
        )

    if not extracted["text"].strip():
        raise HTTPException(
            status_code=422,
            detail="No readable text found in this PDF."
        )

    analysis_id = str(uuid4())

    result = {
        "analysis_id": analysis_id,
        "document_id": document_id,
        "status": "completed",
        "document": {
            "page_count": extracted["page_count"],
            "character_count": extracted["character_count"],
            "ocr_pages": extracted.get("ocr_pages", 0),
        },
        "message": (
            "Document extraction completed. "
            "Compliance comparison is not implemented yet."
        ),
    }

    analysis_results[analysis_id] = result

    return result


@router.get("/{analysis_id}")
def get_analysis(analysis_id: str):
    try:
        analysis_id = str(UUID(analysis_id))
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid analysis ID."
        )

    result = analysis_results.get(analysis_id)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Analysis not found."
        )

    return result
