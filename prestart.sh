#! /usr/bin/env_bash

# Let the DB start
#sleep 10
#
#poetry run alembic revision --autogenerate

sleep 10
# Run migrations
poetry run alembic upgrade head