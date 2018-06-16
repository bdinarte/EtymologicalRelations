# ----------------------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# ----------------------------------------------------------------------------

from model.lang_x_lang import *

# ----------------------------------------------------------------------------


def words_in_common(language1, language2):

    if language1 == language2:
        return {'Se ingresó el mismo lenguaje.'}

    query_results = lang_common_words(language1, language2, Word1)

    if not query_results.v():
        return {'No hay palabras en común.'}

    existing_words = [word_tuple[0] for word_tuple in query_results.data]
    return set(existing_words)


# ----------------------------------------------------------------------------


def count_common_words(language1, language2):

    word_count = count_lang_common_words[language1, language2] == Total

    return word_count.v()[0] if word_count.v() else 0


# ----------------------------------------------------------------------------


def aux_input_words(language1, language2):

    query_results = input_words(language1, Word1, language2, Word2)

    if not query_results.v():
        return {'El lenguaje no aportó nada.'}

    existing_words = [word_tuple[1] for word_tuple in query_results.data]
    return set(existing_words)


def aux_count_input_words(language1, language2):

    word_count = count_input_words[language1, language2] == Total

    return word_count.v()[0] if word_count.v() else 0


def aux_count_words_received(language):

    word_count = count_words_received[language] == Total

    return word_count.v()[0] if word_count.v() else 0

# ----------------------------------------------------------------------------


def aux_input_percent(language1, language2):

    percent = input_percent[language1, language2] == Percent

    return percent.v()[0] if percent.v() else 0


# ----------------------------------------------------------------------------


def get_all_lang_inputs(language=''):

    if language == '':
        query_results = all_lang_inputs(Lang1, Lang2, Total)
    else:
        query_results = all_lang_inputs(Lang1, language, Total)

    if not query_results.v():
        return ['No hay aportes.']

    if language == '':
        existing_results = [result[0] + ' aporta a '
                            + result[1] + ' un '
                            + str(round(result[2], 2) * 100) + '%.'
                            for result in query_results.data]
    else:
        existing_results = [result[0] + ' aporta a '
                            + language + ' un '
                            + str(round(result[1], 2) * 100) + '%.'
                            for result in query_results.data]

    return set(existing_results)


# ----------------------------------------------------------------------------


def get_max_input(language=''):

    if language == '':
        query_results = max_input(Total, Lang2)
    else:
        query_results = max_input(Total, language)

    if not query_results.v():
        return 'No hay aporte.'

    max_input_string = str('Idioma: ' + query_results.data[0][0][1] + ' a: '
                           + query_results.data[0][0][2] + ' con '
                           + str(query_results.data[0][0][0]*100) + '%.')

    return max_input_string
