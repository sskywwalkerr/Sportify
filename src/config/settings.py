import os
from .local_config import *



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

API_V1_STR = "/api/v1"

# Token
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8

# Cors
BACKEND_CORS_ORIGINS = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:3000",
    "http://localhost:8000",
]

# DB
SQLALCHEMY_DATABASE_URI =(
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"
)

USERS_OPEN_REGISTRATION = True