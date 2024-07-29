from sqlalchemy import select

from task import crud
from task.models import Task
from task.schemas import TaskCreate


def test_create_task(session):
    new_task = TaskCreate(title='new_task_111111111111', description='secret')
    new_task = crud.create_task(session, new_task)

    task = session.scalar(select(Task).where(Task.title == 'new_task_111111111111'))

    assert task.title == 'new_task_111111111111'


def test_read_task(session):
    new_task_1 = TaskCreate(title='new_task_1', description='secret')
    new_task_1 = crud.create_task(session, new_task_1)
    new_task_2 = TaskCreate(title='new_task_2', description='secret')
    new_task_2 = crud.create_task(session, new_task_2)

    tasks = crud.get_tasks(session)
    assert len(tasks) >= 2
