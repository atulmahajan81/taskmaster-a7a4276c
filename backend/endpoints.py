from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import get_db

router = APIRouter()

@router.get('/tasks', response_model=List[Task])
def list_tasks(user_id: str, offset: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tasks = db.query(Task).filter(Task.user_id == user_id).offset(offset).limit(limit).all()
    return tasks