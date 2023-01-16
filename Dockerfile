FROM python:3.11-slim@sha256:39cecc9cde774f9209ad26a0ab2dc4f5d10ba92d2913a835cebea3b402af8e8b

# Configuración Poetry (https://python-poetry.org/docs#ci-recommendations)
ENV POETRY_VERSION=1.3.2

ENV VIRTUAL_ENV=/opt/poetry-venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN $VIRTUAL_ENV/bin/pip install "poetry==$POETRY_VERSION"
COPY pyproject.toml poetry.lock ./
RUN poetry install  

WORKDIR /app/test/
RUN chown -R 1001:1001 /app/

ENTRYPOINT [ "poe", "test" ]





