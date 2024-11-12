import uvicorn
from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from src.config import settings
from src.app import routers
from src.db.session import SessionLocal


app = FastAPI(
    title="Fast",
    description="Author-Sky",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    responce = Response("Internal Server Error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(routers.api_router, prefix=settings.API_V1_STR)


# register_tortoise(
#     app,
#     db_url="postgresql://postgres:postgres@127.0.0.1:5432/postgres",
#     modules={"models": ["src.models", "aerich.models"]},
#     generate_schemas=True,
#     add_exception_handlers=True,
# )
