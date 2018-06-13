
from pandas import DataFrame
from unittest import TestCase
from ..controller.lang_x_lang import *

# -----------------------------------------------------------------------------


class TestLangLang(TestCase):

    """
    Clase encargada de probar funciones y fragmentos importantes de código para
    el modulo model.lang_x_lang
    """

    # -------------------------------------------------------------------------

    def test_words_in_common(self):

        """
        Prueba de la función para obtener las palabras en común entre dos
        lenguajes
        Entradas: No aplica
        @return Sin retorno
        """

        tsv_data = [
            ['aaq: prueba1', 'rel:etymology', 'eng: prueba1'],
            ['aaq: senabe', 'rel:etymology', 'eng: sannup'],
            ['abe: waniigan', 'rel:etymological_origin_of', 'eng: waniigan'],
            ['aaq: prueba2', 'rel:etymological_origin_of', 'eng: prueba2'],
            ['abs: beta', 'rel:etymology', 'zsm: beta']
        ]

        dataframe = DataFrame(tsv_data)
        assert_facts_from_dataframe(dataframe)

        obtained_results = set(words_in_common('aaq', 'eng'))
        expected_results = {'prueba1', 'prueba2'}
        first_result_success = obtained_results == expected_results

        obtained_results = words_in_common('aaq', 'zsm')
        expected_results = ['No hay palabras en común.']
        second_result_success = obtained_results == expected_results

        self.assertTrue(first_result_success and second_result_success)

    def test_common_words_count(self):

        """
        Prueba de la función para obtener la cantidad de palabras en común
        entre dos lenguajes
        Entradas: No aplica
        @return Sin retorno
        """

        tsv_data = [
            ['aaq: prueba1', 'rel:etymology', 'eng: prueba1'],
            ['aaq: senabe', 'rel:etymology', 'eng: sannup'],
            ['abe: waniigan', 'rel:etymological_origin_of', 'eng: waniigan'],
            ['aaq: prueba2', 'rel:etymological_origin_of', 'eng: prueba2'],
            ['abs: beta', 'rel:etymology', 'zsm: beta']
        ]

        dataframe = DataFrame(tsv_data)
        assert_facts_from_dataframe(dataframe)

        obtained_count = common_words_count('aaq', 'eng')
        expected_count = 2
        first_count_success = obtained_count == expected_count

        obtained_count = common_words_count('aaq', 'zsm')
        expected_count = 0
        second_count_success = obtained_count == expected_count

        self.assertTrue(first_count_success and second_count_success)
