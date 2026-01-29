from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
import logging

from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi import HTTPException

from app.routes.api.v1 import api_router
from app.core.exceptions import CustomBusinessException


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("🚀 Application started")
    yield
    logging.info("🛑 Application shutdown")


app = FastAPI(
    title="Ecommerce Backend Application",
    description="Ecommerce backend application",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# ---------------- MIDDLEWARES ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- EXCEPTION HANDLERS ----------------

@app.exception_handler(CustomBusinessException)
async def business_exception_handler(
    request: Request,
    exc: CustomBusinessException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.code,
            "message": str(exc),
            "details": exc.details,
        },
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=422,
        content={
            "error": "VALIDATION_ERROR",
            "details": exc.errors(),
        },
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(
    request: Request,
    exc: HTTPException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": "HTTP_ERROR",
            "message": exc.detail,
        },
    )


@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):
    logging.exception(exc)  # VERY IMPORTANT
    return JSONResponse(
        status_code=500,
        content={
            "error": "INTERNAL_SERVER_ERROR",
            "message": "Something went wrong",
        },
    )

# ---------------- ROUTERS ----------------
app.include_router(api_router, prefix="/api")
