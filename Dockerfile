FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc && \
    pip install --no-cache-dir pipenv

COPY Pipfile Pipfile.lock ./
RUN pipenv install --deploy --system

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
