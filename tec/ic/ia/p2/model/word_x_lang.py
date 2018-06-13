# -----------------------------------------------------------------------------

from pyDatalog import pyDatalog
from os import path as ospath
from sys import path as syspath

from util.file_management import get_etim_database


# -----------------------------------------------------------------------------
# ------------------------------ Creating Terms -------------------------------
# -----------------------------------------------------------------------------

pyDatalog.create_terms('word_related_lang, set_of_words_in_lang, Word, '
                       'Lang, X, Y, LX, LY, A, B')

pyDatalog.create_terms('etymology, etymological_origin_of,'
                       'etymologically_related, has_derived_form,'
                       'is_derived_from, orthography')

pyDatalog.create_terms("is_son, is_ancestor, is_parent, lang_related_word,"
                       "is_son2, is_ancestor2, is_parent2")


# -----------------------------------------------------------------------------

word_related_lang(Word, Lang, True) <= word_related_lang(Word, Lang)

word_related_lang(Word, Lang, False) <= ~word_related_lang(Word, Lang)

word_related_lang(Word, Lang) <= (
    etymology(Lang, Word, X, Y)
)
word_related_lang(Word, Lang) <= (
    etymological_origin_of(X, Y, Lang, Word)
)
word_related_lang(Word, Lang) <= (
    etymologically_related(Lang, Word, X, Y)
)
word_related_lang(Word, Lang) <= (
    has_derived_form(X, Y, Lang, Word)
)
word_related_lang(Word, Lang) <= (
    is_derived_from(Lang, Word, X, Y)
)


def word_related_language(word, language):
    """
    ● Determinar si una palabra está relacionada con un idioma (Si / No)

    :param word: <string> indica la palabra utilizada para
    encontrar una posible existencia en el idioma <language>
    :param language: <string> para indicar el idioma sobre el que
    se determinará la existencia de la palabra <word>
    :return: <booleano> para indicar si la palabra tiene relación o no
    con el idioma
    """

    query = word_related_lang(word, language, Y)
    value = query.v()[0]

    return value


# -----------------------------------------------------------------------------

# X = Primera palabra
# Y = Segunda palabra
# True es que X si es hija de Y
is_son(X, Y, LX, True) <= is_son(X, Y, LX)
is_son(X, Y, LX, False) <= ~is_son(X, Y, LX)

is_son(X, Y, LX) <= etymology(LX, X, LY, Y)
is_son(X, Y, LX) <= etymological_origin_of(LY, Y, LX, X)
is_son(X, Y, LX) <= has_derived_form(LY, Y, LX, X)
is_son(X, Y, LX) <= is_derived_from(LX, X, LY, Y)

is_parent(X, Y, LX) <= is_son(Y, X, LX)

is_ancestor(A, LX, B) <= is_parent(A, B, LX)
is_ancestor(X, LX, Y) <= is_parent(X, A, LX) & is_ancestor(A, LX, Y)

# -----------------------------------------------------------------------------

def set_of_words_in_language(word, language):
    """
    ● Obtener el conjunto de todas las palabras en un idioma originadas
    por una palabra específica (e.g. una palabra específica en latín puede
    originar múltiples palabras en español)

    :param word: <string> indica la palabra utilizada para
    encontrar el conjunto de palabras que genera en un idioma <language>
    :param language: <string> indica el idioma sobre el que se determinará
    la existencia del conjunto de palabras
    :return: <array> con el conjunto de palabras en un idioma
    que pueden ser generadas por una palabra específica
    """

    query = is_ancestor(word, language, X)

    return query


# -----------------------------------------------------------------------------

# X = Primera palabra
# Y = Segunda palabra
# True es que X si es hija de Y
is_son2(X, Y, LY, True) <= is_son2(X, Y, LY)
is_son2(X, Y, LY, False) <= ~is_son2(X, Y, LY)

is_son2(X, Y, LY) <= etymology(LX, X, LY, Y)
is_son2(X, Y, LY) <= etymological_origin_of(LY, Y, LX, X)
is_son2(X, Y, LY) <= has_derived_form(LY, Y, LX, X)
is_son2(X, Y, LY) <= is_derived_from(LX, X, LY, Y)

is_parent2(X, Y, LY) <= is_son2(Y, X, LY)

is_ancestor2(A, LX, B) <= is_parent2(A, B, LX)
is_ancestor2(X, LX, Y) <= is_parent2(X, Y, LX) & is_ancestor2(A, LX, X)

lang_related_word(X, LX) <=  is_ancestor(X, LX, B)
lang_related_word(X, LX) <=  is_ancestor2(Y, LX, X)


def set_of_languages_related_word(word):
    """
    ● Listar los idiomas relacionados con una palabra

    :param word: <string> de la palabra sobre la cual se determinaran
    los idiomas que la misma genera
    :return: <array> del conjunto de idiomas que estan relacionados
    con una palabra en específico
    """

    query = lang_related_word(word, LX)

    return query
