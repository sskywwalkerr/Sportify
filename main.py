import uvicorn
from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware

# from src.config import confing
# from src.app import routers
# from src.db.session import SessionLocal


app = FastAPI(
    title="SportifyFast",
    description="Author - Sky",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     responce = Response("Internal Server Error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#     finally:
#         request.state.db.close()
#     return response