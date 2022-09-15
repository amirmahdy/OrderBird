#!/usr/bin/env bash

./manage.py collectstatic --noinput
./manage.py migrate

exec "$@"