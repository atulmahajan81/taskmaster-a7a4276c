from sqlalchemy.orm import selectinload

# Sample query using selectinload for eager loading
session.query(Task).options(selectinload(Task.categories)).filter(Task.user_id == user.id).all()