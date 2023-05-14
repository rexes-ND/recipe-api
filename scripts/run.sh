#!/bin/sh

set -e # one fail -> whole script fail

python manage.py wait_for_db

# collect all static files and put them in the configured static files dir.
python manage.py collectstatic --noinput 
python manage.py migrate

# --socket :9000 -> TCP socket on port 9000
# --workers 4 -> 4 different WSGI workers
# --master -> Set the WSGI daemon as the master thread
# --enable-threads -> Allow multithreading
# --module -> Run ./app/app/wsgi.py (No need to specify .py)
uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi
