# Стек:
# Python >= 3.12
# FastAPI >= 0.115.2
# Tortoise ORM
# Postgres

#### 1) Создать образ

    docker-compose build

#### 2) Запустить контейнер

    docker-compose up

#### 3) Перейти по адресу

    http://127.0.0.1:8000/docs

#### 4) Создать миграции 

    docker exec -it SportifyFast-back poetry run alembic upgrade head

#### 5) Создать суперюзера

    docker exec -it SportifyFast-back python scripts/createsuperuser.py

#### 6) Если не выполняет команды 

-Войти в контейнер - docker exec -it SportifyFast-back bash
-Выполнить команды без docker exec -it SportifyFast-back

#### 7) Если нужно очистить бд 

    docker-compose down -v

