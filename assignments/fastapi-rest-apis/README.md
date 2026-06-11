# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build production-ready REST APIs using the FastAPI framework. You'll create endpoints to handle HTTP requests, manage data with path and query parameters, and implement proper request validation and response models.

## 📝 Tasks

### 🛠️ Create Your First FastAPI Application

#### Description
Set up a basic FastAPI application with a simple GET endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance
- Define a root GET endpoint (`/`) that returns a JSON response with a welcome message
- Run the server using `uvicorn` and verify it works
- Example output: `{"message": "Welcome to the FastAPI Tutorial!"}`

### 🛠️ Build Endpoints with Path and Query Parameters

#### Description
Create multiple endpoints that accept user input through path parameters and query strings.

#### Requirements
Completed program should:

- Create a GET endpoint `/users/{user_id}` that returns user information based on the ID
- Create a GET endpoint `/search` that accepts optional query parameters like `q` (search query) and `limit` (number of results)
- Return JSON responses with the appropriate parameters
- Handle edge cases (e.g., invalid user IDs, missing parameters)

### 🛠️ Implement POST Requests and Data Validation

#### Description
Create an endpoint that accepts POST requests with JSON data and validates the input using Pydantic models.

#### Requirements
Completed program should:

- Define a Pydantic model for a task/item with fields like `name`, `description`, and `completed`
- Create a POST endpoint `/tasks` that accepts JSON data and returns the created task with an ID
- Use automatic validation to ensure required fields are present
- Return appropriate HTTP status codes (201 for creation)

### 🛠️ Build a Complete CRUD API

#### Description
Expand your API to support Create, Read, Update, and Delete operations on a resource.

#### Requirements
Completed program should:

- Implement GET `/tasks/{task_id}` to retrieve a specific task
- Implement PUT `/tasks/{task_id}` to update a task
- Implement DELETE `/tasks/{task_id}` to remove a task
- Store tasks in memory (a simple list or dictionary)
- Return 404 responses when tasks don't exist
