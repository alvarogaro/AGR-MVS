# Elección Gestor De Dependencias

* Como hemos planteado en el issue [#12](https://github.com/alvarogaro/AGR-MVS/issues/12), va a ser necesario la elección de un gestor de dependencias para nuestro proyecto, esto es necesario ya que un gestor de dependencias nos va a permitir tener un proyecto con una mayor previsibilidad, sostenibilidad a lo largo del tiempo y seguridad.

* Para la elección de nuestro gestor de dependencias, tenemos que basarnos en criterios objetivos y de las mejores prácticas del lenguaje que estemos utilizando en nuestro proyecto.

* En nuestro caso, el lenguaje que vamos a utilizar es Python, por lo tanto las mejores prácticas y los criterios objetivos que sigue la comunidad vienen recogidos en los denominados PEP (Python Enhancement Proposals), [Enlace a los PEP](https://peps.python.org/).

* En concreto, estamos tratando ahora la gestión de dependencias, por tanto vamos a seguir las recomendaciones que vienen recogidas en los PEP [517](https://peps.python.org/pep-0517/), [518](https://peps.python.org/pep-0518/) y [621](https://peps.python.org/pep-0621).

## Comparativa Gestores De Dependencias.

* En este apartado vamos a hacer una comparativa de los gestores de dependencias que se comentan en el issue #12 teniendo en cuenta los criterios de los PEP mencionados anteriormente.

* PipEnv: Este gestor de dependencias de python, mirando un poco su [documentación](https://pipenv.pypa.io/en/latest/index.html), podemos ver como su funcionamiento se basa en la presencia de un fichero Pipfile y Pipfile.lock. Debido a que no hace uso de un fichero pyproject.toml, no cumple con el PEP 518, por lo tanto no es un gestor de dependencias que haga uso de las mejores prácticas.

* Hatch: Analizando su [documentación oficial](https://hatch.pypa.io/latest/intro/) vemos como si hace uso de un fichero pyproject.toml para almacenar las dependencias,(Cumple con el PEP 518), ademas su estructura de ficheros es la recomendada por la buenas prácticas.

* Poetry: Gestor de dependencias, igual que hatch hace uso de un fichero pyproject.toml, al igual que su estructura de ficheros es la recomendada por las buenas prácticas, mediante poetry, podemos agrupar los ficheros (Setup.py,requirements.txt,setup.cfg,MANIFES.in y Pipfile en un pyproject.toml, que además de seguir las buenas prácticas nos ayuda a reducir la deuda técnica).


## Poetry vs Hatch

* Finalmente hemos descartado pipenv por no seguir las buenas prácticas y nos queda realizar una comparación entre Poetry y Hatch.

* Poetry: Nos ofrece entornos virtuales de manera automática en la configuración, permite tener una mejor experiencia frente a árboles de dependencia complejos y tiene un uso eficiente de almacenamiento en la caché por tanto es bastante eficiente, viendo su análisis en Snyk podemos ver que tiene una puntuación de 97, una gran popularidad y un mantenimiento activo.

* Hatch: Se define como un manejador de proyectos con su propio manejador de dependencias. Hatch además incorporá funcionalidades como un sistema de test y herramientas para cobertura de código. Hatch como ventaja tiene que nos permite reducir el numero de herramientas que necesitamos en nuestro proyecto  pero lo malo es que al incluir un numero de herramientas tan alto, la curva de aprendizaje va a ser muy grande. Viendo su análisis en Snyk, podemos ver que es un proyecto con un mantenimiento activo y con bastante popularidad aunque mucho menor que poetry(Puntuación en Snyk de 85) . 


## Conclusión

* Finalmente, hemos escogido Poetry como gestor de dependencias, ya que nos permite reducir la deuda técnica, es bastante sencillo a la hora de expresar dependencias y es el gestor con mayor puntuación en Snyk.