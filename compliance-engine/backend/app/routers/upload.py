
from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, File, HTTPException, UploadFile

router = APIRouter(prefix="/upload", tags=["Documents"])

UPLOAD_DIR = Path(__file__).resolve().parents[2] / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename or Path(file.filename).suffix.lower() != ".pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    document_id = str(uuid4())
    destination = UPLOAD_DIR / f"{document_id}.pdf"
    size = 0

    try:
        with destination.open("wb") as output:
            while chunk := await file.read(1024 * 1024):
                size += len(chunk)

                if size > MAX_FILE_SIZE:
                    raise HTTPException(
                        status_code=413,
                        detail="File exceeds the 10 MB limit."
                    )

                output.write(chunk)

        return {
            "document_id": document_id,
            "filename": Path(file.filename).name,
            "size_bytes": size,
            "status": "uploaded"
        }

    except Exception:
        destination.unlink(missing_ok=True)
        raise

    finally:
        await file.close()
