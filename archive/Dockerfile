FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /code
ADD requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "mysite/manage.py", "runserver", "0.0.0.0:8000"]