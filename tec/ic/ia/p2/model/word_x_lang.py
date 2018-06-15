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

son(X, Y, LX) <= etymology(LY, Y, LX, X)
son(X, Y, LX) <= etymological_origin_of(LX, X, LY, Y)
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
ancestor(X, LX, Y) <= parent(X, Y, LX) & ancestor(Y, LX, A)


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

son_ly(X, Y, LY) <= etymology(LY, Y, LX, X)
son_ly(X, Y, LY) <= etymological_origin_of(LX, X, LY, Y)
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
ancestor_ly(X, LX, Y) <= parent_ly(X, A, LX) & ancestor_ly(A, LY, Y)


# Determina el conjunto de lenguajes LX & LY relacionados a una palabra X
lang_related_word(X, LX) <=  ancestor(X, LX, B)     # Lenguajes LX
lang_related_word(X, LX) <=  ancestor_ly(Y, LX, X)  # Lenguajes LY


+ etymology("spa", "padre", "spa", "ego")
+ etymological_origin_of("spa", "ego", "spa", "padre")
+ etymologically_related('afr', 'aanval', 'afr', 'aanvaller')
+ has_derived_form("eng", "tatarabuelo", "spa", "bisabuelo")
+ has_derived_form("ita", "ttatatattaatarabuelo", "eng", "tatarabuelo")
+ has_derived_form("ita", "tio_bisabuelo", "ind", "tio_abuelo_seg")
+ has_derived_form("afr", "tio_abuelo_seg", "hun", "tio_ter")
+ has_derived_form("por", "tio_ter", "cat", "primo_ter")
+ has_derived_form("spa", "bisabuelo", "lat", "abuelo")
+ has_derived_form("por", "bisabuelo", "mal", "tio_abuelo")
+ has_derived_form("tha", "abuelo", "nap", "padre")
+ has_derived_form("cab", "abuelo", "spa", "tio")
+ has_derived_form("chi", "padre", "nor", "ego")
+ has_derived_form("nap", "padre", "ape", "hermano")
+ has_derived_form("can", "tio", "", "primo")
+ has_derived_form("ale", "tio_abuelo", "spa", "tio_seg")
+ has_derived_form("ara", "tio_seg", "spa", "primo_seg")

print(lang_related_word('abuelo', LX))

print(ancestor('abuelo', 'nap', B))
