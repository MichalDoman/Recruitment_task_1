FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

RUN apt-get update \
    && apt-get install -y --no-install-recommends mongodb-clients \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/

EXPOSE 8000

RUN python manage.py collectstatic --noinput

CMD ["service", "mongod", "start"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
