#!/bin/bash
set -e
set -x
cd ./scraper/ && \
    python manage.py download_stopwords && \
    python manage.py makemigrations core && \
    python manage.py migrate --no-input && \
    python manage.py insertdata && \
    python manage.py runserver 0.0.0.0:8080
