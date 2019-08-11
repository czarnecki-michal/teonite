FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
    apt-get autoremove -y && \
    mkdir -p /scraper
WORKDIR /scraper
ADD /requirements.txt /scraper/
RUN pip install -r requirements.txt
ADD . /scraper/
EXPOSE 8000
RUN chmod +x ./entrypoint.sh
CMD [ "./entrypoint.sh" ]