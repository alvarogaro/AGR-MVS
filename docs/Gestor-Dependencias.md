# Elección Gestor De Dependencias

* Como hemos planteado en el issue [#12](https://github.com/alvarogaro/AGR-MVS/issues/12), vamos a elegir un gestor de dependenciar

* Para la elección de nuestro gestor de dependencias, vamos a seguir una serie de criterios que  vienen recogidos en los denominados PEP (Python Enhancement Proposals), [Enlace a los PEP](https://peps.python.org/).

* En concreto, estamos tratando ahora la gestión de dependencias, por tanto vamos a seguir las recomendaciones que vienen recogidas en los PEP [517](https://peps.python.org/pep-0517/), [518](https://peps.python.org/pep-0518/) y [621](https://peps.python.org/pep-0621) además de contemplar la posibilidad de que puedan compartir fichero con el gestor de tareas.
  
* Adicionalmente a los criterios anteriormente mencionados, vamos a tener en cuenta el análisis que se hace  de estos gestores en [Synk](https://snyk.io/), en concreto nos vamos a fijar en su puntuación global, popularidad y mantenimiento.

## Comparativa Gestores De Dependencias.

* En este apartado vamos a hacer una comparativa de los gestores de dependencias que se comentan en el issue #12 teniendo en cuenta los criterios de los PEP mencionados anteriormente.

* Hatch: Analizando su [documentación oficial](https://hatch.pypa.io/latest/intro/) vemos que cumple los PEP mencionados anteriormente

* Poetry: gestor de dependencias, igual que como hemos hecho con Hatch, vemos que cumple los PEP mencionados anteriormente.

* Guiandonos por los criterios recogidos en los PEP, nos encontramos con dos gestores de dependencias que cumplen estos requisitos, que son [Poetry](https://python-poetry.org/) y [Hatch](https://hatch.pypa.io/latest/intro/)

## Poetry vs Hatch


* Poetry: En esta siguiente comparativa nos vamos a basar en su análisis en Snyk podemos ver que tiene una puntuación de 97, una gran popularidad y un mantenimiento activo.

* Hatch: Viendo su análisis en Snyk, podemos ver que es un proyecto con un mantenimiento activo y con bastante popularidad aunque mucho menor que poetry(Puntuación en Snyk de 85) . 


## Conclusión

* Finalmente, tanto Hatch como Poetry son dos gestores de dependencias que nos van a servir perfectamente para nuestro proyecto y que cumplen con los PEP mencionados anteriormente. Sin embargo me voy a decantar por Poetry simplemente por que tiene una mayor puntuación en Snyk.