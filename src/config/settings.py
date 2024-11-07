import os
from .local_config import *

from envparse import Env

env = Env()

PROJECT_NAME = "Sportify"
SERVER_HOST = 'http://127.0.0.1:8000'


# Secret key
SECRET_KEY = b"oaisuhdfoi32yriudhqwlefguui3"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

API_V1_STR = "/api/v1"

# Token
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7

# Cors
BACKEND_CORS_ORIGINS = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:3000",
    "http://localhost:8000",
]

SQLALCHEMY_DATABASE_URI = (
    "postgresql://postgres:postgres@127.0.0.1:5432/postgres"
) # connect string for the database
APP_PORT = default = 8000
# SQLALCHEMY_DATABASE_URI = env.str(
#     "REAL_DATABASE_URL",
#     default="postgresql://postgres:postgres@127.0.0.1:5432/postgres"
# )

# SQLALCHEMY_DATABASE_URI = (
#     f'postgresql://{os.environ["POSTGRES_USER"]}:'
#     f'{os.environ["POSTGRES_PASSWORD"]}@'
#     f'{os.environ["POSTGRES_HOST"]}/'
#     f'{os.environ["POSTGRES_DB"]}'
# )

USERS_OPEN_REGISTRATION = True

EMAILS_FROM_NAME = PROJECT_NAME
EMAIL_RESET_TOKEN_EXPIRE_HOURS = 48
EMAIL_TEMPLATES_DIR = "src/email-templates/build"
EMAILS_ENABLED = SMTP_HOST and SMTP_PORT and EMAILS_FROM_EMAIL
EMAIl_TEST_USER = "rysaev.ryss@gmail.com"
# DB
# SQLALCHEMY_DATABASE_URI =(
#     f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"
# )
# SUPERUSER_NAME = "Sky"
# SUPERUSER_EMAIL = "Sky@mail.ru"
# SUPERUSER_PASSWORD = "272371rad"
# SUPERUSER_FIRST_NAME = "Sky"
# USERS_OPEN_REGISTRATION = True
