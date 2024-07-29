from fastapi import APIRouter, HTTPException, Query
from fastapi_cache.decorator import cache

from task import schemas, crud
from task.api.deps import SessionDep
from task.schemas import Message, TaskList

router = APIRouter()


@router.post("/", response_model=schemas.Task, status_code=201)
def create_task(db: SessionDep, task: schemas.TaskCreate):
    return crud.create_task(db=db, task=task)


@router.get('/', response_model=TaskList)
@cache(expire=60)
def list_task(  # noqa
        db: SessionDep,
        search: str = Query(None),
        skip: int = 0,
        limit: int = 100):
    return {"tasks": crud.get_tasks(db, search, skip, limit)}


@router.get("/{task_id}", response_model=schemas.Task)
@cache(expire=60)
def read_task(db: SessionDep, task_id: int):
    db_task = crud.get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.put("/{task_id}", response_model=schemas.Task)
def update_task(db: SessionDep, task: schemas.TaskUpdate, task_id: int):
    db_task = crud.update_task(db, task_id, task)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.patch("/{task_id}", response_model=schemas.Task)
def path_task(db: SessionDep, task_id: int):
    db_task = crud.update_task_partial(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.delete("/{task_id}", response_model=Message)
def delete_task(db: SessionDep, task_id: int):
    task = crud.delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return Message(message="Task has been deleted successfully.")
