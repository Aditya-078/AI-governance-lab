from fastapi import APIRouter

router = APIRouter(prefix ="/health", tags=["Health"])

@router.get("/")
def heath():
    return{
        "status": "Backend Connected ✅",
        "project": "Compliance Engine",
        "version": "0.1.0"
    }