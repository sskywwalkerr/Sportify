import os
from .local_config import *

PROJECT_NAME = "Sportify"
SERVER_HOST = "http://127.0.0.1:8000"


# Secret key
SECRET_KEY = b"oaisuhdfoi32yriudhqwlefguui3"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

API_V1_STR = "/api/v1"

# Token = 8 days
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

EMAILS_FROM_NAME = PROJECT_NAME
EMAIL_RESET_TOKEN_EXPIRE_HOURS = 48
EMAIL_TEMPLATES_DIR = "src/email-templates/build"
EMAIL_ENABLED = SMTP_HOST and SMTP_PORT and EMAILS_FROM_EMAIL
EMAIl_TEST_USER = "sky@gmail.com"

# SUPERUSER_NAME = "Sky"
# SUPERUSER_EMAIL = "Sky@mail.ru"
# SUPERUSER_PASSWORD = "272371rad"
# SUPERUSER_FIRST_NAME = "Sky"
# USERS_OPEN_REGISTRATION = True
