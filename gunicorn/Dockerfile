FROM python:3

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

RUN django-admin startproject mysite ./

ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:8000", "mysite.wsgi" ]
