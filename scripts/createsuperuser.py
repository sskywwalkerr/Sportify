from src.config import settings
from src.db.session import db_session
from src.app.user.service import user
from src.app.user.schemas import UserCreate

def main():
    """Создание супер юзера"""
    super_user = user.get_by_username(db_session, username=confing.SUPERUSER_NAME)
    if not super_user:
        user_in = UserCreate(
            username=confing.SUPERUSER_NAME,
            email=confing.SUPERUSER_EMAIL,
            password=confing.SUPERUSER_PASSWORD,
            first_name=confing.SUPERUSER_FIRST_NAME,
            is_superuser=True,
            is_active=True,
        )
        user.create(db_session, obj_in=user_in)

main()