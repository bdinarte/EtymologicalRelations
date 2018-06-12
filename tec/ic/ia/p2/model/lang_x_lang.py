# ----------------------------------------------------------------------------

from pyDatalog import pyDatalog
from os import path as ospath
from sys import path as syspath

from ..util.file_management import get_etim_database
from ..model.data_management import assert_facts_from_dataframe

# ----------------------------------------------------------------------------

# Definición de términos comunes a la mayoría de predicados
pyDatalog.create_terms('etymological_origin_of, has_derived_form,'
                       'is_derived_from, etymology, etymologically_related,'
                       'orthography')
pyDatalog.create_terms('Lang1, Lang2, Word1, Word2')

# ----------------------------------------------------------------------------

# Términos para la función words_in_common
pyDatalog.create_terms('lang_common_words')
# Relaciones para la función words_in_common
lang_common_words(Lang1, Word1, Lang2, Word1) <= (
    etymological_origin_of(Lang1, Word1, Lang2, Word1)
)
lang_common_words(Lang1, Word1, Lang2, Word1) <= (
    etymology(Lang1, Word1, Lang2, Word1)
)


def words_in_common(language1, language2):

    if language1 == language2:
        return ['Se ingresó el mismo lenguaje.']

    query_results = lang_common_words(language1, Word1, language2, Word2)

    if not query_results.v():
        return ['No hay palabras en común.']

    existing_words = [word_tuple[0] for word_tuple in list(query_results)]
    return existing_words


# ----------------------------------------------------------------------------

# Términos para la función common_words_count
pyDatalog.create_terms('count_lang_common_words, Total')
# Relaciones para la función words_in_common
(count_lang_common_words[Lang1, Lang2] == len_(Word1)) <= (
    lang_common_words(Lang1, Word1, Lang2, Word1)
)


def common_words_count(language1, language2):

    word_count = count_lang_common_words[language1, language2] == Total

    return word_count.v()[0] if word_count.v() else 0


# ----------------------------------------------------------------------------