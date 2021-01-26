FROM python:3.8-slim

RUN apt-get update \
    && apt-get install -y python-psycopg2

COPY ./app/ /app/
COPY requirements.txt /app/
RUN python -m pip install --upgrade pip; pip install -r /app/requirements.txt

ENV PYTHONIOENCODING=utf-8 \
    PYTHONUNBUFFERED=1

WORKDIR /app

EXPOSE 8000
# execute the app
CMD ["/usr/local/bin/gunicorn", "banzai.wsgi", "-b", "0.0.0.0:8000"]
