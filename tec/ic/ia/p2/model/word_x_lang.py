# -----------------------------------------------------------------------------

from pyDatalog import pyDatalog


# -----------------------------------------------------------------------------
# ------------------------------ Creating Terms -------------------------------
# -----------------------------------------------------------------------------

pyDatalog.create_terms('etymology, etymological_origin_of,'
                       'etymologically_related, has_derived_form')

pyDatalog.create_terms('etymological_origin_of_active,'
                       'has_derived_form_active,'
                       'etymology_active,'
                       'etymologically_related_active')

pyDatalog.create_terms('word_related_lang, set_of_words_in_lang, Word, '
                       'Lang, X, Y, LX, LY, A, B')

pyDatalog.create_terms("son, ancestor, parent, lang_related_word,"
                       "son_ly, ancestor_ly, parent_ly, ancestor_lx")


+ etymological_origin_of_active(True)
+ has_derived_form_active(True)
+ etymology_active(True)
+ etymologically_related_active(True)

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
    & etymology_active(True)
)
word_related_lang(Word, Lang) <= (
    etymology(X, Y, Lang, Word)
    & etymology_active(True)
)

# Verifica si existe un hecho en el KB que tenga la relación
# etymological_origin_of para la palabra y lenguaje especificado
word_related_lang(Word, Lang) <= (
    etymological_origin_of(X, Y, Lang, Word)
    & etymological_origin_of_active(True)
)
word_related_lang(Word, Lang) <= (
    etymological_origin_of(Lang, Word, X, Y)
    & etymological_origin_of_active(True)
)

# Verifica si existe un hecho en el KB que tenga la relación
# etymologically_related para la palabra y lenguaje especificado
word_related_lang(Word, Lang) <= (
    etymologically_related(Lang, Word, X, Y)
    & etymologically_related_active(True)
)
word_related_lang(Word, Lang) <= (
    etymologically_related(X, Y, Lang, Word)
    & etymologically_related_active(True)
)

# Verifica si existe un hecho en el KB que tenga la relación
# has_derived_form para la palabra y lenguaje especificado
word_related_lang(Word, Lang) <= (
    has_derived_form(X, Y, Lang, Word)
    & has_derived_form_active(True)
)
word_related_lang(Word, Lang) <= (
    has_derived_form(Lang, Word, X, Y)
    & has_derived_form_active(True)
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

son(X, Y, LX) <= (
        etymology(LX, X, LY, Y)
        & etymology_active(True)
)

son(X, Y, LX) <= (
        etymological_origin_of(LY, Y, LX, X)
        & etymological_origin_of_active(True)
)

son(X, Y, LX) <= (
        has_derived_form(LY, Y, LX, X)
        & has_derived_form_active(True)
)


# Esta regla se utiliza para determinar si una letra (X), es padre de alguna
# otra (Y), utilizando la regla de hijo definida previamente
#   Entonces: X es padre de Y, Si Y es hija de X
# Note que en esta se llama la regla son para determinar el conjunto de
# lenguajes origen asociados a la palabra X

parent(X, Y, LX) <= son(Y, X, LX)


# Similar a es ancestro
# Determina el conjunto de palabras relacionadas a un lenguaje(LX) y a
# una palabra de origen

ancestor(X, LX, Y) <= parent(X, Y, LX)


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

son_ly(X, Y, LY) <= (
        etymology(LX, X, LY, Y)
        & etymology_active(True)
)
son_ly(X, Y, LY) <= (
        etymological_origin_of(LY, Y, LX, X)
        & etymological_origin_of_active(True)
)
son_ly(X, Y, LY) <= (
        has_derived_form(LY, Y, LX, X)
        & has_derived_form_active(True)
)


# Esta regla se utiliza para determinar si una letra (X), es padre de alguna
# otra (Y), utilizando la regla de hijo definida previamente
#   Entonces: X es padre de Y, Si Y es hija de X
# Note que en esta se llama la regla son_ly para determinar el conjunto de
# lenguajes destino/producto asociados a la palabra Y

parent_ly(X, Y, LY) <= son_ly(Y, X, LY)


# Similar a es ancestro
# Determina el conjunto de lenguajes (LY )relacionadas a una palabra de origen

ancestor_ly(A, LX, B) <= parent_ly(A, B, LX)


ancestor_lx(X, LX, Y) <= parent(X, Y, LX)

# Determina el conjunto de lenguajes LX & LY relacionados a una palabra X
lang_related_word(X, LX) <=  son(X, Y, LX)          # Lenguajes con word X lado hijo
lang_related_word(X, LX) <=  son_ly(Y, X, LX)       # Lenguajes con word X lado padre
lang_related_word(X, LX) <=  ancestor_lx(X, LX, B)     # Lenguajes LX
lang_related_word(X, LX) <=  ancestor_ly(Y, LX, X)  # Lenguajes LY
