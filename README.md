# Teonite blog scraper

Teonite blog scraper is an application which downloads informations about articles and their authors from `https://teonite.com/blog/` and presents them as stats via Django based REST API.

## Prerequisities
In order to run this application you need to install:
- [docker](https://docs.docker.com/install/)
- [docker-compose](https://docs.docker.com/compose/install/)

## Installation notes
1. Clone the repository `git clone https://gitlab.com/michal-czarnecki/recruitment-teonite.git`
2. Navigate to repository root directory.
3. In terminal run: `docker-compose up`.
4. Wait for docker to pull and build images.
5. After docker images are built scraping module is started and all gathered information is inserted into database.
6. When scraping is done, the application in accessible on `localhost:8080`

# General information
The application consists of two services:

## Django REST API with web-scraper module.

The application was created with **Django** and **Django REST Framework**. It accepts three types of requests:

### Request 
`GET /stats/` which returns top 10 used words and how much their occure in the blog.

`curl http://localhost:8080/stats/`
### Response
```
{
    "data": 172,
    "one": 151,
    "time": 147,
    ...
}
```
### Request 
`GET /stats/<author>` which returns top 10 used words per author and how much their occure in the blog.

`curl http://localhost:8080/stats/andrzejpiasecki`
### Response
```
{
    "image": 41,
    "neural": 21,
    "deep": 19,
    ...
}
```
### Request 
`GET /authors/` which returns authors of the blog posts and their id's.

`curl http://localhost:8080/authors`
### Response
```
{
    "jacekchmielewski": "Jacek Chmielewski",
    "martakoziel": "Marta Kozieł",
    "michalgryczka": "Michał Gryczka",
    ...
}
```

## Web-scraper module
Uses **BeautifulSoup** for website scraping and **Requests** libraries.
* The scraper connects to the blog website, 
* gets all available pages, then gets urls for all articles on each page and 
* returns a list with content of each article with it's author.
* After all the information about articles is collected `word_counter` is used.
* This module removes stopwords (like 'me', 'and', etc) and punctuation and calculates statictics for each article. 
* These statistics are calculated when user visits `/stats` or `/stats/<author>`.


## PostgreSQL database.

* Database is based on postgres docker image.
* There are two tables (based on django models) created by running django migrations:
    * `authors` - with two columns: `id` and `name`, with `id` being the primary key.
    * `articles` - with three columns: `id`, `text` and `author_id`, with `id` being the    primary key, `text` contains article's content and `author_id` is foreign key to `authors` table. 


It returns

| Route              | Method | Description                           |   |   |
|--------------------|--------|---------------------------------------|---|---|
| /stats/            | GET    | Get general stats                     |   |   |
| /stats/<author>/   | GET    | Get stats for specified author        |   |   |
| /authors           | GET    | Get all authors and their identifiers |   |   |