from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Initialize FastAPI application
app = FastAPI(title="Book Management API", version="1.0.0")

# Define the Book model
class Book(BaseModel):
    title: str
    author: str
    isbn: str
    publication_year: int

# In-memory database (list of books)
books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "isbn": "978-0-7432-7356-5",
        "publication_year": 1925
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "isbn": "978-0-06-112008-4",
        "publication_year": 1960
    }
]

# TODO: Implement GET endpoint to retrieve all books
# Hint: Use @app.get("/books") decorator

# TODO: Implement GET endpoint to retrieve a book by ID
# Hint: Use @app.get("/books/{book_id}") decorator

# TODO: Implement POST endpoint to create a new book
# Hint: Use @app.post("/books") decorator

# TODO: Implement PUT endpoint to update a book by ID
# Hint: Use @app.put("/books/{book_id}") decorator

# TODO: Implement DELETE endpoint to remove a book by ID
# Hint: Use @app.delete("/books/{book_id}") decorator

# To run the API: uvicorn main:app --reload
