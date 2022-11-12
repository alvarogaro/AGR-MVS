# Elección Gestor De Tareas

* En este documentos vamos a realizar un análisis de los Gestores de Tareas que hemos mencionado en el issue [#13](https://github.com/alvarogaro/AGR-MVS/issues/13). Para este análisis vamos a tocar temas principalmente relacionados con el mantenimiento, seguridad, comunidad...

* Los diferentes análisis de los gestores de tareas se van a obtener de la página web [Snyk](https://snyk.io/)

* Pypyr: Este Gestor ha aumentado su popularidad recientemente, especialmente en octubre de 2022. Revisando su repositorio vemos que ha tenido un gran numero de commits en Octubre de 2022 lo que nos hace ver que es una herramienta que se encuentra en un mantenimiento activo. Tiene una buena cadencia de versiones ( De media 1 cada 3 meses)(Puntuación en Snyk de 75).

* Doit: Respecto a Doit, vemos que adquirió cierta popularidad en abril del 2022, pero a raíz de esa fecha, la popularidad cayó en picado, su cadencia de versiones es muy baja (1 cada año). Respecto a su repositorio vemos que tiene abiertos 70 issues y 5 PR, de los cuales en el ultimo mes no se ha realizado ninguna modificación, y Snyk considera que es un proyecto que esta Inactivo por tanto no sería una buena opción ( Puntuación de 75 en Snyk).

* Invoke: Vemos que es el gestor de tareas mas popular de todos los disponibles para python en los ultimos 3 meses. Su cadencia de actualizaciones es bastante grande y se considera como un proyecto en mantenimiento activo. Cuenta con 278 issues y 68 PR, pero se tiene constancia de que el proyecto tiene mas de 50 desarrolladores activos trabajando en su mantenimiento. Tiene cerca de 1 millón de descargas semanales, por tanto es considerado como un "influential project" y los últimos análisis de seguridad no muestran ninguna vulnerabilidad(Puntuación de 81 en Snyk).

* Poethepoet: Gestor de Tareas bastante interesante debido a que puede trabajar conjuntamente con Poetry ( Esto nos ayudaría a tener un numero menor de ficheros que mantener). Su popularidad es bastante alta y tiene registrados unos 20 desarrolladores activos por tanto se considera como una herramienta en mantenimiento activo(Puntuación de Snyk 85).

* Por todo lo expuesto anteriormente, utilizaremos Poethepoet como gestor de tareas para nuestro proyecto, ya que nos permite reducir la deuda técnica de nuestro proyecto, teniendo en cuenta nuestras anteriores decisiones, es un gestor en mantenimiento y con una gran comunidad y obtiene la mayor puntuación en Snyk.