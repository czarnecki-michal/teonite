FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /scraper
WORKDIR /scraper
ADD scraper/requirements.txt /scraper/
RUN pip install -r requirements.txt
ADD . /scraper/