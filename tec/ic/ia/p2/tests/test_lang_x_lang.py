

from ..model.lang_x_lang import *


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

    obtained_results = lang_common_words('spa', 'lat', Word1)
    obtained_results = [word_tuple[0] for word_tuple in obtained_results.data]
    expected_results = {'padre', 'tio_seg'}

    assert set(obtained_results) == expected_results


def test_words_in_common_dont_exist():

    """
    Prueba de la función para obtener las palabras en común entre dos
    lenguajes que no tienen palabras en común
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_results = lang_common_words('spa', 'ind', Word1).v()
    expected_results = None

    assert obtained_results == expected_results

# ----------------------------------------------------------------------------


def test_count_common_words_count_2():

    """
    Prueba de la función para obtener la cantidad de palabras en común
    entre dos lenguajes que si tienen en común
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_count = (count_lang_common_words['lat', 'spa'] == Total).v()[0]
    expected_count = 2

    assert obtained_count == expected_count


def test_count_common_words_count_0():

    """
    Prueba de la función para obtener la cantidad de palabras en común
    entre dos lenguajes que no tienen en común
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_count = (count_lang_common_words['spa', 'nor'] == Total).v()
    expected_count = None

    assert obtained_count == expected_count


# ----------------------------------------------------------------------------


def test_aux_input_words_existing():

    """
    Prueba de la función para obtener las palabras que el primer lenguaje
    aportó al otro
    Entradas: No aplica
    @return Sin retorno
    """
    obtained_results = input_words('chi', Word1, 'por', Word2)
    obtained_results = [word_tuple[1] for word_tuple in obtained_results.data]
    expected_results = {'ego', 'tio_ter', 'padre'}

    assert set(obtained_results) == expected_results


def test_aux_input_words_not_existing():
    """
        Prueba de la función para obtener las palabras que el primer lenguaje
        aportó al otro cuando no hay aporte
        Entradas: No aplica
        @return Sin retorno
        """

    obtained_results = input_words('nor', Word1, 'spa', Word2).v()
    expected_results = None

    assert obtained_results == expected_results


# ----------------------------------------------------------------------------


def test_aux_count_input_words_count_3():

    """
    Prueba de la función para obtener la cantidad de palabras que el primer
    lenguaje aportó al otro
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_count = (count_input_words['chi', 'por'] == Total).v()[0]
    expected_count = 3

    assert obtained_count == expected_count


def test_aux_count_input_words_count_0():

    """
    Prueba de la función para obtener la cantidad de palabras que el primer
    lenguaje aportó al otro
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_count = (count_input_words['nor', 'spa'] == Total).v()
    expected_count = None

    assert obtained_count == expected_count


# ----------------------------------------------------------------------------


def test_aux_count_words_received_count_5():

    """
    Prueba de la función para obtener la cantidad de palabras que cualquier
    lenguaje aportó al segundo
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_count = (count_words_received['por'] == Total).v()[0]
    expected_count = 5

    assert obtained_count == expected_count


def test_aux_count_words_received():

    """
    Prueba de la función para obtener la cantidad de palabras que cualquier
    lenguaje aportó al segundo
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_count = (count_words_received['chi'] == Total).v()
    expected_count = None

    assert obtained_count == expected_count


# ----------------------------------------------------------------------------


def test_aux_input_percent_60():
    """
    Prueba de la función para obtener el porcentaje que un lenguaje aportó
    al segundo
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_percent = (input_percent['chi', 'por'] == Percent).v()[0]
    expected_percent = 0.6

    assert obtained_percent == expected_percent


def test_aux_input_percent_0():
    """
    Prueba de la función para obtener el porcentaje que un lenguaje aportó
    al segundo
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_percent = (input_percent['ita', 'chi'] == Percent).v()
    expected_percent = None

    assert obtained_percent == expected_percent


# ----------------------------------------------------------------------------


def test_get_all_lang_inputs_for_all():
    """
    Prueba de la función para obtener los porcentajes que cada lenguaje aportó
    a los otros
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_results = all_lang_inputs(Lang1, Lang2, Total).data
    expected_results = {('lat', 'ita', 0.5),
                         ('lat', 'ape', 0.3333333333333333),
                         ('chi', 'nor', 1.0),
                         ('por', 'ape', 0.3333333333333333),
                         ('por', 'lat', 1.0),
                         ('ind', 'ind', 1.0),
                         ('ind', 'por', 0.2),
                         ('nor', 'ita', 0.5),
                         ('spa', 'por', 0.2),
                         ('spa', 'spa', 0.3333333333333333),
                         ('ind', 'ape', 0.3333333333333333),
                         ('por', 'spa', 0.3333333333333333),
                         ('chi', 'spa', 0.3333333333333333),
                         ('chi', 'por', 0.6)}

    assert set(obtained_results) == expected_results


def test_get_all_lang_inputs_for_one():
    """
    Prueba de la función para obtener los porcentajes que cada lenguaje aportó
    a uno específico
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_results = all_lang_inputs(Lang1, 'por', Total).data
    expected_results = {('ind', 0.2), ('spa', 0.2), ('chi', 0.6)}

    assert set(obtained_results) == expected_results


def test_get_all_lang_inputs_no_input():
    """
    Prueba de la función para obtener los porcentajes que cada lenguaje aportó
    a un lenguaje que no recibió aportes
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_results = all_lang_inputs(Lang1, 'chi', Total).data
    expected_results = []

    assert obtained_results == expected_results


# ----------------------------------------------------------------------------


def test_get_max_input_for_all():
    """
    Prueba de la función para obtener el máximo de los porcentajes que cada
    lenguaje aportó a los otros
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_max = max_input(Total, Lang2).data[0][0]
    expected_max = (1.0, 'por', 'lat')

    assert obtained_max == expected_max


def test_get_max_input_for_one():
    """
    Prueba de la función para obtener el máximo de los porcentajes que cada
    lenguaje aportó a uno específico
    Entradas: No aplica
    @return Sin retorno
    """
    obtained_max = max_input(Total, 'por').data[0][0]
    expected_max = (0.6, 'chi', 'por')

    assert obtained_max == expected_max


def test_get_max_input_for_one_empty():
    """
    Prueba de la función para obtener el máximo de los porcentajes que cada
    lenguaje aportó a uno específico vacío
    Entradas: No aplica
    @return Sin retorno
    """

    obtained_max = max_input(Total, 'chi').data
    expected_max = []

    assert obtained_max == expected_max
