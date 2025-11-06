from fastapi import APIRouter

subject_router = APIRouter()


@subject_router.get("/subject")
def get_subject():
    return {"message":"subject get route"}