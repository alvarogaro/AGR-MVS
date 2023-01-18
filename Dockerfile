FROM python:3.11-slim@sha256:4d091e6e8ea62ee443917ffa62106f08da104c133026bcc8f153a1db92fe27cd


WORKDIR /app/test


ENV VIRTUAL_ENV=/app/venv

RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install poetry


COPY pyproject.toml poetry.lock ./
RUN poetry install 

RUN chown -R 1001:1001 /app/


ENTRYPOINT ["poe","test"]





