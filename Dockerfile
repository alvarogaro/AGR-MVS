FROM python:3.11-slim@sha256:4d091e6e8ea62ee443917ffa62106f08da104c133026bcc8f153a1db92fe27cd

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





