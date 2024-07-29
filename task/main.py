import logging
from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi_cache.decorator import cache
from redis import asyncio as aioredis

from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from task.api.main import api_router
from task.core.conf import settings

logging.basicConfig(level=logging.DEBUG)


# models.Base.metadata.create_all(bind=engine)

def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    try:
        redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}")
        FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
        yield
        logging.info("Cache initialized successfully.")
    except Exception as e:
        logging.error(f"Error initializing cache: {e}")

    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
    lifespan=lifespan
)


@cache()
async def get_cache():
    return 1


app.include_router(api_router, prefix=settings.API_V1_STR)
