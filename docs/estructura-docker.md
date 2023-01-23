## Explicación Estructura Dockerfile.

* El contenedor que se va a montar para el Objetivo 5, es un contenedor enfocado al entorno de desarrollo,
por tanto se van a seguir una serie de pasos para su construcción.

* Usuario: La imagen docker escogida para el contenedor, tras revisar su dockerfile, se ha visto que no tiene ningún usuario no privilegiado asignado por defecto, por lo que vamos a crear un usuario no privilegiado para el contenedor [issue](https://github.com/alvarogaro/AGR-MVS/issues/40) 

* Cuando hemos creado el usuario no privilegiado por defecto se le va a asignar un HOME. Este home, en caso de que hagamos RUN echo $HOME, podemos ver que se encuentra en /home/agr-mvs.

* El caso es que si queremos no definir una variable HOME y usarla en el resto del dockerfile lo que sucede es que por ejemplo al utilizarla en cualquier otra variable ENV, no nos la va a detectar, dándonos por tanto problemas en los PATH que tenemos definidos. 

* Este problema, tanto en el manual de [docker] (https://docs.docker.com/engine/reference/builder/#user), como en el siguiente [ejemplo](https://stackoverflow.com/questions/28966198/dockerfile-home-is-not-working-with-add-copy-instructions), se puede ver como el HOME que se define para el usuario no privilegiado solo va a ser conocido cuando se ejecuten sentencias tales como RUN, ENTRYPOINT o CMD. Ya que estas sentencias van a abrir un nuevo shell dentro del contenedor, que es modificado por el USER. 

* Con el fin de no complicar mas el dockerfile, y que todas las directivas tengan un conocimiento del HOME del usuario, la mejor opción sería la de dejar definida la variable de entorno HOME



* [Instalación de Poetry](https://python-poetry.org/docs#ci-recommendations): De las diferentes opciones que nos ofrece Poetry para su instalación, vamos a optar por la instalación mediante curl y el script de instalación. Mediante el script siempre vamos a tener disponible la última versión de poetry y la herramienta curl, pese a que en el dockerfile de la imagen base escogida lo instala, posteriormente lo desinstala por lo que vamos a instalar curl mediante permisos de superusuario [issue](https://github.com/alvarogaro/AGR-MVS/issues/31). Como se comenta en el issue debido a que la instalación se hace sobre un directorio del usuario ( Esta instalación la estamos haciendo con el usuario no privilegiado que hemos creado), vamos a especificar mediante la variable POETRY_HOME el lugar donde queremos que se realice la instalación. 

* Seguidamente vamos a añadir al PATH, la ruta donde se encuentra poetry y el home del usuario.

* Ahora una vez que tenemos definidas todas las rutas vamos a proceder con la instalación. La cual se va a realizar en el directorio /home/"nombre_usuario"/.local/poetry/bin.

* La instalación de poethepoet mediante poetry ha generado algunos problemas de rutas de solución compleja por lo que finalmente se ha optado por instalarlo por separado mediante pip, y añadir su ruta al PATH. [issue](https://github.com/alvarogaro/AGR-MVS/issues/42) 

* Seguidamente se ha establecido el WORKDIR en /app/test

* Ahora se procede a copiar los ficheros necesarios para la instalación de las dependencias mediante poetry, para ello hacemos un COPY pero asignando los permisos con --chown de los ficheros a nuestro usuario.

* A la hora de eliminar estos ficheros del contenedor, pese a copiarlos con permisos de usuario no he podido eliminarlos debido a un error de permisos. 

* Este error se debe a que cuando se ejecuta el comando WORKDIR lo va a hacer con los permisos de root, por tanto al no tener permisos sobre el directorio no nos va a permitir borrar los ficheros. Con el fin de solucionar esto lo que se ha hecho ha sido al principio del Dockerfile, crear la carpeta /app/test como root y cambiar el propietario de manera recursiva de la carpeta /app a nuestro usuario no privilegiado.

* Una vez copiados, se procede a instalar las dependencias. Para la instalación se ha dejado que poetry genere su entorno virtual por defecto, ya que al ser una instalación sin privilegios, en caso de que queramos desactivar la opción de crear un entorno virtual, pese a hacerlo con la opción --no-root, nos daría problemas de permisos, ya que intentaría instalar sobre /usr/local/lib/pythonX.X/site-packages, Directorio sobre el cual no tenemos permisos.[issue](https://github.com/alvarogaro/AGR-MVS/issues/30)

