FROM python:slim-bullseye

RUN useradd -m agr-mvs
RUN apt-get update && apt-get install -y curl
USER agr-mvs
ENV POETRY_HOME="/home/agr-mvs/.local/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH" \
    HOME="/home/agr-mvs"

RUN curl -sSL https://install.python-poetry.org | python3 - && pip install poethepoet

ENV PATH="/home/agr-mvs/.local/bin:$PATH"

WORKDIR /app/test

COPY --chown=agr-mvs pyproject.toml poetry.lock ./
RUN  poetry install --no-root --no-ansi 


ENTRYPOINT ["poe","test"]









