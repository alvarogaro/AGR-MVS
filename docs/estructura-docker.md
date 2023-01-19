## Explicación Estructura Dockerfile.

* El contenedor que se va a montar para el Objetivo 5, es un contenedor enfocado al entorno de desarrollo,
por tanto se van a seguir una serie de pasos para su construcción.

* Usuario: La imagen de docker escogida no tiene ningun usuario definido por tanto he creado un usuario llamado alvarogaro mediante el comando useradd -u 1001 alvarogaro. He tenido que asignarle el mismo UID que el usado para ejecutar el contenedor, ya que de lo contrario me da un error de permisos al acceder a la carpeta /app/.config/pypoetry/config.toml  

* [Instalación de Poetry](https://python-poetry.org/docs#ci-recommendations): Para la instalación de poetry, vamos a optar por la opción mas sencilla que funcione (buscando el PMV). En este caso, debido a que la imagen que hemos elegido, esta solo contiene lo necesario para ejecutar python, no tiene curl, wget ni herramienta por el estilo. Por contra, si tiene pip instalado y de las opciones que nos ofrece poetry para su instalación, pip es una de ellas, por tanto, con el fin de no añadir mas herramientas que luego no vamos a utilizar, vamos a optar por esta opción.

* Entorno Virtual: No vamos a hacer uso de ningun entorno virtual, ni para la instalación de poetry ni el que poetry crea a la hora de instalar las dependencias (se va a desactivar la opcion de crear entornos virtuales que tiene poetry), ya que realmente el hecho de estar en un contenedor es suficiente aislamiento y además puede funcionar sin necesidad de crear un entorno virtual por tanto nos lo podemos ahorrar. 

* Instalación Dependencias Poetry: Tras los pasos anteriores, poetry escribiría la cache en el raiz, por tanto luego a la hora de ejecutar el contenedor tendríamos problemas de permisos. Para solucionar esto se ha optado por crear un home para el usuario creado y así que poetry escriba la cache en este directorio. En caso contrario, habría que dar permisos al usuario sobre la carpeta /.cache.

* La instalación de las dependencias, debido a que no se va a crear un entorno virtual, se va a realizar en la carpeta /usr/local/bin/python3.11/site-packages y en /usr/local/bin, aunque se ejecute con la opción --no-root. Dar permisos al usuario creado sobre estas carpetas no lo veo conveniente por tanto estos comandos se ejecutan con el superusuario.

* El directorio de trabajo que va a ser /app/test (Mediante workdir en caso de que no este creado, lo crea). Para poder tener acceso a estar carpeta vamos a hacer uso del comando chown para poder dar permisos al usuario sobre la carpeta /app/ de manera recursiva, que además va a ser su home.