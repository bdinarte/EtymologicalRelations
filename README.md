# EtymologicalRelations
Procesamiento de datos mediante un motor de derivación lógico.


## Descripción de Instalación
________________


## Manual de Usuario
________________
### Operación 1
**Descripción:** Determinar si dos palabras son heman@s

Lo que pretende esta funcionalidad es que a partir de dos palabras **(X, Y)** proporcionadas
por el usuario, el sistema brinde una respuesta indicando si la palabra **X** está relacionada con
la palabra **Y** o no.

Entonces, suponiendo que el usuario proporciona la palabra  **'X = hijo1'** y **'Y = hijo2,'**
el sistema verifica en la base de conocimiento para ver si existe un hecho que cumpla la relación
donde _X_ and _Y_ tienen un **padre en común**.

**Utilización de la interfaz:** Para llevar a cabo esta funcionalidad, basta con ingresar la palabra1
y la palabra2 en los campos de texto respectivos. Un ejemplo de este ingreso se encuentra en 
la siguiente imagen:

![img_op1](/imgs/op1.png)

Note que la salida es simplemente un **Si/No** indicando si la palabra **X** se encuentra relacionada a
la palabra **Y** bajo el concepto de herman@s.

### Operación 2
**Descripción:** Determinar si dos palabras son prim@s

Lo que pretende esta funcionalidad es que a partir de dos palabras **(X, Y)** proporcionadas
por el usuario, el sistema brinde una respuesta indicando si la palabra **X** está relacionada con
la palabra **Y** o no.

Entonces, suponiendo que el usuario proporciona la palabra  **'X = primo1'** y **'Y = primo2,'**
el sistema verifica en la base de conocimiento para ver si existe un hecho que cumpla la relación
donde _X_ and _Y_ tienen un **abuelo en común**.

**Utilización de la interfaz:** Para llevar a cabo esta funcionalidad, basta con ingresar la palabra1
y la palabra2 en los campos de texto respectivos. Un ejemplo de este ingreso se encuentra en 
la siguiente imagen:

![img_op2](/imgs/op2.png)

Note que la salida es simplemente un **Si/No** indicando si la palabra **X** se encuentra relacionada a
la palabra **Y** bajo el concepto de prim@s.

### Operación 3
**Descripción:** Determinar si una palabra es hij@ de otra

Lo que pretende esta funcionalidad es que a partir de dos palabras **(X, Y)** proporcionadas
por el usuario, el sistema brinde una respuesta indicando si la palabra **X** está relacionada con
la palabra **Y** o no.

Entonces, suponiendo que el usuario proporciona la palabra  **'X = padre'** y **'Y = hijo,'**
el sistema verifica en la base de conocimiento para ver si existe un hecho que cumpla la relación
donde _Y_ tiene como padre a la palabra _X._

**Utilización de la interfaz:** Para llevar a cabo esta funcionalidad, basta con ingresar la palabra1
y la palabra2 en los campos de texto respectivos. Un ejemplo de este ingreso se encuentra en 
la siguiente imagen:

![img_op3](/imgs/op3.png)

Note que la salida es simplemente un **Si/No** indicando si la palabra **X** se encuentra relacionada a
la palabra **Y** bajo el concepto de hij@.

### Operación 4
**Descripción:** Determinar si una palabra es ti@

Lo que pretende esta funcionalidad es que a partir de dos palabras **(X, Y)** proporcionadas
por el usuario, el sistema brinde una respuesta indicando si la palabra **X** está relacionada con
la palabra **Y** o no.

Entonces, suponiendo que el usuario proporciona la palabra  **'X = tio'** y **'Y = sobrino,'**
el sistema verifica en la base de conocimiento para ver si existe un hecho que cumpla la relación
donde _Y_ tiene como padre una palabra _Z,_ tal que la palabra Z tiene de hermano la palabra _X._
Entonces se cumpliría que la palabra X es ti@ de la palabra Y.

**Utilización de la interfaz:** Para llevar a cabo esta funcionalidad, basta con ingresar la palabra1
y la palabra2 en los campos de texto respectivos. Un ejemplo de este ingreso se encuentra en 
la siguiente imagen:

![img_op4](/imgs/op4.png)

Note que la salida es simplemente un **Si/No** indicando si la palabra **X** se encuentra relacionada a
la palabra **Y** bajo el concepto de ti@.

### Operación 5
**Descripción:** Determinar si son prim@s y en qué grado.

### Operación 6
**Descripción:** Determinar si una palabra está relacionada con un idioma (Si / No)

Lo que pretende esta funcionalidad es que a partir de una palabra y un idioma proporcionados
por el usuario, el sistema brinde una respuesta indicando si la palabra está relacionada con
el lenguaje o no.

Entonces, suponiendo que el usuario proporciona la palabra **'padre'** y el idioma **'spa,'**
el sistema verifica en la base de conocimiento para ver si existe un hecho que cumpla la relación,
ya sea que el _idioma:palabra_ se encuentre al lado derivado o al contrario(generador).

**Utilización de la interfaz:** Para llevar a cabo esta funcionalidad, basta con ingresar la palabra
y el idioma en los campos de texto respectivos. Un ejemplo de este ingreso se encuentra en 
la siguiente imagen:

![img_op6](/imgs/op6.png)

Note que la salida es simplemente un **Si/No** indicando si la palabra se encuentra relacionada al
lenguaje proporcionado.
  

### Operación 7
**Descripción:** Obtener el conjunto de todas las palabras en un idioma originadas por una palabra específica

Lo que pretende esta funcionalidad es que a partir de una palabra y un idioma proporcionados
por el usuario, el sistema brinde una respuesta indicando todas las palabras que son originadas
a partir de la ingresada en la interfaz y además que dichas palabras de encuentren en el idioma
indicado.

Entonces, suponiendo que el usuario proporciona la palabra base: **'-lik'** y el idioma: **'afr,'**
el sistema procede a verificar en la base de conocimiento para ver si existen hechos que cumpla la relación
donde la palabra generadora sea _'-lik'_ y que el lenguaje de la palabra generada sea _'afr'_.

**Utilización de la interfaz:** Para llevar a cabo esta funcionalidad, basta con ingresar la palabra
y el idioma en los campos de texto respectivos. Un ejemplo de este ingreso se encuentra en 
la siguiente imagen:

![img_op7](/imgs/op7.png)

Note que la salida difiere de la operación anterior, ya que en esta no es simplemente un valor booleano,
sino que se espera una lista de idiomas, y de no encontrar ningún hecho simplemente despliega una 
lista vacía de elementos.
 
### Operación 8
**Descripción:** Listar los idiomas relacionados con una palabra

Lo que pretende esta funcionalidad es que a partir de una palabra proporcionada
por el usuario, el sistema brinde una respuesta indicando todas los lenguajes que están relacionados
de manera directa con la misma. Ya sea que la palabra esté escrita en un idioma o que sea generada
de otra palabra en un idioma determinado. En síntesis, la respuesta se compone de los lenguajes originarios
y de los generados, donde exista la palabra especificada en la interfaz.

Entonces, suponiendo que el usuario proporciona la palabra base: **'bruin'**
el sistema procede a verificar en la base de conocimiento para ver si existen hechos que cumpla la relación
donde la palabra generadora/generada sea _'bruin',_ entonces de cumplirse, se toman en cuenta los lenguajes
que incorpora el hecho del KB.

**Utilización de la interfaz:** Para llevar a cabo esta funcionalidad, basta con ingresar la palabra
en el campo de texto respectivo. Un ejemplo de este ingreso se encuentra en 
la siguiente imagen:

![img_op8](/imgs/op8.png)

Note que en la salida se espera una lista de idiomas, y de no encontrar ningún hecho simplemente despliega una 
lista vacía.

### Operación 9
**Descripción:** Contar todas las palabras comunes entre dos idiomas

Lo que pretende esta funcionalidad es que a partir de dos idiomas **(X, Y)** proporcionados
por el usuario, el sistema brinde una respuesta indicando la cantidad de palabras que se encuentran
relacionadas de manera común entre los lenguajes (**X** and **Y**).

Entonces, suponiendo que el usuario proporciona el lenguaje **'X = eng'** y **'Y = afr,'**
el sistema verifica en la base de conocimiento para ver si existe un hecho que cumpla la relación
donde _Y_ tiene un conjunto de palabras _Z,_ tal que ese conjunto Z se encuentra en el idioma _X._
Entonces se cumpliría que las palabras en ese conjunto, son comunes entre Y y X.

**Utilización de la interfaz:** Para llevar a cabo esta funcionalidad, basta con ingresar ambos idiomas
en los campos de texto respectivos. Un ejemplo de este ingreso se encuentra en 
la siguiente imagen:

![img_op9](/imgs/op9.png)

Note que en la salida se espera un valor numérico, indicando la cantidad de palabras en común, las
cuales denominamos como el conjunto Z en el ejemplo anterior.

### Operación 10
**Descripción:** Listar todas las palabras comunes entre dos idiomas

Lo que pretende esta funcionalidad es que a partir de dos idiomas **(X, Y)** proporcionados
por el usuario, el sistema brinde una respuesta indicando la palabras que se encuentran
relacionadas de manera común entre los lenguajes (**X** and **Y**).

Entonces, suponiendo que el usuario proporciona el lenguaje **'X = eng'** y **'Y = afr,'**
el sistema verifica en la base de conocimiento para ver si existe un hecho que cumpla la relación
donde _Y_ tiene un conjunto de palabras _Z,_ tal que ese conjunto Z se encuentra en el idioma _X._
Entonces se cumpliría que las palabras en ese conjunto, son comunes entre Y y X.

**Utilización de la interfaz:** Para llevar a cabo esta funcionalidad, basta con ingresar ambos idiomas
en los campos de texto respectivos. Un ejemplo de este ingreso se encuentra en 
la siguiente imagen:

![img_op10](/imgs/op10.png)

Note que en la salida se espera una lista de palabras. De no encontrar palabras, se despliega un mensaje
indicando dicho resultado.

### Operación 11
**Descripción:** Idioma que más aportó a otro.

### Operación 12
**Descripción:** Listar todos los idiomas que aportaron a otro.


## Resultados Interesantes
________________
### Operación 1
**Descripción:** Determinar si dos palabras son heman@s

### Operación 2
**Descripción:** Determinar si dos palabras son prim@s

### Operación 3
**Descripción:** Determinar si una palabra es hij@ de otra

### Operación 4
**Descripción:** Determinar si una palabra es ti@

### Operación 5
**Descripción:** Determinar si son prim@s y en qué grado.

### Operación 6
**Descripción:** Determinar si una palabra está relacionada con un idioma (Si / No)

### Operación 7
**Descripción:** Obtener el conjunto de todas las palabras en un idioma originadas por una palabra específica

### Operación 8
**Descripción:** Listar los idiomas relacionados con una palabra

### Operación 9
**Descripción:** Contar todas las palabras comunes entre dos idiomas

### Operación 10
**Descripción:** Listar todas las palabras comunes entre dos idiomas

### Operación 11
**Descripción:** Idioma que más aportó a otro.

### Operación 12
**Descripción:** Listar todos los idiomas que aportaron a otro.


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

Por otra parte, el módulo C(Controller) se encarga del flujo de acceso
entre la vista y el modelo, entonces lo que pretende es brindar la definición de funciones
que reciben los parámetros respectivos para ejecutar alguna de las reglas definidas en 
la parte del modelo.

La sección del modelo, contiene todo lo relacionado a la lógica, es donde se definen las 
reglas y donde se hacen las inferencias respectivas a cada método.

El módulo de **test**, contiene todas las pruebas desarrollas por medio de pytest
para cada una de las funcionalidades que contempla el proyecto.

Por último, la carpeta **util** almacena código que está relacionado a herramientas, entre 
estas se encuentran las de lectura y escritura de archivos, entre otras.

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
| Total:                    | 3 750 250     |


Para dar un ejemplo claro de porqué se tomó esta decisión es la eliminación de la
relación: **is_derived_from**, que es recíproca a la relación **has_derived_form.**
* Esto se concluyó por medio de la verificación a nivel de datos, de que realmente 
si existe la regla has_derived_form, también estaba la contraparte is_derived_from, 
con los valores de lenguaje y palabra correspondientes.

* Inclusive si lo vemos a nivel general, podemos determinar que existe la misma cantidad
de relaciones is_derived_from que de has_derived_form, lo que también da un indicio
fuerte de que los registros son recíprocos.

#### Manejo de los tipos de relaciones
Parte de las instrucciones del proyecto incluye que en la interfaz gráfica sea posible 
seleccionar cuáles relaciones se consideran al ejecutar cada operación de consulta. 
Lo anterior debe poder realizarse sin reiniciar por completo la aplicación, es por eso que 
se definen hechos específicos que poseen un valor booleano dependiendo de que 
relación debe tomarse en cuenta para la consulta. Los hechos definidos son:

> etymology_active(True / False)
> has_derived_form_active(True / False)
> etymologically_related_active(True / False)
> etymological_origin_of_active(True / False)

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
