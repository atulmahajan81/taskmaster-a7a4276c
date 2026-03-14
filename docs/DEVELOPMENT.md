# Development Guide

## Local Development Setup

1. **Clone the Repository**
   
   ```bash
   git clone https://github.com/yourusername/taskmaster.git
   cd taskmaster
   ```

2. **Install Dependencies**

   - Backend: Navigate to the backend directory and install dependencies.
     
     ```bash
     cd backend
     pip install -r requirements.txt
     ```

   - Frontend: Navigate to the frontend directory and install dependencies.
     
     ```bash
     cd frontend
     npm install
     ```

3. **Run Services with Docker**

   ```bash
   docker-compose up
   ```

## Running Tests

- To run backend tests:
  
  ```bash
  cd backend
  pytest
  ```

- To run frontend tests:
  
  ```bash
  cd frontend
  npm test
  ```

## Code Structure

- **Backend**: Contains the API services, models, and business logic.
- **Frontend**: Houses all the UI components, pages, and state management.

## Contributing Guide

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test thoroughly.
4. Submit a pull request with a detailed description of your changes.