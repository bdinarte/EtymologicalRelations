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

pyDatalog.create_terms('Word, Lang, X, Y, LX, LY')

pyDatalog.create_terms("word_related_lang,"
                       "words_in_lang,"
                       "derived,"
                       "langs_related_word," 
                       "origin_langs,"
                       "derived_langs")


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
#       De cumplirse 'devuelve' el lenguaje asociado (LX/LY) según fue el
#       llamado
#   Sino
#       Devuelve vacío

derived(X, Y, LX, LY) <= (
        etymology(LX, X, LY, Y)
        & etymology_active(True)
)

derived(X, Y, LX, LY) <= (
        etymological_origin_of(LY, Y, LX, X)
        & etymological_origin_of_active(True)
)

derived(X, Y, LX, LY) <= (
        has_derived_form(LY, Y, LX, X)
        & has_derived_form_active(True)
)

# Determina el conjunto de palabras relacionadas (Y) a un lenguaje(LX) y a
# una palabra de origen (X)

words_in_lang(X, LX, Y) <= derived(Y, X, LX, LY)


# -----------------------------------------------------------------------------
#   Listar los idiomas relacionados con una palabra
# -----------------------------------------------------------------------------

# Determina el conjunto de lenguajes de origen/destino
# relacionadas a una palabra de origen
origin_langs(X, LX, Y) <= derived(Y, X, LY, LX)  # Fathers / origin
derived_langs(X, LX, Y) <= derived(Y, X, LX, LY)  # Sons / derived

# Determina el conjunto de lenguajes LX & LY relacionados a una palabra X
langs_related_word(X, LX) <=  derived(X, Y, LX, LY)
langs_related_word(X, LX) <=  derived(Y, X, LY, LX)
langs_related_word(X, LX) <=  derived_langs(X, LX, Y)    # Sons / derived
langs_related_word(X, LX) <=  origin_langs(Y, LX, X)     # Fathers / origin
