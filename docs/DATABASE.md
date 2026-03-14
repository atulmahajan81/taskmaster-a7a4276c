# Database Guide

## Schema Overview

TaskMaster utilizes PostgreSQL as its primary database. Below is a simplified schema overview:

- **Users**: Stores user details and authentication information.
- **Tasks**: Stores task details, including title, description, due date, and priority.
- **Categories**: Manages task categorization.

## Entity Relationships

- **Users** have many **Tasks**.
- **Tasks** belong to a **Category**.

## Migration Guide

1. **Create a New Migration**
   
   Navigate to the backend directory and run:
   
   ```bash
   alembic revision --autogenerate -m "Migration message"
   ```

2. **Apply Migrations**
   
   ```bash
   alembic upgrade head
   ```