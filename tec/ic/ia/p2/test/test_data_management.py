
from pandas import DataFrame
from unittest import TestCase
from model.data_management import get_lang_rows, assert_facts_from_dataframe

# -----------------------------------------------------------------------------


class TestDataManagement(TestCase):

    """
    Clase encargada de probar funciones y fragmentos importantes de código para
    el modulo model.data_management
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

        database = DataFrame(tsv_data)

        obtained_data = get_lang_rows(database, 'abe')
        expected_data = database.iloc[2:4]

        self.assertTrue(obtained_data.equals(expected_data))

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
