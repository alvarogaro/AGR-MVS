# Elección Gestor De Dependencias

* Como hemos planteado en el issue [#12](https://github.com/alvarogaro/AGR-MVS/issues/12), va a ser necesario la elección de un gestor de dependencias para nuestro proyecto, esto es necesario ya que un gestor de dependencias nos va a permitir tener un proyecto con una mayor previsibilidad, sostenibilidad a lo largo del tiempo y seguridad.

* Para la elección de nuestro gestor de dependencias, tenemos que basarnos en criterios objetivos y de las mejores prácticas del lenguaje que estemos utilizando en nuestro proyecto.

* En nuestro caso, el lenguaje que vamos a utilizar es Python, por lo tanto las mejores prácticas y los criterios objetivos que sigue la comunidad vienen recogidos en los denominados PEP (Python Enhancement Proposals), [Enlace a los PEP](https://peps.python.org/).

* En concreto, estamos tratando ahora la gestión de dependencias, por tanto vamos a seguir las recomendaciones que vienen recogidas en los PEP [517](https://peps.python.org/pep-0517/), [518](https://peps.python.org/pep-0518/) y [621](https://peps.python.org/pep-0621).

## Comparativa Gestores De Dependencias.

* En este apartado vamos a hacer una comparativa de los gestores de dependencias que se comentan en el issue #12 teniendo en cuenta los criterios de los PEP mencionados anteriormente.

* Hatch: Analizando su [documentación oficial](https://hatch.pypa.io/latest/intro/) vemos que cumple los PEP mencionados anteriormente

* Poetry: Gestor de dependencias, igual que como hemos hecho con Hatch, vemos que cumple los PEP mencionados anteriormente.


## Poetry vs Hatch


* Poetry: En esta siguiente comparativa nos vamos a basar en su análisis en Snyk podemos ver que tiene una puntuación de 97, una gran popularidad y un mantenimiento activo.

* Hatch: Viendo su análisis en Snyk, podemos ver que es un proyecto con un mantenimiento activo y con bastante popularidad aunque mucho menor que poetry(Puntuación en Snyk de 85) . 


## Conclusión

* Finalmente, tanto Hatch como Poetry son dos Gestores de Dependencias que nos van a servir perfectamente para nuestro proyecto y que cumplen con los PEP mencionados anteriormente. Sin embargo me voy a decantar por Poetry simplemente por que tiene una mayor puntuación en Snyk y por su capacidad de poder integrarse con gestores de Tareas como PoethePoet.