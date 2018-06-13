

from ..controller.lang_x_lang import *


# ----------------------------------------------------------------------------
# ------ Definición del KB con el que se generan las pruebas unitarias -------
# ----------------------------------------------------------------------------


def setup_module(module):
    + etymology('abs', 'beta', 'zsm', 'beta')
    + etymology('aaq', 'prueba1', 'eng', 'prueba1')
    + etymology('aaq', 'senabe', 'eng', 'sannup')
    + etymological_origin_of('abe', 'waniigan', 'eng', 'waniigan')
    + etymological_origin_of('aaq', 'prueba2', 'eng', 'prueba2')


# ----------------------------------------------------------------------------


def test_words_in_common():

    """
    Prueba de la función para obtener las palabras en común entre dos
    lenguajes
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_results = set(words_in_common('aaq', 'eng'))
    expected_results = {'prueba1', 'prueba2'}
    first_result_success = obtained_results == expected_results

    obtained_results = words_in_common('aaq', 'zsm')
    expected_results = ['No hay palabras en común.']
    second_result_success = obtained_results == expected_results

    assert(first_result_success and second_result_success)


# ----------------------------------------------------------------------------


def test_common_words_count():

    """
    Prueba de la función para obtener la cantidad de palabras en común
    entre dos lenguajes
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_count = common_words_count('aaq', 'eng')
    expected_count = 2
    first_count_success = obtained_count == expected_count

    obtained_count = common_words_count('aaq', 'zsm')
    expected_count = 0
    second_count_success = obtained_count == expected_count

    assert(first_count_success and second_count_success)
