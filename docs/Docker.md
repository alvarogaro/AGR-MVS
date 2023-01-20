# Imagen Docker Proyecto

* Para la elección de la imagen del contenedor de Docker vamos a tener en cuenta una serie de criterios en base a las mejores prácticas relacionadas con el empaquetamiento de imágenes Docker para python.[Mejores prácticas Docker](https://snyk.io/blog/best-practices-containerizing-python-docker/). Los criterios que vamos a seguir son: 

* Tamaño de la Imagen: Siguiendo las mejores prácticas vamos a tener en cuenta como un requisito fundamental el elegir la imagen con menor tamaño posible que nos proporcione todas nuestros requerimientos. De esta manera vamos a tener una mayor velocidad de descargar de la imagen, menor uso de recursos y por tanto mayor rapidez y contendrá también menos vulnerabilidades.

* Dependencias: Debemos de buscar una imagen de docker que nos permita instalar las dependencias que necesitemos para nuestro proyecto. Por tanto buscaremos una imagen que tenga acceso a gran cantidad de librerías.

* En base a estos 2 criterios anteriormente comentados vamos a comparar una serie de opciones: 

## Imágenes Oficiales de Python

* En primer lugar vemos que tenemos imágenes oficiales de docker para python, buscando tanto en snyk el paquete python como en docker hub, podemos ver algunas alternativas. Entre las cuales destacan las siguientes:

* [python:version-slim](https://hub.docker.com/_/python/tags?page=1&name=slim): Esta imagen tiene un tamaño de 45Mb. es una imagen basada en debian pero con un tamaño muy reducido.

* [python:version](https://hub.docker.com/_/python): Esta imagen no nos conviene ya que tiene un tamaño muy superior al resto de imágenes, ademas de tener muchos mas requisitos de los que necesitamos.

* [python:version-alpine](https://hub.docker.com/_/python/tags?page=1&name=alpine): Esta es una imagen basada en Alpine Linux Project, sistema construido específicamente para su uso en contenedores. Es una muy buena opción en caso de que solo tuvieramos el espacio como requisito fundamental ya que esta version es la mas liviana que se puede encontrar, teniendo un tamaño en torno a los 20 Mb. Por contra, no solo tenemos como criterio el espacio, sino que tambien tenemos en cuenta otros factores como las dependencias. Respecto a esto, esta imagen no es muy recomendable ya que este sistema utiliza musl lib en lugar de glibc, por lo que podemos encontrarnos con problemas de compatibilidad con algunas librerías de python, al igual que con largos tiempos de compilación y bugs. Por tanto se va a preferir las versiones slim y debian-slim ante estas versiones.[Problemas Alpine Python](https://pythonspeed.com/articles/alpine-docker-python/)

* [python:slim-bullseye](https://hub.docker.com/_/python/tags?page=1&name=bullseye): Son imágenes basadas también en Debian11 y con un tamaño promedio de 45Mb. Son imágenes slim que contienen el sistema operativo y las herramientas necesarias para ejecutar python.


## Sistemas Operativos

* Encontramos otras imágenes docker que no son oficiales, son imágenes creadas por empresas o por usuarios. Buscando python dentro del buscador de [dockerhub](https://hub.docker.com/search?q=python) podemos encontrar algunas imagenes verificadas como por ejemplo: 

* [circleci/python](https://hub.docker.com/r/circleci/python): Son una serie de imágenes docker que estan recomendadas principalmente para usuarios que buscan crear una imagen muy específica para su proyecto. Tienen un tamaño promedio de 1.00 Gb. Un tamaño muy grande por tanto no va a ser seleccionada.

* [bitnami/python](https://hub.docker.com/r/bitnami/python): Imagen de python creada por la empresa Bitnami. Estas imágenes estan bajo el soporte de la empresa de manera que cualquier bug o fallo tienen soporte. Estan basadas en una distribución Debian-slim para que el peso sea el menor posible. El tamaño promedio de estas imágenes es de 200.98 Mb. Por tanto va a tener un tamaño muy grande con una cantidad de herramientas que no vamos a usar

* [debian:stable-slim](https://hub.docker.com/layers/library/debian/stable-slim/images/sha256-9554f6caf2cafc99ad9873a822e1aafbb29d40608fe7ebe6569365b80fa5a422?context=explore): Sistema operativo Debian 11, basado en Debian 11. Tienen un tamaño promedio de 29.94Mb. Tiene un tamaño bastante reducido y al ser la versión slim va a tener muy pocas herramientas instaladas por defecto.



## Conclusion

* Se han comparado las distintas imágenes. Principalmente las mejores opciones  son la imagen [debian:stable-slim](https://hub.docker.com/layers/library/debian/stable-slim/images/sha256-9554f6caf2cafc99ad9873a822e1aafbb29d40608fe7ebe6569365b80fa5a422?context=explore) y [python:slim-bullseye](https://hub.docker.com/_/python/tags?page=1&name=bullseye) Entre estas dos opciones, de base vamos a tener una diferencia de 20 MB en peso y realmente en caso de escoger la imagen [debian:stable-slim](https://hub.docker.com/layers/library/debian/stable-slim/images/sha256-9554f6caf2cafc99ad9873a822e1aafbb29d40608fe7ebe6569365b80fa5a422?context=explore)4, cuando se instale va a a tener un tamaño parecido por lo que no hay una diferencia muy grande. Finalmente voy a optar por escoger la imagen oficial [python:slim-bullseye](https://hub.docker.com/_/python/tags?page=1&name=bullseye). En concreto voy a coger la versión latest ya que estamos en un entorno de desarrollo. 







