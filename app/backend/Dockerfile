FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app/

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

ENV PYTHONPATH=/app

COPY ./app/pyproject.toml ./app/poetry.lock* /app/ 

RUN poetry install --no-root 

RUN alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000 --reload

