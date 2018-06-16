
from ..controller.word_x_lang import *


# -----------------------------------------------------------------------------
# ------- Definición del KB con el que se generan las pruebas unitarias -------
# -----------------------------------------------------------------------------

def setup_module(module):

    + etymology("por", "ego", "chi", "padre")
    + etymology("por", "tio_ter", "chi", "tio_abuelo_seg")
    + etymology("por", "padre", "chi", "abuelo")
    + etymology("spa", "tio_seg", "chi", "tio_abuelo")

    + has_derived_form("ind", "tatarabuelo", "por", "bisabuelo")
    + has_derived_form("ind", "tatarabuelo", "ind", "tio_bisabuelo")
    + has_derived_form("por", "tio_ter", "lat", "primo_ter")
    + has_derived_form("por", "bisabuelo", "ape", "abuelo")
    + has_derived_form("chi", "abuelo", "nor", "tio")
    + has_derived_form("lat", "padre", "ape", "hermano")
    + has_derived_form("lat", "tio_seg", "ita", "primo_seg")

    + etymological_origin_of("por", "padre", "spa", "prueba")
    + etymological_origin_of("ind", "tio_bisabuelo", "ape", "tio_abuelo_seg")
    + etymological_origin_of("spa", "padre", "spa", "ego")
    + etymological_origin_of("spa", "bisabuelo", "por", "tio_abuelo")
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
        En esta prueba el word es igual a -> 'ego'

    :param language: <string> para indicar el idioma sobre el que
    se determinará la existencia de la palabra <word>
        En esta prueba el language es igual a -> 'spa'

    Respecto al valor de retorno que se va verificar, el mismo es
    <booleano> para indicar si la palabra tiene relación o no con el idioma

    La respuesta esperada es un valor booleano de True ya que dados los hechos
    definidos en el setup_module, los siguientes hacen que la respuesta
    sea positiva:

        + etymological_origin_of("spa", "padre", "spa", "ego")
        + etymologically_related("spa", "ego", "ape", "hermano")

    """

    word_aux = 'ego'
    language_aux = 'spa'

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
        En esta prueba el language es igual a -> 'spa'

    Respecto al valor de retorno que se va verificar, el mismo es
    <booleano> para indicar si la palabra tiene relación o no con el idioma

    La respuesta esperada es un valor booleano de True ya que dados los hechos
    definidos en el setup_module, los mismos no cumplen ninguna condicion
        'spa' : 'hola'
    """

    word_aux = 'hola'
    language_aux = 'spa'

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
        En esta prueba el word es igual a -> 'padre'

    :param language: <string> indica el idioma sobre el que se determinará
    la existencia del conjunto de palabras
        En esta prueba el language es igual a -> 'spa'

    Respecto al valor de retorno que se va verificar, el mismo es
    un <array> con el conjunto de palabras en un idioma que pueden ser
    generadas por una palabra específica

    La respuesta esperada es un set de 'words', que dados los hechos
    definidos en el setup_module, una palabra de origen y un lenguaje de
    destino, la palabra origen da lugar a las siguientes que están
    en el lenguaje 'spa':
        -> ego
        -> prueba
    """

    word_aux = 'padre'
    language_aux = 'spa'

    words = set_of_words_in_language(word_aux, language_aux)
    words.sort()

    expected_words = ['ego', 'prueba']

    assert words == expected_words

# -------------------------------------------------------------------------

def test_set_of_languages_related_word():
    """
    Prueba utilizada para verificar la correcta funcionalidad a la hora de:
    ● Listar los idiomas relacionados con una palabra

    Se utilizan los siguientes parámetros:
    :param word: <string> de la palabra sobre la cual se determinaran
    los idiomas que la misma genera
        En esta prueba el word es igual a -> 'padre'

    Respecto al valor de retorno que se va verificar, el mismo es
    un <array> del conjunto de idiomas que estan relacionados
    con la palabra especificada

    La respuesta esperada es un set de 'languages', que dados los hechos
    definidos en el setup_module y una palabra base, la misma se relaciona a
    los siguientes lenguajes:
        -> ape
        -> chi
        -> lat
        -> por
        -> spa

    Note que estos se originan de los siguientes hechos:
        + etymology("por", "ego", "chi", "padre")
        + etymology("por", "padre", "chi", "abuelo")

        + has_derived_form("lat", "padre", "ape", "hermano")

        + etymological_origin_of("por", "padre", "spa", "prueba")
        + etymological_origin_of("spa", "padre", "spa", "ego")

        + etymologically_related("nor", "tio", "lat", "padre")

    """

    word_aux = 'padre'

    langs = set_of_languages_related_word(word_aux)
    langs.sort()

    expected_langs = ['ape', 'chi', 'lat', 'por', 'spa']

    assert langs == expected_langs
