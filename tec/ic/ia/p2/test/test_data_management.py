# -----------------------------------------------------------------------------

from pandas import DataFrame
from unittest import TestCase
from ..model.data_management import *

# -----------------------------------------------------------------------------


class TestDataManagement(TestCase):

    """
    Clase encargada de probar funciones y fragmentos importantes de
    código para el modulo model.data_management
    """

    # -------------------------------------------------------------------------

    def test_get_lang_rows(self):

        """
        Prueba del correcto resultado de la función para obtener las filas
        de un dataframe correspondientes a un lenguaje
        :param None: No aplica
        :return Sin retorno
        """

        tsv_data = [
            ['aaq: Pawanobskewi', 'rel:etym', 'eng: Penobscot'],
            ['aaq: senabe', 'rel:etym', 'eng: sannup'],
            ['abe: waniigan', 'rel:etym', 'eng: wangan'],
            ['abe: waniigan', 'rel:etym', 'eng: wannigan'],
            ['abs: beta', 'rel:etym', 'zsm: beta']
        ]

        dataframe = DataFrame(tsv_data)

        obtained_data = get_lang_rows(dataframe, 'abe')
        expected_data = dataframe.iloc[2:4]

        self.assertTrue(obtained_data.equals(expected_data))

    def test_get_relations_rows(self):
        """
        Prueba del correcto resultado de la función para obtener las filas
        de un dataframe correspondientes a la relación 'derived_from'
        :param None: No aplica
        :return Sin retorno
        """
        tsv_data = [
            ['aaq: Pawanobskewi', 'rel:etym', 'eng: Penobscot'],
            ['aaq: senabe', 'rel:derived_from', 'eng: sannup'],
            ['abe: waniigan', 'rel:derived_from', 'eng: wangan'],
            ['abe: waniigan', 'rel:etym', 'eng: wannigan'],
            ['abs: beta', 'rel:has_derived_form', 'zsm: beta']
        ]

        dataframe = DataFrame(tsv_data)

        obtained_data = get_relations_rows(dataframe, ['derived_from', 'etym'])
        expected_data = dataframe.iloc[0:4]  # Se espera obtener filas 0 1 2 3

        result1 = obtained_data.equals(expected_data)

        obtained_data = get_relations_rows(dataframe, [])
        expected_data = dataframe  # Se espera obtener todos el dataframe

        result2 = obtained_data.equals(expected_data)

        overall_results = result1 and result2

        self.assertTrue(overall_results)

    def test_assert_facts_from_dataframe(self):

        """
        Prueba del correcto resultado de la función para insertar hechos a
        la base de conocimiento según las filas de un dataframe
        :param None: No aplica
        :return Sin retorno
        """

        tsv_data = [
            ['abe: waniigan', 'rel:etym', 'eng: wannigan'],
            ['abs: beta', 'rel:etym', 'zsm: beta']
        ]

        dataframe = DataFrame(tsv_data)

        try:
            assert_facts_from_dataframe(dataframe)
            success = True
        except Exception as error:
            success = False

        self.assertTrue(success)
