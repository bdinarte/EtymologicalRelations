
from unittest import TestCase

from model.word_x_lang import *
from pyDatalog import pyDatalog

# -----------------------------------------------------------------------------
# ------- Definición del KB con el que se generan las pruebas unitarias -------
# -----------------------------------------------------------------------------



# -----------------------------------------------------------------------------

class TestWordLang(TestCase):

    """
    Clase encargada de probar funciones y fragmentos importantes de código para
    el modulo model.word_x_lang
    """

    # -------------------------------------------------------------------------

    def test_word_related_language_true(self):

        """
        Descripción

        Entradas: No aplica
        @return Sin retorno
        """

        word_aux = '-lik'
        language_aux = 'afr'

        answer = word_related_language(word_aux, language_aux)

        self.assertTrue(answer)

    # -------------------------------------------------------------------------

    def test_word_related_language_false(self):
        """
        Descripción

        Entradas: No aplica
        @return Sin retorno
        """

        word_aux = 'hola'
        language_aux = 'afr'

        answer = word_related_language(word_aux, language_aux)

        self.assertFalse(answer)

    # -------------------------------------------------------------------------

    def test_set_of_words_in_language(self):
        """
        Descripción

            wetlik
            tydelik
            persoonlik
            wetenskaplik

        Entradas: No aplica
        @return Sin retorno
        """

        word_aux = '-lik'
        language_aux = 'afr'

        words_aux = set_of_words_in_language(word_aux, language_aux)

        words = [i[0] for i in words_aux.data]
        expected_words = ['persoonlik', 'tydelik', 'wetlik', 'wetenskaplik']

        # Se ordenan las listas para que funcione el assert, pues no siempre
        # tienen el mismo orden al ejecutar set_of_words_in_language
        words.sort()
        expected_words.sort()

        self.assertEqual(words, expected_words)

    # -------------------------------------------------------------------------

    def test_set_of_languages_related_word(self):
        """
        Descripción

        Entradas: No aplica
        @return Sin retorno
        """

        """
        afr: -lik	rel:etymological_origin_o   eng: persoonlik
        afr: -lik	rel:etymological_origin_o   afr: tydelik
        afr: -lik	rel:etymological_origin_o   zsm: wetenskaplik
        afr: -lik	rel:etymological_origin_o   afr: wetlik
        afr: -lik	rel:has_derived_form    afr: wetenskaplik
        afr: -tjie	rel:etymological_origin_o   afr: dogtertjie
        afr: -tjie	rel:etymological_origin_o   afr: seuntjie
        afr: -tji   rel:etymological_origin_o   afr: uitjie
        afr: Afrikaner	rel:etymological_origin_o   por: africâner
        por: lan    rel:has_derived_form    ita: April
        ita: April	rel:has_derived_form    afr: -lik
        zsm: wetenskaplik    rel:etymological_origin_   spa: tydelik

        --- Abajo ---
        afr 
        zsm spa
        eng

        --- Arriba ---
        ita por
        """

        word_aux = '-lik'
        language_aux = 'afr'

        langs_aux = set_of_languages_related_word(word_aux)
        langs = [i[0] for i in langs_aux.data]
        expected_langs = ['ita', 'afr', 'zsm', 'eng']

        langs.sort()
        expected_langs.sort()

        self.assertEqual(langs, expected_langs)

if __name__ == '__main__':
    unittest.main()
