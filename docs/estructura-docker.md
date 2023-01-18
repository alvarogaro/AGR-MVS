## Explicación Estructura Dockerfile.

* El contenedor que se va a montar para el Objetivo 5, es un contenedor enfocado al entorno de desarrollo,
por tanto se van a seguir una serie de pasos para su construcción.

* [Instalación de Poetry](https://python-poetry.org/docs#ci-recommendations): Para la instalación de poetry, tal y como podemos ver en la página oficial de poetry, se recomienda para los entornos de desarrollo que se use la última versión disponible. Siguiendo esto y las distintas maneras en las que ofrece como instalarlo (Mediante script, con pipx o con pip) Finalmente se va a optar por la instalación mediante pip, ya que es la forma donde se puede tener un mayor control de errores, y además evitamos la instalación de pipx en el contenedor. Siguiendo las instrucciones de instalación mediante pip. Se recomienda la instalación de poetry en un entorno virtual separado del entorno donde trabajamos, de manera que evitemos errores complejos en el caso en el que poetry actualice o desinstale sus propias dependencias.

* Uso y montaje del Entorno Virtual: Como hemos comentado en el primer punto, va a ser necesario crear un entorno virtual para la instalación de poetry mediante pip. La ruta donde situemos nuestro entorno virtual no es relevante, pero en mi caso, ya que el proyecto lo vamos a montar sobre /app, voy a situar el entorno virtual en /app/venv.

* Instalación Dependencias Poetry: Una vez instalado, vamos a proceder a instalar las dependencias, para ello simplemente vamos a ejecutar el comando poetry install, esto va a instalar todas las dependencias que tenemos configuradas.

* workdir y permisos: El directorio de trabajo que va a ser /app/test (Mediante workdir en caso de que no este creado, lo crea). Debido a que el usuario del runner de la Github action no es el mismo que el del contendor, vamos a tener que cambiar el propietario de la carpeta /app para que sea tanto del grupo como del usuario 1001, de manera que así a la hora de ejecutar el contenedor, como se va a hacer con el usuario 1001, este pueda tener permisos sobre la carpeta.