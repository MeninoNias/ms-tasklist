import factory

from task.models import Task


class TaskFactory(factory.Factory):
    class Meta:
        model = Task

    title = factory.Faker('text')
    description = factory.Faker('text')
