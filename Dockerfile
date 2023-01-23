FROM python:slim-bullseye
RUN useradd -m agr-mvs
RUN mkdir -p /app/test && chown -R agr-mvs /app/
USER agr-mvs
ENV POETRY_HOME="/home/agr-mvs/.local/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH" \
    HOME="/home/agr-mvs"

RUN pip install poethepoet poetry
ENV PATH="$HOME/.local/bin:$PATH"
WORKDIR /app/test
COPY --chown=agr-mvs pyproject.toml poetry.lock ./
RUN  poetry install && rm ./pyproject.toml ./poetry.lock


ENTRYPOINT ["poe","test"]









