import logging
from contextlib import asynccontextmanager

import redis
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
async def lifespan(app: FastAPI):
    # Inicializa o cliente Redis
    try:
        redis_client = redis.Redis(host="localhost", port=6379, db=0)
        FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")
        logging.info("Cache initialized successfully.")
    except Exception as e:
        logging.error(f"Error initializing cache: {e}")

    # Yield para manter a aplicação viva
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
    lifespan=lifespan
)

app.include_router(api_router, prefix=settings.API_V1_STR)
