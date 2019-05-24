#!/bin/sh

echo "Waiting for database service..."

while ! nc -z users-db 5432; do
    sleep 0.1
done

echo "Database service started!"

python manage.py run -h 0.0.0.0

