# API Reference

TaskMaster API provides endpoints for user authentication, task management, and more.

## Authentication

### Register a New User

- **URL**: `/api/v1/auth/register`
- **Method**: `POST`
- **Auth Required**: No
- **Request Body**:
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- **Response**:
  ```json
  {
    "id": "UUID",
    "email": "string"
  }
  ```

### Login a User

- **URL**: `/api/v1/auth/login`
- **Method**: `POST`
- **Auth Required**: No
- **Request Body**:
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- **Response**:
  ```json
  {
    "access_token": "string",
    "refresh_token": "string"
  }
  ```

## Task Management

### Create a Task

- **URL**: `/api/v1/tasks`
- **Method**: `POST`
- **Auth Required**: Yes
- **Request Body**:
  ```json
  {
    "title": "string",
    "description": "string",
    "due_date": "date",
    "priority": "string",
    "category_id": "UUID"
  }
  ```
- **Response**:
  ```json
  {
    "id": "UUID",
    "title": "string"
  }
  ```

### Retrieve a List of Tasks

- **URL**: `/api/v1/tasks`
- **Method**: `GET`
- **Auth Required**: Yes
- **Query Parameters**:
  - `page` (optional)
  - `limit` (optional)
  - `search` (optional)
- **Response**:
  ```json
  {
    "tasks": [
      {
        "id": "UUID",
        "title": "string",
        "due_date": "date",
        "priority": "string"
      }
    ]
  }
  ```