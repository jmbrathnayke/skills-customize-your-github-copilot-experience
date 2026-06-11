from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# TODO: Define your Pydantic models here
# Example:
# class Task(BaseModel):
#     name: str
#     description: Optional[str] = None
#     completed: bool = False

# TODO: Create an in-memory storage (e.g., a list or dictionary)
# tasks = []

# Task 1: Create a root endpoint
# @app.get("/")
# def read_root():
#     TODO: Return a welcome message

# Task 2: Path and query parameters
# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     TODO: Return user information

# @app.get("/search")
# def search(q: str, limit: int = 10):
#     TODO: Perform a search

# Task 3: POST endpoint with validation
# @app.post("/tasks", status_code=status.HTTP_201_CREATED)
# def create_task(task: Task):
#     TODO: Create and return a task

# Task 4: CRUD operations
# @app.get("/tasks/{task_id}")
# def get_task(task_id: int):
#     TODO: Retrieve a specific task

# @app.put("/tasks/{task_id}")
# def update_task(task_id: int, task: Task):
#     TODO: Update a task

# @app.delete("/tasks/{task_id}")
# def delete_task(task_id: int):
#     TODO: Delete a task

# Run with: uvicorn starter-code:app --reload
