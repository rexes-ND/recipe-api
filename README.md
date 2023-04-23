# recipe-api

## Creating a new Django project
```
docker compose run --rm app django-admin startproject app . # Usage: django-admin startproject name [directory]
```

## Linting 
```
docker compose run --rm app flake8
```

## Docker
```
docker login -u {DOCKERHUB_USER}
```