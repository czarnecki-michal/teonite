#!/bin/bash
cd ./scraper
python manage.py migrate
python manage.py makemigrations core
python manage.py migrate core
python manage.py download_stopwords
python manage.py insertdata
python manage.py runserver 0.0.0.0:8080