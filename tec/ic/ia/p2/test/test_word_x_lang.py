
from ..controller.word_x_lang import *


# -----------------------------------------------------------------------------
# ------- Definición del KB con el que se generan las pruebas unitarias -------
# -----------------------------------------------------------------------------

def setup_module(module):
    + etymology("afr", "Dinsdag", "afr", "dinsdag")
    + etymologically_related('afr', 'aanval', 'afr', 'aanvaller')
    + etymological_origin_of("afr", "-lik", "eng", "persoonlik")
    + etymological_origin_of("afr", "-lik", "afr", "tydelik")
    + etymological_origin_of("afr", "-lik", "zsm", "wetenskaplik")
    + etymological_origin_of("afr", "-lik", "afr", "wetlik")
    + etymological_origin_of("afr", "-tjie", "afr", "dogtertjie")
    + etymological_origin_of("afr", "-tjie", "afr", "seuntjie")
    + etymological_origin_of("afr", "-tji", "afr", "uitjie")
    + etymological_origin_of("afr", "Afrikaner", "por", "africâner")
    + etymological_origin_of("zsm", "wetenskaplik", "spa", "tydelik")
    + has_derived_form("afr", "-lik", "afr", "wetenskaplik")
    + has_derived_form("por", "lan", "ita", "April")
    + has_derived_form("ita", "April", "afr", "-lik")
    + has_derived_form("afr", "Desember", "afr", "Decembermaande")
    + is_derived_from("afr", "Decembermaande", "afr", "Desember")


# -----------------------------------------------------------------------------
# -- Definición de las diferentes pruebas para las funcionalidades word_lang --
# -----------------------------------------------------------------------------

def test_word_related_language_true():

    """
    Descripción

    Entradas: No aplica
    @return Sin retorno
    """

    word_aux = '-lik'
    language_aux = 'afr'

    answer = word_related_language(word_aux, language_aux)

    assert answer

# -------------------------------------------------------------------------

def test_word_related_language_false():
    """
    Descripción

    Entradas: No aplica
    @return Sin retorno
    """

    word_aux = 'hola'
    language_aux = 'afr'

    answer = word_related_language(word_aux, language_aux)

    assert not answer

# -------------------------------------------------------------------------

def test_set_of_words_in_language():
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

    words = set_of_words_in_language(word_aux, language_aux)

    expected_words = ['tydelik', 'wetenskaplik', 'wetlik']

    assert words == expected_words

# -------------------------------------------------------------------------

def test_set_of_languages_related_word():
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

    langs = set_of_languages_related_word(word_aux)

    expected_langs = ['afr', 'eng', 'ita', 'zsm']

    assert langs == expected_langs
