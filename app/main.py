from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging

# from app.core.config import settings
# from app.core.logging import setup_logging
# from app.api.v1.router import api_router
# from app.db.session import init_db, close_db
# from app.observability.metrics import init_metrics
# from app.middlewares import register_middlewares


@asynccontextmanager
async def lifespan(app: FastAPI):
    # ---------- STARTUP ----------
    logging.info("aplication started")

    yield  # app is running

    # ---------- SHUTDOWN ----------
    # await close_db()
    logging.info("Application shut down")


def create_app() -> FastAPI:
    app = FastAPI(
        title="Ecomerce backend",
        version="1.0.0",
        lifespan=lifespan,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    register_middlewares(app)
    app.include_router(api_router, prefix="/api")

    return app


app = create_app()
