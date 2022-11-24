# Elección Test Runner  

Como se ha comentado en el issue [#19](https://github.com/alvarogaro/AGR-MVS/issues/19), vamos a realizar una elección del Test Runner que vamos a utilizar en nuestro proyecto, para ello vamos a tener como criterios, las mejores prácticas para el lenguaje, la puntuación de la herramienta en la web [Snyk] (https://snyk.io/), el mantenimiento y comunidad de la herramienta y por último su popularidad.


* Tox: Es un Test-Runner que como hemos comentado en el issue nos permite ejecutar nuestro test en un entorno virtual configurable, esta carácterística esta relacionada con las buenas prácticas del lenguaje, viendo su puntuación en snyk vemos que tiene la puntuación máxima, tiene una gran comunidad encargada de su mantenimiento y una gran popularidad

* Nox: De manera similar a Tox, tambien sigue las buenas prácticas del lenguaje, tiene una puntuación de 94 en Snyk, una gran comunidad encargada de su mantenimiento y una gran popularidad.

* Pytest: Es uno de los Test-Runner mas populares de Python con una gran comunidad de mantenimiento, tiene un 97 de puntuación en Snyk, no hace uso de entornos virtuales para la realización de los test.

* Nose2: Tiene una gran comunidad de mantenimiento y cierta popularidad. En Snyk, obtiene una puntuación de 85, no hace uso de entornos virtuales para la realización de los test.


* Finalmente, tras la evaluación de estos Test-Runners, nos vamos a decantar por Tox ya que obtiene la mayor puntuación en Snyk. 






















































