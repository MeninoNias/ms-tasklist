from typing import Optional

from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    title: str
    description: str


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class Task(TaskBase):
    id: int
    completed: bool

    model_config = ConfigDict(from_attributes=True)


class TaskList(BaseModel):
    tasks: list[Task]


# Generic message
class Message(BaseModel):
    message: str
