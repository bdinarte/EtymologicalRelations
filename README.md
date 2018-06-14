# EtymologicalRelations
Procesamiento de datos mediante un motor de derivación lógico.


## Descripción de Instalación
________________


## Manual de Usuario
________________
### Operación 1
**Descipción:** Determinar si dos palabras son heman@s

### Operación 2
**Descipción:** Determinar si dos palabras son prim@s

### Operación 3
**Descipción:** Determinar si una palabra es hij@ de otra

### Operación 4
**Descipción:** Determinar si una palabra es ti@

### Operación 5
**Descipción:** Determinar si son prim@s y en qué grado.

### Operación 6
**Descipción:** Determinar si una palabra está relacionada con un idioma (Si / No)

### Operación 7
**Descipción:** Obtener el conjunto de todas las palabras en un idioma originadas por una palabra específica

### Operación 8
**Descipción:** Listar los idiomas relacionados con una palabra

### Operación 9
**Descipción:** Contar todas las palabras comunes entre dos idiomas

### Operación 10
**Descipción:** Listar todas las palabras comunes entre dos idiomas

### Operación 11
**Descipción:** Idioma que más aportó a otro.

### Operación 12
**Descipción:** Listar todos los idiomas que aportaron a otro.


## Resultados Interesantes
________________
### Operación 1
**Descipción:** Determinar si dos palabras son heman@s

### Operación 2
**Descipción:** Determinar si dos palabras son prim@s

### Operación 3
**Descipción:** Determinar si una palabra es hij@ de otra

### Operación 4
**Descipción:** Determinar si una palabra es ti@

### Operación 5
**Descipción:** Determinar si son prim@s y en qué grado.

### Operación 6
**Descipción:** Determinar si una palabra está relacionada con un idioma (Si / No)

### Operación 7
**Descipción:** Obtener el conjunto de todas las palabras en un idioma originadas por una palabra específica

### Operación 8
**Descipción:** Listar los idiomas relacionados con una palabra

### Operación 9
**Descipción:** Contar todas las palabras comunes entre dos idiomas

### Operación 10
**Descipción:** Listar todas las palabras comunes entre dos idiomas

### Operación 11
**Descipción:** Idioma que más aportó a otro.

### Operación 12
**Descipción:** Listar todos los idiomas que aportaron a otro.


## Detalles de Implementación y Diseño
________________

### Diseño
Respecto al diseño del sistema, se decide crear una especie de módulos con una divisón 
basada en el modelo MVC (Model, View, Controller), no obstante, también se incluyen
folders para la incorporación de las pruebas, los archivos utilizados y herramientas.

Entonces de esta manera, el módulo V (view) se encarga de controlar todo lo relacionado
con el diseño, despliegue y ejecución de la interfaz gráfica mostrada al usuario. Que incluye
eventos por medio de botones, inputs para ingresar datos y áreas destinadas a mostrar las
respuestas recibidas por parte del sistema.

Por otra parte, el módulo C(Controller) se encarga de controlar el flujo de acceso
entre la vista y el modelo, entonces lo que pretende es brindar la definición de funciones
que reciben los parámetros respectivos para ejecutar alguna de las reglas definidas en 
la parte del modelo.

La sección del modelo, contiene todo lo relacionado a la lógica, es donde se definen las 
reglas y donde se hacen las inferencias respectivas a cada método.

El módulo de test, contiene todas las pruebas desarrollas por medio de pytest
para cada una de las funcionalidades que contempla el proyecto.

Por último, el folder util almacena código que está relacionado a herramientas, entre 
estas se encuentran las de lectura de archivos, escritura, entre otras cosas.

### Implementación
En este apartado es importante mencionar que no todas las relaciones que se encontraban en 
el archivo etymwn.tsv que representa la base de datos, fueron consideradas, ya que el equipo
de trabajo encontró que algunas relaciones eran recíprocas, entonces con solo una de ellas
bastaría para encontrar la relación.

La lista de relaciones que se consideraron a lo largo del desarrollo de este proyecto son:
| Relación                  | Registros     |
| ------------------------- | ------------- |
| etymology                 | 473 515       |
| etymological_origin_of    | 473 433       |
| etymologically_related    | 538 558       |
| has_derived_form          | 2 264 744     |
| ------------------------- | ------------- |
| Total:                    | 3 750 250     |


Para dar un ejemplo claro de porqué se tomó esta decisión es la eliminación de la
relación: **is_derived_from**, que es recíproca a la relación **has_derived_form.**
* Esto se concluyó por medio de la verificación a nivel de código, de que realmente 
si existe la regla has_derived_form, también estaba la contraparte is_derived_from, 
con los valores de lengauje y palabra correspondientes.

* Inclusive si lo vemos a nivel de registros, podemos determinar que existen la misma 
cantidad de relaciones is_derived_from que de has_derived_form, lo que también da un 
indicio claro de que los registros son recíprocos.


## Distribución de Trabajo
________________
La distribución de trabajo en este proyecto se realizó según las funcionalidades
que fueron solitidas, es decir que a cada uno de los tres estudiantes le tocó desarrollar
un conjunto de estas.
* Palabra con Palabra
* Palabra con lenguaje
* Lenguaje con lenguaje 

Respecto a los integrantes del proyecto:

| Nombre                    | Carné      | Nota |
| ------------------------- | ---------- | ---- |
| Brandon Dinarte Chavarría | 2015088894 | 100  |
| Armando López Cordero     | 2015125414 | 100  |
| Julian Salinas Rojas      | 2015114132 | 100  |

Estudiantes de Ingeniería en Computación del Instituto Tecnológico de Costa Rica.
