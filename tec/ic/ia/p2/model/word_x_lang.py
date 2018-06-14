# -----------------------------------------------------------------------------

from pyDatalog import pyDatalog


# -----------------------------------------------------------------------------
# ------------------------------ Creating Terms -------------------------------
# -----------------------------------------------------------------------------

pyDatalog.create_terms('word_related_lang, set_of_words_in_lang, Word, '
                       'Lang, X, Y, LX, LY, A, B')

pyDatalog.create_terms('etymology, etymological_origin_of,'
                       'etymologically_related, has_derived_form')

pyDatalog.create_terms("son, ancestor, parent, lang_related_word,"
                       "son_ly, ancestor_ly, parent_ly")


# -----------------------------------------------------------------------------
#   Determinar si una palabra está relacionada con un idioma (Si / No)
# -----------------------------------------------------------------------------

# Se asigna True como respuesta si se cumple la regla
# word_related_lang(Word, Lang) en alguna de sus condiciones
word_related_lang(Word, Lang, True) <= word_related_lang(Word, Lang)

# De no cumplirse ninguna regla, se debera asignar un False como respuesta
word_related_lang(Word, Lang, False) <= ~word_related_lang(Word, Lang)

# Verifica si existe un hecho en el KB que tenga la relación
# etymology para la palabra y lenguaje especificado
word_related_lang(Word, Lang) <= (
    etymology(Lang, Word, X, Y)
)

# Verifica si existe un hecho en el KB que tenga la relación
# etymological_origin_of para la palabra y lenguaje especificado
word_related_lang(Word, Lang) <= (
    etymological_origin_of(X, Y, Lang, Word)
)

# Verifica si existe un hecho en el KB que tenga la relación
# etymologically_related para la palabra y lenguaje especificado
word_related_lang(Word, Lang) <= (
    etymologically_related(Lang, Word, X, Y)
)

# Verifica si existe un hecho en el KB que tenga la relación
# has_derived_form para la palabra y lenguaje especificado
word_related_lang(Word, Lang) <= (
    has_derived_form(X, Y, Lang, Word)
)


# -----------------------------------------------------------------------------
#   Obtener el conjunto de todas las palabras en un idioma originadas
#   por una palabra específica (e.g. una palabra específica en latín puede
#   originar múltiples palabras en español)
# -----------------------------------------------------------------------------

# Lo que se pretende con esta regla es determinar los lenguajes relacionados
# a la palabra 'origen' en el hecho, por medio de la verificación de si
# dicha palabra es hija de alguna otra
#   X = Primera palabra
#   Y = Segunda palabra
#   Si se cumple es que X si es hija de Y
#       De cumplirse 'devuelve' el lenguaje asociado (LX) a la palabra X
#   Sino
#       Devuelve vacío

son(X, Y, LX) <= etymology(LX, X, LY, Y)
son(X, Y, LX) <= etymological_origin_of(LY, Y, LX, X)
son(X, Y, LX) <= has_derived_form(LY, Y, LX, X)


# Esta regla se utiliza para determinar si una letra (X), es padre de alguna
# otra (Y), utilizando la regla de hijo definida previamente
#   Entonces: X es padre de Y, Si Y es hija de X
# Note que en esta se llama la regla son para determinar el conjunto de
# lenguajes origen asociados a la palabra X

parent(X, Y, LX) <= son(Y, X, LX)


# Similar a es ancestro
# Determina el conjunto de palabras relacionadas a un lenguaje(LX) y a
# una palabra de origen

ancestor(A, LX, B) <= parent(A, B, LX)
ancestor(X, LX, Y) <= parent(X, A, LX) & ancestor(A, LX, Y)


# -----------------------------------------------------------------------------
#   Listar los idiomas relacionados con una palabra
# -----------------------------------------------------------------------------

# Lo que se pretende con esta regla es determinar los lenguajes relacionados
# a la palabra 'destino'/'producto' en el hecho, por medio de
# la verificación de si dicha palabra es hija de alguna otra
#   X = Primera palabra
#   Y = Segunda palabra
#   Si se cumple es que X si es hija de Y
#       De cumplirse 'devuelve' el lenguaje asociado (LY) a la palabra Y
#   Sino
#       Devuelve vacío

son_ly(X, Y, LY) <= etymology(LX, X, LY, Y)
son_ly(X, Y, LY) <= etymological_origin_of(LY, Y, LX, X)
son_ly(X, Y, LY) <= has_derived_form(LY, Y, LX, X)


# Esta regla se utiliza para determinar si una letra (X), es padre de alguna
# otra (Y), utilizando la regla de hijo definida previamente
#   Entonces: X es padre de Y, Si Y es hija de X
# Note que en esta se llama la regla son_ly para determinar el conjunto de
# lenguajes destino/producto asociados a la palabra Y

parent_ly(X, Y, LY) <= son_ly(Y, X, LY)


# Similar a es ancestro
# Determina el conjunto de lenguajes (LY )relacionadas a una palabra de origen

ancestor_ly(A, LX, B) <= parent_ly(A, B, LX)
ancestor_ly(X, LX, Y) <= parent_ly(X, Y, LX) & ancestor_ly(A, LX, X)


# Determina el conjunto de lenguajes LX & LY relacionados a una palabra X
lang_related_word(X, LX) <=  ancestor(X, LX, B)     # Lenguajes LX
lang_related_word(X, LX) <=  ancestor_ly(Y, LX, X)  # Lenguajes LY





# -----------------------------------------------------------------------------
# ------------------------------ Función Dinarte ------------------------------
# -----------------------------------------------------------------------------


# ----------------------------------------------------------------------------

# Definición de términos comunes a la mayoría de predicados
pyDatalog.create_terms('etymological_origin_of_active,'
                       'has_derived_form_active,'
                       'etymology_active,'
                       'etymologically_related_active')

pyDatalog.create_terms('Lang1, Lang2, Word1, Word2, Total')

+ etymological_origin_of('','','','')
+ has_derived_form('','','','')
+ etymology('','','','')
+ etymologically_related('','','','')
+ etymological_origin_of_active(True)
+ has_derived_form_active(True)
+ etymology_active(True)
+ etymologically_related_active(True)

# ----------------------------------------------------------------------------

# Términos para la función words_in_common
pyDatalog.create_terms('lang_common_words')

# Relaciones para la función words_in_common
lang_common_words(Lang1, Word1, Lang2, Word1) <= (
    etymology(Lang1, Word1, Lang2, Word1) &
    etymology_active(True)
)
lang_common_words(Lang1, Word1, Lang2, Word1) <= (
    etymological_origin_of(Lang1, Word1, Lang2, Word1) &
    etymological_origin_of_active(True)
)
lang_common_words(Lang1, Word1, Lang2, Word1) <= (
    has_derived_form(Lang1, Word1, Lang2, Word1) &
    has_derived_form_active(True)
)
lang_common_words(Lang1, Word1, Lang2, Word1) <= (
    etymologically_related(Lang1, Word1, Lang2, Word1) &
    etymologically_related_active(True)
)

# ----------------------------------------------------------------------------

# Términos para la función common_words_count
pyDatalog.create_terms('count_lang_common_words')

# Relaciones para la función words_in_common
(count_lang_common_words[Lang1, Lang2] == len_(Word1)) <= (
    lang_common_words(Lang1, Word1, Lang2, Word1)
)

# ----------------------------------------------------------------------------

# Términos para la función input_words
pyDatalog.create_terms('input_words')

# Relaciones para la función input_words
# Obtiene cuales palabras aportó un lenguaje a otro
input_words(Lang1, Word1, Lang2, Word2) <= (
    has_derived_form(Lang1, Word1, Lang2, Word2) &
    has_derived_form_active(True)
)
input_words(Lang1, Word1, Lang2, Word2) <= (
    etymology(Lang2, Word2, Lang1, Word1) &
    etymology_active(True)
)
input_words(Lang1, Word1, Lang2, Word2) <= (
    etymological_origin_of(Lang1, Word1, Lang2, Word2) &
    etymological_origin_of_active(True)
)

# ----------------------------------------------------------------------------

# Términos para la función count_input_words
pyDatalog.create_terms('count_input_words')

# Relaciones para la función count_input_words
(count_input_words[Lang1, Lang2] == len_(Word2)) <= (
    input_words(Lang1, Word1, Lang2, Word2)
)

# ----------------------------------------------------------------------------

# Términos para la función count_words_received
pyDatalog.create_terms('count_words_received')

# Relaciones para la función count_words_received
(count_words_received[Lang1] == len_(Word1)) <= (
    input_words(Lang2, Word2, Lang1, Word1)
)

# ----------------------------------------------------------------------------

# Términos para la función input_percent
pyDatalog.create_terms('input_percent', 'Percent', 'Partial')

# Relaciones para la función input_percent
# Retorna el porcentaje que el lenguaje uno le aportó al segundo
(input_percent[Lang1, Lang2] == Percent) <= (
    (Partial == count_input_words[Lang1, Lang2]) &
    (Total == count_words_received[Lang2]) &
    (Percent == Partial/Total)
)

+ etymology('abs', 'beta', 'zsm', 'beta')
+ etymology('aaq', 'prueba1', 'eng', 'prueba1')
+ etymology('aaq', 'senabe', 'eng', 'sannup')
+ etymological_origin_of('abe', 'waniigan', 'eng', 'waniigan')
+ etymological_origin_of('aaq', 'prueba2', 'eng', 'prueba2')
+ etymology('aaq', 'prueba3', 'eng', 'prueba3')
+ has_derived_form('equ', 'father', 'isd', 'son')
+ has_derived_form('equ', 'father', 'isd', 'son2')
+ etymology('aaq', 'son3', 'equ', 'father3')
+ etymological_origin_of('sas', 'mom', 'aaq', 'son4')
+ has_derived_form('sss', 'mom', 'isd', 'son5')


son(LX, LY, Total) <= etymology(LX, X, LY, Y) & (Total == [input_percent[LY, LX]])
son(LX, LY, Total) <= etymological_origin_of(LY, Y, LX, X) & (Total == [input_percent[LY, LX]])
son(LX, LY, Total) <= has_derived_form(LY, Y, LX, X) & (Total == [input_percent[LY, LX]])

# Esta regla se utiliza para determinar si una letra (X), es padre de alguna
# otra (Y), utilizando la regla de hijo definida previamente
#   Entonces: X es padre de Y, Si Y es hija de X
# Note que en esta se llama la regla son para determinar el conjunto de
# lenguajes destino/producto asociados a la palabra Y

# parent(LX, LY, Total) <= son(LY, LX, Total)
parent(LX, LY, Total) <= son(LY, LX, Total)


# Similar a es ancestro
# Determina el conjunto de lenguajes (LY )relacionadas a una palabra de origen

ancestor(LX, LY, Total) <= parent(LX, LY, Total)
ancestor(LX, LY, Total) <= parent(LY, LX, Total)
# ancestor(LX, LY, Total) <= parent(LX, LY, Total) & ancestor(LY, B, Total)

pyDatalog.create_terms('langs_related_lang')
# Determina el conjunto de lenguajes relacionados a otro lenguaje
langs_related_lang(LX, LY, Total) <=  ancestor(LX, LY, Total)
# lang_related_word(LX, LY) <=  ancestor(Y, LX, X)  # Lenguajes LY

print(langs_related_lang('aaq', LX, Total))
