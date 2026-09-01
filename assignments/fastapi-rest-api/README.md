# 🚀 Building REST APIs with FastAPI

## 🎯 Objective

Create a complete REST API for managing a collection of books using the FastAPI framework. You'll learn to build endpoints, handle HTTP methods, validate data, and work with request/response models.

## 📝 Tasks

### 🛠️ Create Basic API Endpoints

#### Description
Set up a FastAPI application with endpoints to retrieve and create books. Start with in-memory storage and basic routing.

#### Requirements
Completed program should:

- Initialize a FastAPI application
- Create a GET endpoint to list all books
- Create a GET endpoint to retrieve a specific book by ID
- Create a POST endpoint to add a new book
- Return appropriate HTTP status codes (200, 201, 404)


### 🛠️ Implement Data Validation and Models

#### Description
Use Pydantic models to validate incoming data and ensure type safety throughout your API.

#### Requirements
Completed program should:

- Define a Book model with title, author, isbn, and publication_year fields
- Validate that ISBN is a non-empty string
- Validate that publication_year is a positive integer
- Return clear error messages when validation fails
- Use consistent model structure for all API responses


### 🛠️ Add Update and Delete Operations

#### Description
Implement full CRUD operations by adding endpoints to update existing books and delete books from the collection.

#### Requirements
Completed program should:

- Create a PUT endpoint to update an existing book by ID
- Create a DELETE endpoint to remove a book by ID
- Handle cases when a book ID doesn't exist
- Preserve data consistency across all operations
- Return appropriate confirmation messages for successful operations


### 🛠️ Advanced: Add Query Parameters and Filtering

#### Description
Enhance your API with filtering capabilities to retrieve books by author or publication year.

#### Requirements
Completed program should:

- Add optional query parameters to the list endpoint (author, year)
- Filter books based on provided query parameters
- Support filtering by multiple criteria simultaneously
- Return an empty list when no matches are found
- Document query parameters in the API documentation
