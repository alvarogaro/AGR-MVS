# FRANCAPP

## Descripción
Dentro de la grandes franquicias de hostelería se presenta un problema relacionado con la ocupación de sus diferentes tiendas. Tanto Macdonald's,KFC,Burguer King... suelen estar presentes en las principales ciudades y muchas veces debido a su carácter de,"Comida Rápida", el objetivo que tienen sus clientes es el de comer en el menor tiempo posible, por tanto la presencia de grandes colas en sus establecimientos es un problema grave que se busca evitar a toda costa.

## Lógica De Negocio
El problema como se ha comentado antes es la espera en colas de los clientes de cadenas de comida rápida. Para plantera la solución partiremos de un conjunto de datos que son las diferentes tiendas registradas en la aplicación y un conjunto de datos para cada tienda, que sería la media de tiempo que se tarda en servir a un cliente y el tiempo medio de llegada de un nuevo cliente. Con esto, el sistema, haciendo uso de la teoría de colas, realizaría una predicción del tiempo que tardaría un cliente nuevo en ser atendido, de manera que cuando un cliente entrara a la aplicación, en base a estos cálculos, la aplicación mostraría las mejores opciones para el cliente en base a los cálculos anteriores.


## Instalación y Test

* Para instalar poetry dentro de nuestro entorno global, ejecutamos el siguiente comando:
```
pip install poetry
```
* Para instalar poethepoet dentro del entorno global, ejecutamos el siguiente comando

```
pip install poethepoet
```

* Para la creación del entorno virtual e instalación de las dependencias ejecutamos el comando:

```
poe install
```

* Para la comprobación de la sintaxis tendremos que ejecutar el comando

```
poe check 
```
* Realización de los test

```
poe test
```


## Enlaces Documentación

- [Milestones](./docs/Milestones.md)
- [Historias De Usuario](./docs/Historias-Usuario.md)
- [Gestor De Dependencias](./docs/Gestor-Dependencias.md)
- [Gestor De Tareas](./docs/Gestor-Tareas.md)
- [Test Runner](./docs/Test-Runner.md)
- [Biblioteca Aserciones](./docs/Biblioteca-Aserciones.md)
- [Imagen Docker](./docs/Docker.md)   




