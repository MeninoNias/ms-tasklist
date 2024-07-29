from select import select
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from task.models import Task
from . import schemas


def get_tasks(db: Session,
              search: str = None,
              skip: int = 0,
              limit: int = 10):
    query = select(Task)
    if search:
        query = query.where(
            or_(
                Task.title.contains(search),
                Task.description.contains(search)
            )
        )
    result = db.execute(query.offset(skip).limit(limit))

    return result.scalars().all()


def get_task(db: Session, task_id: int):
    statement = select(Task).where(Task.id == task_id)
    result = db.execute(statement)
    return result.scalar_one_or_none()


def create_task(db: Session, task: schemas.TaskCreate):
    db_task = Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(db: Session, task_id: int, task: schemas.TaskUpdate):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        if task.title is not None:
            db_task.title = task.title
        if task.description is not None:
            db_task.description = task.description
        if task.completed is not None:
            db_task.completed = task.completed
        db.commit()
        db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int):
    db_task = get_task(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task


def update_task_partial(db, task_id: int):
    db_task = get_task(db, task_id)
    if db_task:
        db_task.completed = True
        db.commit()
        db.refresh(db_task)
    return db_task
