

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
    + etymological_origin_of('sas', 'mom', 'isd', 'son4')
    + has_derived_form('sss', 'mom', 'isd', 'son5')
    + etymologically_related('lla','ma','alp','aca')

# ----------------------------------------------------------------------------


def test_words_in_common():

    """
    Prueba de la función para obtener las palabras en común entre dos
    lenguajes
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_results = words_in_common('aaq', 'eng')
    expected_results = {'prueba1', 'prueba2', 'prueba3'}
    first_result_success = obtained_results == expected_results

    obtained_results = words_in_common('aaq', 'zsm')
    expected_results = {'No hay palabras en común.'}
    second_result_success = obtained_results == expected_results

    assert first_result_success and second_result_success


# ----------------------------------------------------------------------------


def test_count_common_words():

    """
    Prueba de la función para obtener la cantidad de palabras en común
    entre dos lenguajes
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_count = count_common_words('aaq', 'eng')
    expected_count = 3
    first_count_success = obtained_count == expected_count

    obtained_count = count_common_words('aaq', 'zsm')
    expected_count = 0
    second_count_success = obtained_count == expected_count

    assert first_count_success and second_count_success


# ----------------------------------------------------------------------------


def test_aux_input_words():

    """
    Prueba de la función para obtener las palabras que el primer lenguaje
    aportó al otro
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_results = aux_input_words('equ', 'isd')
    expected_results = {'son', 'son2', 'son3'}
    first_result_success = obtained_results == expected_results

    obtained_results = aux_input_words('abs', 'aaq')
    expected_results = {'El lenguaje no aportó nada.'}
    second_result_success = obtained_results == expected_results

    assert first_result_success and second_result_success


# ----------------------------------------------------------------------------


def test_aux_count_input_words():

    """
    Prueba de la función para obtener la cantidad de palabras que el primer
    lenguaje aportó al otro
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_count = aux_count_input_words('equ', 'isd')
    expected_count = 3
    first_count_success = obtained_count == expected_count

    obtained_count = count_common_words('abs', 'aaq')
    expected_count = 0
    second_count_success = obtained_count == expected_count

    assert first_count_success and second_count_success


# ----------------------------------------------------------------------------


def test_aux_count_words_received():

    """
    Prueba de la función para obtener la cantidad de palabras que cualquier
    lenguaje aportó al segundo
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_count = aux_count_words_received('isd')
    expected_count = 5
    first_count_success = obtained_count == expected_count

    obtained_count = count_common_words('abs', 'aaq')
    expected_count = 0
    second_count_success = obtained_count == expected_count

    assert first_count_success and second_count_success


# ----------------------------------------------------------------------------


def test_aux_input_percent():
    """
    Prueba de la función para obtener el porcentaje que un lenguaje aportó
    al segundo
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_percent = aux_input_percent('equ', 'isd')
    expected_percent = 0.6
    first_result_success = obtained_percent == expected_percent

    obtained_percent = count_common_words('abs', 'aaq')
    expected_percent = 0
    second_result_success = obtained_percent == expected_percent

    assert first_result_success and second_result_success


# ----------------------------------------------------------------------------


def test_get_all_lang_inputs():
    """
    Prueba de la función para obtener los porcentajes que cada lenguaje aportó
    a los otros
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_results = get_all_lang_inputs()
    expected_results = ['sss aporta a isd un 20.0%.',
                        'equ aporta a isd un 60.0%.',
                        'sas aporta a isd un 20.0%.',
                        'aaq aporta a eng un 50.0%.',
                        'abe aporta a eng un 50.0%.',
                        'eng aporta a aaq un 100.0%.',
                        'zsm aporta a abs un 100.0%.']

    assert obtained_results == expected_results


# ----------------------------------------------------------------------------


def test_get_max_input():

    assert True