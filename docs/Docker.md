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

* [python:version-bullseye](https://hub.docker.com/_/python/tags?page=1&name=bullseye): Son imágenes basadas también en Debian11 pero con una tamaño mucho mas considerables ya que tienen muchas características adicionales del SO. En este caso el tamaño promedio de una imagen es de 330Mb, contienen muchas mas características de las necesarias para nuestra aplicación.


## Imágenes no oficiales de Python

Encontramos otras imágenes docker que no son oficiales, son imágenes creadas por empresas o por usuarios. Buscando python dentro del buscador de [dockerhub](https://hub.docker.com/search?q=python) podemos encontrar algunas imagenes verificadas como por ejemplo: 

* [circleci/python](https://hub.docker.com/r/circleci/python): Son una serie de imágenes docker que estan recomendadas principalmente para usuarios que buscan crear una imagen muy específica para su proyecto. Tienen un tamaño promedio de 1.00 Gb.

* [bitnami/python](https://hub.docker.com/r/bitnami/python): Imagen de python creada por la empresa Bitnami. Estas imágenes estan bajo el soporte de la empresa de manera que cualquier bug o fallo tienen soporte. Estan basadas en una distribución Debian-slim para que el peso sea el menor posible. El tamaño promedio de estas imágenes es de 200.98 Mb. 

* Estas imágenes como podemos ver, en comparación con algunas oficiales ( por ejemplo la slim), tienen un tamaño muy superior, por lo que no van a ser seleccionadas.


## Conclusion

* Finalmente tras evaluar las distintas opciones y viendo los requerimientos que tenemos nuestro proyecto. Vamos a elegir la imagen slim de python, ya que es la de tamaño mas reducido que cumple con todos los requisitos que necesitamos. Respecto a la versión de python que vamos a utilizar, nuestro proyecto depende de poethepoet, pytest y poetry. Tanto pytest como poetry como poethepoet funcionan con python 3.7 o superior.

* Por tanto vamos a usar la versión latest de [python-slim](https://hub.docker.com/layers/library/python/slim/images/sha256-2415bc113b5cdc232dfed6f29a029adad8c9440442fdc63598d6c83a91fa573c?context=explore). Una imagen que contiene los paquetes mínimos para ejecutar python.








