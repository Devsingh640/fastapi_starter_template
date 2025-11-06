from fastapi import APIRouter

student_router = APIRouter()

@student_router.get("/student")
def get_student():
    return {"message":"student get route"}