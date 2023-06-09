FROM python:3.9-slim-buster

COPY Pipfile .
COPY Pipfile.lock .

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && pip install --upgrade pip \
    && pip install pipenv \
    && pipenv install --system --deploy --ignore-pipfile

COPY . .

# Copy the .env.example file and rename it to .env
COPY .env.example .env

CMD ["uvicorn", "service:deploy_local_app", "--port", "8000", "--host", "0.0.0.0"]
