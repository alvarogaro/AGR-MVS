FROM python:3.11-slim@sha256:4d091e6e8ea62ee443917ffa62106f08da104c133026bcc8f153a1db92fe27cd


WORKDIR /app/test

ENV HOME=/app
ENV POETRY_HOME="/opt/poetry"

ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apt-get update \
    && apt-get install -y curl \
    && curl -sSL https://install.python-poetry.org | python3 -

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-ansi

RUN chown -R 1001:1001 /app
USER 1001

ENTRYPOINT ["poe","test"]





