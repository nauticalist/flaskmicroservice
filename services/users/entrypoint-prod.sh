#!/bin/sh

echo "Waiting for the database service..."

while ! nc -z users-db 5432; do
    sleep 0.1
done

echo "Database service started!"

gunicorn -b 0.0.0.0:5000 manage:app
