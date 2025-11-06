from fastapi import FastAPI
from src.packages.students.controller import student_router
from src.packages.subjects.controller import subject_router

def init_routes(application: FastAPI):
    application.include_router(student_router, tags=["students"])
    application.include_router(subject_router, tags=["subjects"])