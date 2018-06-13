# -----------------------------------------------------------------------------

from model.word_x_lang import *

# -----------------------------------------------------------------------------

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

    words = [i[0] for i in query.data]
    words.sort()

    return words


# -----------------------------------------------------------------------------

def set_of_languages_related_word(word):
    """
    ● Listar los idiomas relacionados con una palabra

    :param word: <string> de la palabra sobre la cual se determinaran
    los idiomas que la misma genera
    :return: <array> del conjunto de idiomas que estan relacionados
    con una palabra en específico
    """

    query = lang_related_word(word, LX)

    langs = [i[0] for i in query.data]
    langs.sort()

    return langs
