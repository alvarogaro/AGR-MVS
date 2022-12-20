## Elección de la biblioteca de aserciones.

* En este documento vamos a realizar un análisis de las bibliotecas de aserciones que hemos comentado en el issue [#21](https://github.com/alvarogaro/AGR-MVS/issues/21)

* Los criterios que vamos a seguir se basan en el análisis de estas herramientas en la página web [Snyk](https://snyk.io/), en concreto vamos a mirar su puntuación global, mantenimiento y popularidad. Seguidamente vamos a tener en cuenta que cumplan con las buenas prácticas del lenguaje, que tengan una fácil integración con la herramienta de test que hemos escogido anteriormente y finalmente que nos permita usar múltiples funciones de aserción.

* [Hypothesis](https://snyk.io/advisor/python/hypothesis): Esta librería de Aserciones leyendo su página oficial nos ofrece una manera mas rápida, humana y sencilla de automatizar los test. Tiene una puntuación de 97 en Snyk, además de una gran popularidad y una solida comunidad de mantenimiento.

* [Assertpy](https://snyk.io/advisor/python/assertpy): Esta librería de Aserciones tiene una puntuación de 66 en Snyk, tiene la capacidad de tener una buena integración con pytest,

* [PyHamcrest](https://snyk.io/advisor/python/pyhamcrest): Framework para matchers, mediante esta biblioteca tenemos una muy amplia gama de funcionalidades para probar "UI validations", filtrado de datos... Esta característica permite tener test legibles, limpios y de un alto valor. Tiene una puntuación en Snyk de 85, es una herramienta con un desarrollo activo y alta popularidad
  
* [Unittest](https://docs.python.org/3/library/unittest.html): Librería estándar de python por tanto se encuentra en su core, no sería relevante la puntuación que tiene en Snyk.


* Tras haber evaluado las herramientas anteriores, y haciendo un balance de los criterios anteriormente mencionados, vemos que la herramienta mas "completa" es PyHamcrest, debido a una alta puntuación junto con su gran funcionalidad para crear test con gran funcionalidad y limpieza. Elegimos PyHamcrest sobre Unittest ya que nos proporciona "matchers", también conocidos como "assertion functions", extra sobre los que vienen en Unittest lo que nos va a permitir tener una mayor funcionalidad a la hora de hacer los test.