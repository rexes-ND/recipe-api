# 1. Create user app
```
docker compose run --rm app python manage.py startapp user
```
# 2.1. Remove files and folders
```
user/migrations/ # All migration in the core app
models.py        # All models in the core app
admin.py
tests.py         # tests/ subdirectory is created instead
```
# 2.2. Add files and folders
```
tests/
tests/__init__.py
```
# 3. Add `app` to list of app(s) of the project
```
# settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'rest_framework',
    'drf_spectacular',
    'user',
]

```

# 4. Define UserSerializer in `app/user/serializers.py`

# 5. Create url mapping in `app/user/urls.py` to UserSerializer

# 6. Create url mapping in `app/app/urls.py` to `app/user/urls.py`
