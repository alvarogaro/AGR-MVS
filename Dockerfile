FROM python:slim


ENV POETRY_HOME="/opt/poetry" \ 
    HOME="/app"                \         
    PATH="$POETRY_HOME/bin:$PATH"

RUN useradd -u 1001 alvarogaro

RUN pip install poetry 

COPY --chown=alvarogaro pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --no-root --no-ansi && rm ./pyproject.toml ./poetry.lock

WORKDIR /app/test
RUN chown -R alvarogaro /app
USER alvarogaro

ENTRYPOINT ["poe","test"]





