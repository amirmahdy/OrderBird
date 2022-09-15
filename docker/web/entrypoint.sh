#!/usr/bin/env bash

./manage.py collectstatic --noinput
./manage.py migrate
./manage.py loaddata app/fixtures/*.json

exec "$@"