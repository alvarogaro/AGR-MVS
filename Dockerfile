FROM python:3.11-slim@sha256:39cecc9cde774f9209ad26a0ab2dc4f5d10ba92d2913a835cebea3b402af8e8b

# Configuración Poetry (https://python-poetry.org/docs#ci-recommendations)
ENV POETRY_VERSION=1.3.2
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETHEPOET_VERSION=0.18.0

RUN python3 -m venv $POETRY_VENV


RUN $POETRY_VENV/bin/pip install "poetry==$POETRY_VERSION"
RUN $POETRY_VENV/bin/pip install "poethepoet==$POETHEPOET_VERSION"


# Configuración de PATH 
ENV PATH="$POETRY_VENV/bin:$PATH"

COPY pyproject.toml poetry.lock ./

# Directorio de trabajo (En caso de que no esté creado se va a crear)
WORKDIR /app/test
RUN chown -R 1001:1001 /app

RUN poetry install  --no-interaction --no-ansi

ENTRYPOINT ["poe", "test"]





