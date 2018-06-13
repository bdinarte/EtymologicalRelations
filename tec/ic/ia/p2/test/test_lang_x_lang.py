

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
    + etymology('aaq', 'prueba3', 'eng', 'prueba3')
    + has_derived_form('equ', 'father', 'isd', 'son')
    + has_derived_form('equ', 'father', 'isd', 'son2')
    + etymology('isd', 'son3', 'equ', 'father3')

# ----------------------------------------------------------------------------


def test_words_in_common():

    """
    Prueba de la función para obtener las palabras en común entre dos
    lenguajes
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_results = set(words_in_common('aaq', 'eng'))
    expected_results = {'prueba1', 'prueba2', 'prueba3'}
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
    expected_count = 3
    first_count_success = obtained_count == expected_count

    obtained_count = common_words_count('aaq', 'zsm')
    expected_count = 0
    second_count_success = obtained_count == expected_count

    assert(first_count_success and second_count_success)


# ----------------------------------------------------------------------------


def test_aux_input_words():

    """
    Prueba de la función para obtener las palabras que el primer lenguaje
    aportó al otro
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_results = set(aux_input_words('equ', 'isd'))
    expected_results = {'son', 'son2', 'son3'}
    first_result_success = obtained_results == expected_results

    obtained_results = aux_input_words('abs', 'aaq')
    expected_results = ['El lenguaje no aportó nada.']
    second_result_success = obtained_results == expected_results

    assert(first_result_success and second_result_success)