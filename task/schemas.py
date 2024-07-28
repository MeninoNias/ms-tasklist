from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    title: str
    description: str


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    completed: bool


class Task(TaskBase):
    id: int
    completed: bool

    model_config = ConfigDict(from_attributes=True)


class TaskList(BaseModel):
    tasks: list[Task]


# Generic message
class Message(BaseModel):
    message: str
