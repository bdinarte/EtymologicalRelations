

from ..controller.lang_x_lang import *


# ----------------------------------------------------------------------------
# ------ Definición del KB con el que se generan las pruebas unitarias -------
# ----------------------------------------------------------------------------


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

    + etymology_active(True)
    + has_derived_form_active(True)
    + etymological_origin_of_active(True)
    + etymologically_related_active(True)

# ----------------------------------------------------------------------------


def test_words_in_common_exist():

    """
    Prueba de la función para obtener las palabras en común entre dos
    lenguajes que si tienen palabras en común
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_results = words_in_common('spa', 'lat')
    expected_results = {'padre', 'tio_seg'}

    assert obtained_results == expected_results


def test_words_in_common_dont_exist():

    """
    Prueba de la función para obtener las palabras en común entre dos
    lenguajes que no tienen palabras en común
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_results = words_in_common('spa', 'ind')
    expected_results = {'No hay palabras en común.'}

    assert obtained_results == expected_results

# ----------------------------------------------------------------------------


def test_count_common_words_count_2():

    """
    Prueba de la función para obtener la cantidad de palabras en común
    entre dos lenguajes que si tienen en común
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_count = count_common_words('lat', 'spa')
    expected_count = 2

    assert obtained_count == expected_count


def test_count_common_words_count_0():

    """
    Prueba de la función para obtener la cantidad de palabras en común
    entre dos lenguajes que no tienen en común
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_count = count_common_words('spa', 'nor')
    expected_count = 0

    assert obtained_count == expected_count


# ----------------------------------------------------------------------------


def test_aux_input_words_existing():

    """
    Prueba de la función para obtener las palabras que el primer lenguaje
    aportó al otro
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_results = aux_input_words('chi', 'por')
    expected_results = {'ego', 'tio_ter', 'padre'}

    assert obtained_results == expected_results


def test_aux_input_words_not_existing():
    """
        Prueba de la función para obtener las palabras que el primer lenguaje
        aportó al otro cuando no hay aporte
        Entradas: No aplica
        @return Sin retorno
        """

    obtained_results = aux_input_words('nor', 'spa')
    expected_results = {'El lenguaje no aportó nada.'}

    assert obtained_results == expected_results


# ----------------------------------------------------------------------------


def test_aux_count_input_words_count_3():

    """
    Prueba de la función para obtener la cantidad de palabras que el primer
    lenguaje aportó al otro
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_count = aux_count_input_words('chi', 'por')
    expected_count = 3

    assert obtained_count == expected_count


def test_aux_count_input_words_count_0():

    """
    Prueba de la función para obtener la cantidad de palabras que el primer
    lenguaje aportó al otro
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_count = count_common_words('nor', 'spa')
    expected_count = 0

    assert obtained_count == expected_count


# ----------------------------------------------------------------------------


def test_aux_count_words_received_count_5():

    """
    Prueba de la función para obtener la cantidad de palabras que cualquier
    lenguaje aportó al segundo
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_count = aux_count_words_received('por')
    expected_count = 5

    assert obtained_count == expected_count


def test_aux_count_words_received():

    """
    Prueba de la función para obtener la cantidad de palabras que cualquier
    lenguaje aportó al segundo
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_count = aux_count_words_received('chi')
    expected_count = 0

    assert obtained_count == expected_count


# ----------------------------------------------------------------------------


def test_aux_input_percent_60():
    """
    Prueba de la función para obtener el porcentaje que un lenguaje aportó
    al segundo
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_percent = aux_input_percent('chi', 'por')
    expected_percent = 0.6

    assert obtained_percent == expected_percent


def test_aux_input_percent_0():
    """
    Prueba de la función para obtener el porcentaje que un lenguaje aportó
    al segundo
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_percent = aux_input_percent('ita', 'chi')
    expected_percent = 0
    assert obtained_percent == expected_percent


# ----------------------------------------------------------------------------


def test_get_all_lang_inputs_for_all():
    """
    Prueba de la función para obtener los porcentajes que cada lenguaje aportó
    a los otros
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_results = get_all_lang_inputs()
    expected_results = {'chi aporta a nor un 100.0%.',
                        'chi aporta a por un 60.0%.',
                        'chi aporta a spa un 33.0%.',
                        'ind aporta a ape un 33.0%.',
                        'ind aporta a ind un 100.0%.',
                        'ind aporta a por un 20.0%.',
                        'lat aporta a ape un 33.0%.',
                        'lat aporta a ita un 50.0%.',
                        'nor aporta a ita un 50.0%.',
                        'por aporta a ape un 33.0%.',
                        'por aporta a lat un 100.0%.',
                        'por aporta a spa un 33.0%.',
                        'spa aporta a por un 20.0%.',
                        'spa aporta a spa un 33.0%.'}

    assert obtained_results == expected_results


def test_get_all_lang_inputs_for_one():
    """
    Prueba de la función para obtener los porcentajes que cada lenguaje aportó
    a uno específico
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_results = get_all_lang_inputs('por')
    expected_results = {'chi aporta a por un 60.0%.',
                        'ind aporta a por un 20.0%.',
                        'spa aporta a por un 20.0%.'}

    assert obtained_results == expected_results


def test_get_all_lang_inputs_no_input():
    """
    Prueba de la función para obtener los porcentajes que cada lenguaje aportó
    a un lenguaje que no recibió aportes
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_results = get_all_lang_inputs('chi')
    expected_results = ['No hay aportes.']

    assert obtained_results == expected_results


# ----------------------------------------------------------------------------


def test_get_max_input_for_all():
    """
    Prueba de la función para obtener el máximo de los porcentajes que cada
    lenguaje aportó a los otros
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_max = get_max_input()
    expected_max = 'Idioma: por a: lat con 100.0%.'

    assert obtained_max == expected_max


def test_get_max_input_for_one():
    """
    Prueba de la función para obtener el máximo de los porcentajes que cada
    lenguaje aportó a uno específico
    Entradas: No aplica
    @return Sin retorno
    """
    obtained_max = get_max_input('por')
    expected_max = 'Idioma: chi a: por con 60.0%.'

    assert obtained_max == expected_max


def test_get_max_input_for_one_empty():
    """
    Prueba de la función para obtener el máximo de los porcentajes que cada
    lenguaje aportó a uno específico vacío
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_max = get_max_input('chi')
    expected_max = 'No hay aporte.'

    assert obtained_max == expected_max
