1. Run python container: `docker run -it -p 8000:8000 python:3 /bin/bash`

2. Install Django: `pip3 install Django`

3. Create Django project: `django-admin startproject mysite`

4. Run application with gunicorn: `gunicorn --bind 0.0.0.0:8000 mysite.wsgi`
