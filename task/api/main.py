from fastapi import APIRouter

from task.api.routes import tasks

api_router = APIRouter()
api_router.include_router(tasks.router, tags=["tasks"])
