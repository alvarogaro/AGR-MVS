# Elección Gestor De Tareas

* En este documentos vamos a realizar un análisis de los Gestores de Tareas que hemos mencionado en el issue [#13](https://github.com/alvarogaro/AGR-MVS/issues/13).

* Los criterios que vamos a seguir se basan en el análisis que se realiza de estas herramientas en la página web [Snyk](https://snyk.io/), en concreto vamos a tener en cuenta su puntuación global, mantenimiento y popularidad.

* Como criterio adicional, vamos a tener en cuenta la posibilidad de que se puedan integrar con el gestor de dependencias que hemos elegido anteriormente, ya que esto nos podrá ayudar a reducir el numero de ficheros que debemos mantener.


* [Pypyr](https://snyk.io/advisor/python/pypyr): Este gestor ha aumentado su popularidad recientemente, especialmente en octubre de 2022. Revisando su repositorio vemos que ha tenido un gran numero de commits en Octubre de 2022 lo que nos hace ver que es una herramienta que se encuentra en un mantenimiento activo. Tiene una buena cadencia de versiones ( De media 1 cada 3 meses)(Puntuación en Snyk de 75).

* [Doit](https://snyk.io/advisor/python/doit): Respecto a Doit, vemos que adquirió cierta popularidad en abril del 2022, pero a raíz de esa fecha, la popularidad cayó en picado, su cadencia de versiones es muy baja (1 cada año). Respecto a su repositorio vemos que tiene abiertos 70 issues y 5 PR, de los cuales en el ultimo mes no se ha realizado ninguna modificación, y Snyk considera que es un proyecto que esta Inactivo por tanto no sería una buena opción ( Puntuación de 75 en Snyk).

* [Invoke](https://snyk.io/advisor/python/invoke): Vemos que es el gestor de tareas mas popular de todos los disponibles para python en los ultimos 3 meses. Su cadencia de actualizaciones es bastante grande y se considera como un proyecto en mantenimiento activo. Cuenta con 278 issues y 68 PR, pero se tiene constancia de que el proyecto tiene mas de 50 desarrolladores activos trabajando en su mantenimiento. Tiene cerca de 1 millón de descargas semanales, por tanto es considerado como un "influential project" y los últimos análisis de seguridad no muestran ninguna vulnerabilidad(Puntuación de 81 en Snyk).

* [Poethepoet](https://snyk.io/advisor/python/poethepoet): gestor de tareas bastante interesante debido a que puede usar el mismo fichero (pyproject.toml) que Poetry (Cosa que no es posible con Hatch). Su popularidad es bastante alta y tiene registrados unos 20 desarrolladores activos por tanto se considera como una herramienta en mantenimiento activo(Puntuación de Snyk 85).

* Por todo lo expuesto anteriormente, utilizaremos Poethepoet como gestor de tareas para nuestro proyecto, ya que nos permite reducir la deuda técnica de nuestro proyecto, teniendo en cuenta nuestras anteriores decisiones, es un gestor en mantenimiento y con una gran comunidad y obtiene la mayor puntuación en Snyk.