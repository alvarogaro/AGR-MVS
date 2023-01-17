FROM python:3.11-slim@sha256:4d091e6e8ea62ee443917ffa62106f08da104c133026bcc8f153a1db92fe27cd

# Configuración Poetry (https://python-poetry.org/docs#ci-recommendations)
ENV POETRY_VERSION=1.3.2


# Se define el Workdir (No es necesario hacer mkdir ya que lo crea si no está creado)
# Creo la carpeta home para definir el home del usuario que no estaba establecido
# Finalmente a la carpeta /app le doy tanto permisos para que sea del usuario y grupo 1001
WORKDIR /app/test
RUN mkdir -p /app/home
RUN chown -R 1001:1001 /app
USER 1001

# En esta parte vamos a definir la variable de entorno home con el home del usuario
# Vamos a montar el entorno virtual en la carpeta /app que es la que anteriormente hemos hecho que pertenezca al grupo y usuario 1001
ENV HOME=/app/home
ENV VIRTUAL_ENV=/app
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN $VIRTUAL_ENV/bin/pip install "poetry==$POETRY_VERSION"
COPY pyproject.toml poetry.lock ./
RUN poetry install  

ENTRYPOINT [ "poe", "test" ]





