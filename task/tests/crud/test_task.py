from sqlalchemy import select
from task.models import Task


def test_create_task(session):
    new_task = Task(title='alice', description='secret')
    session.add(new_task)
    session.commit()

    task = session.scalar(select(Task).where(Task.title == 'alice'))

    assert task.title == 'alice'
