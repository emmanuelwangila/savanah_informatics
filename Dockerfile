FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt


COPY . /app/

ENV DJANGO_SETTINGS_MODULE=savanah_informatics.settings


RUN python manage.py collectstatic --noinput

# Use gunicorn to serve the app
CMD ["gunicorn", "savanah_informatics.wsgi:application", "--bind", "0.0.0.0:8000"]
