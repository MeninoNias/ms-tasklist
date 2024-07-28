import redis

from fastapi import FastAPI
from fastapi.routing import APIRoute

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from task.core.conf import settings

from task.api.main import api_router


# models.Base.metadata.create_all(bind=engine)

def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)


@app.on_event("startup")
async def startup():
    redis_client = redis.Redis(host="localhost", port=6379, db=0)
    FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")


app.include_router(api_router, prefix=settings.API_V1_STR)
