# ----------------------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# ----------------------------------------------------------------------------

from model.lang_x_lang import *
from util.file_management import get_etim_database
from model.data_management import assert_facts_from_dataframe

# ----------------------------------------------------------------------------


def words_in_common(language1, language2):

    if language1 == language2:
        return ['Se ingresó el mismo lenguaje.']

    query_results = lang_common_words(language1, Word1, language2, Word2)

    if not query_results.v():
        return ['No hay palabras en común.']

    existing_words = [word_tuple[0] for word_tuple in query_results.data]
    return existing_words


# ----------------------------------------------------------------------------


def common_words_count(language1, language2):

    word_count = count_lang_common_words[language1, language2] == Total

    return word_count.v()[0] if word_count.v() else 0
