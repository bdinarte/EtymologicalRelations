# ----------------------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# ----------------------------------------------------------------------------

from model.lang_x_lang import *

# ----------------------------------------------------------------------------


def words_in_common(language1, language2):
    """
    Función principal para obtener las palabras en común entre dos idiomas
    :param language1: cadena de texto que representa el primer lenguaje
    :param language2: cadena de texto que representa el segundo lenguaje
    :return: Conjunto de las palabras en común entre los idiomas
    """

    query_results = lang_common_words(language1, language2, Word1)

    if not query_results.v():
        return {'No hay palabras en común.'}

    existing_words = [word_tuple[0] for word_tuple in query_results.data]
    return set(existing_words)


# ----------------------------------------------------------------------------


def count_common_words(language1, language2):
    """
    Función principal para contar las palabras en común entre dos idiomas
    :param language1: cadena de texto que representa el primer lenguaje
    :param language2: cadena de texto que representa el segundo lenguaje
    :return: Cantidad de palabras en común entre los idiomas
    """

    word_count = count_lang_common_words[language1, language2] == Total

    return word_count.v()[0] if word_count.v() else 0


# ----------------------------------------------------------------------------


def aux_input_words(language1, language2):
    """
    Función auxiliar para obtener las palabras que el 1er idioma aportó a otro
    :param language1: cadena de texto que representa el primer lenguaje
    :param language2: cadena de texto que representa el segundo lenguaje
    :return: Conjunto con las palabras que un idioma aportó al otro
    """

    query_results = input_words(language1, Word1, language2, Word2)

    if not query_results.v():
        return {'El lenguaje no aportó nada.'}

    existing_words = [word_tuple[1] for word_tuple in query_results.data]
    return set(existing_words)


def aux_count_input_words(language1, language2):
    """
    Función auxiliar para contar las palabras que el 1er idioma aportó al otro
    :param language1: cadena de texto que representa el primer lenguaje
    :param language2: cadena de texto que representa el segundo lenguaje
    :return: cantidad de palabras aportadas
    """

    word_count = count_input_words[language1, language2] == Total

    return word_count.v()[0] if word_count.v() else 0


def aux_count_words_received(language):
    """
    Función auxiliar para contar el total de la suma de palabras que un
    lenguaje recibió de todos los lenguajes que le aportan
    :param language: cadena de texto que representa el lenguaje
    :return: cantidad de palabras recibidas
    """

    word_count = count_words_received[language] == Total

    return word_count.v()[0] if word_count.v() else 0

# ----------------------------------------------------------------------------


def aux_input_percent(language1, language2):
    """
    Función auxiliar para calcular el porcentaje que representa el aporte de
    el primer lenguaje al segundo
    :param language1: cadena de texto que representa el primer lenguaje
    :param language2: cadena de texto que representa el segundo lenguaje
    :return: un número entre 0 y 1 representando el porcentaje aportado
    """

    percent = input_percent[language1, language2] == Percent

    return percent.v()[0] if percent.v() else 0


# ----------------------------------------------------------------------------


def get_all_lang_inputs(language=''):
    """
    Función principal para obtener todos los porcentajes de aporte que
    ocurren entre todos los lenguajes. En caso de especificar un lenguaje
    como parámetro, se calculan los porcentajes que cada lenguaje aportó
    solo a ese lenguaje de parámetro
    :param language: cadena de texto que representa el lenguaje, languaje=''
    para realizar el cálculo de todos los aportes existentes
    :return: conjunto de todos los aportes
    """

    if language == '':
        query_results = all_lang_inputs(Lang1, Lang2, Total)
    else:
        query_results = all_lang_inputs(Lang1, language, Total)

    if not query_results.v():
        return ['No hay aportes.']

    if language == '':
        existing_results = [result[0] + ' aporta a '
                            + result[1] + ' un '
                            + str(round(result[2], 2) * 100) + '%.'
                            for result in query_results.data]
    else:
        existing_results = [result[0] + ' aporta a '
                            + language + ' un '
                            + str(round(result[1], 2) * 100) + '%.'
                            for result in query_results.data]

    return set(existing_results)


# ----------------------------------------------------------------------------


def get_max_input(language=''):
    """
    Función principal para obtener el mayor porcentaje de aporte entre los que
    ocurren entre todos los lenguajes. En caso de especificar un lenguaje
    como parámetro, se calcula el máximo porcentaje entre los que cada
    lenguaje aportó solo a ese lenguaje de parámetro
    :param language: cadena de texto que representa el lenguaje, languaje=''
    para realizar el cálculo del máximo entre todos los aportes existentes
    :return: cadena de texto que representa el máximo aporte
    """

    if language == '':
        query_results = max_input(Total, Lang2)
    else:
        query_results = max_input(Total, language)

    if not query_results.v():
        return 'No hay aporte.'

    query_results = query_results.data[0][0]

    max_input_string = str('Idioma: ' + query_results[1] + ' a: '
                           + query_results[2] + ' con '
                           + str(query_results[0]*100) + '%.')

    return max_input_string
