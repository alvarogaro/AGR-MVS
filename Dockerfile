FROM python:3.11-slim@sha256:39cecc9cde774f9209ad26a0ab2dc4f5d10ba92d2913a835cebea3b402af8e8b

# Configuración Poetry (https://python-poetry.org/docs#ci-recommendations)
ENV POETRY_VERSION=1.3.2
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv





