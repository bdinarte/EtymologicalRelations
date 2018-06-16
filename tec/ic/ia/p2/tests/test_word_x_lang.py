
from ..controller.word_x_lang import *


# -----------------------------------------------------------------------------
# ------- Definición del KB con el que se generan las pruebas unitarias -------
# -----------------------------------------------------------------------------

def setup_module(module):
    + etymology("spa", "ego", "lat", "padre")
    + etymology("por", "tio_ter", "chi", "tio_abuelo_seg")
    + etymology("lat", "padre", "chi", "abuelo")
    + etymology("spa", "tio_seg", "spa", "tio_abuelo")

    + has_derived_form("ind", "tatarabuelo", "por", "bisabuelo")
    + has_derived_form("ind", "tatarabuelo", "ind", "tio_bisabuelo")
    + has_derived_form("por", "tio_ter", "lat", "primo_ter")
    + has_derived_form("por", "bisabuelo", "chi", "abuelo")
    + has_derived_form("chi", "abuelo", "nor", "tio")
    + has_derived_form("lat", "padre", "ape", "hermano")
    + has_derived_form("lat", "tio_seg", "ita", "primo_seg")

    + etymological_origin_of("ind", "tio_bisabuelo", "chi", "tio_abuelo_seg")
    + etymological_origin_of("lat", "padre", "spa", "ego")
    + etymological_origin_of("por", "bisabuelo", "spa", "tio_abuelo")
    + etymological_origin_of("nor", "tio", "ita", "primo")

    + etymologically_related("spa", "ego", "ape", "hermano")
    + etymologically_related("nor", "tio", "lat", "padre")


# -----------------------------------------------------------------------------
# -- Definición de las diferentes pruebas para las funcionalidades word_lang --
# -----------------------------------------------------------------------------

def test_word_related_language_true():

    """
    Prueba utilizada para verificar la correcta funcionalidad a la hora de:
    ● Determinar si una palabra está relacionada con un idioma (Si / No)

    Se utilizan los siguientes parámetros:
    :param word: <string> indica la palabra utilizada para
    encontrar una posible existencia en el idioma <language>
        En esta prueba el word es igual a -> '-lik'

    :param language: <string> para indicar el idioma sobre el que
    se determinará la existencia de la palabra <word>
        En esta prueba el language es igual a -> 'afr'

    Respecto al valor de retorno que se va verificar, el mismo es
    <booleano> para indicar si la palabra tiene relación o no con el idioma

    La respuesta esperada es un valor booleano de True ya que dados los hechos
    definidos en el setup_module, los siguientes hacen que la respuesta
    sea positiva:

        + etymological_origin_of("afr", "-lik", "eng", "persoonlik")
        + etymological_origin_of("afr", "-lik", "afr", "tydelik")
        + etymological_origin_of("afr", "-lik", "zsm", "wetenskaplik")
        + etymological_origin_of("afr", "-lik", "afr", "wetlik")
        + has_derived_form("afr", "-lik", "afr", "wetenskaplik")
        + has_derived_form("ita", "April", "afr", "-lik")

    """

    word_aux = '-lik'
    language_aux = 'afr'

    answer = word_related_language(word_aux, language_aux)

    assert answer

# -------------------------------------------------------------------------

def test_word_related_language_false():
    """
    Prueba utilizada para verificar la correcta funcionalidad a la hora de:
    ● Determinar si una palabra está relacionada con un idioma (Si / No)

    Se utilizan los siguientes parámetros:
    :param word: <string> indica la palabra utilizada para
    encontrar una posible existencia en el idioma <language>
        En esta prueba el word es igual a -> 'hola'

    :param language: <string> para indicar el idioma sobre el que
    se determinará la existencia de la palabra <word>
        En esta prueba el language es igual a -> 'afr'

    Respecto al valor de retorno que se va verificar, el mismo es
    <booleano> para indicar si la palabra tiene relación o no con el idioma

    La respuesta esperada es un valor booleano de True ya que dados los hechos
    definidos en el setup_module, los mismos no cumplen ninguna condicion
        'afr' : 'hola'
    """

    word_aux = 'hola'
    language_aux = 'afr'

    answer = word_related_language(word_aux, language_aux)

    assert not answer

# -------------------------------------------------------------------------

def test_set_of_words_in_language():
    """
    Prueba utilizada para verificar la correcta funcionalidad a la hora de:
    ● Obtener el conjunto de todas las palabras en un idioma originadas
    por una palabra específica (e.g. una palabra específica en latín puede
    originar múltiples palabras en español)

    Se utilizan los siguientes parámetros:
    :param word: <string> indica la palabra utilizada para
    encontrar el conjunto de palabras que genera en un idioma <language>
        En esta prueba el word es igual a -> '-lik'

    :param language: <string> indica el idioma sobre el que se determinará
    la existencia del conjunto de palabras
        En esta prueba el language es igual a -> 'afr'

    Respecto al valor de retorno que se va verificar, el mismo es
    un <array> con el conjunto de palabras en un idioma que pueden ser
    generadas por una palabra específica

    La respuesta esperada es un set de 'words', que dados los hechos
    definidos en el setup_module, una palabra de origen y un lenguaje de
    destino, la palabra origen da lugar a las siguientes que están
    en el lenguaje 'afr':
        -> tydelik
        -> wetenskaplik
        -> wetlik
    """

    word_aux = '-lik'
    language_aux = 'afr'

    words = set_of_words_in_language(word_aux, language_aux)

    expected_words = ['tydelik', 'wetenskaplik', 'wetlik']

    assert words == expected_words

# -------------------------------------------------------------------------

def test_set_of_languages_related_word():
    """
    Prueba utilizada para verificar la correcta funcionalidad a la hora de:
    ● Listar los idiomas relacionados con una palabra

    Se utilizan los siguientes parámetros:
    :param word: <string> de la palabra sobre la cual se determinaran
    los idiomas que la misma genera
        En esta prueba el word es igual a -> '-lik'

    Respecto al valor de retorno que se va verificar, el mismo es
    un <array> del conjunto de idiomas que estan relacionados
    con la palabra especificada

    La respuesta esperada es un set de 'languages', que dados los hechos
    definidos en el setup_module y una palabra base, la misma se relaciona a
    los siguientes lenguajes:
        -> afr
        -> eng
        -> ita
        -> zsm

    Note que estos se originan de los siguientes hechos:
        + etymological_origin_of("afr", "-lik", "afr", "tydelik")
        + etymological_origin_of("afr", "-lik", "eng", "persoonlik")
        + etymological_origin_of("afr", "-lik", "zsm", "wetenskaplik")
        + has_derived_form("ita", "April", "afr", "-lik")
    """

    word_aux = '-lik'

    langs = set_of_languages_related_word(word_aux)

    expected_langs = ['afr', 'eng', 'ita', 'zsm']

    assert langs == expected_langs
