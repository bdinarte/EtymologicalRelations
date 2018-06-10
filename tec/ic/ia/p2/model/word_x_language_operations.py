from pyDatalog import pyDatalog
from os import path as ospath
from sys import path as syspath

from util.file_management import get_etim_database


# -----------------------------------------------------------------------------

"""
Lectura de la BD de pruebas y creación de los hechos
para posteriormente utilizarlos

rel:
etymological_origin_of
has_derived_form
is_derived_from
etymology 
"""

mainfile_path = ospath.abspath(__file__)
base_path = ospath.split(mainfile_path)[0]
base_path = ospath.split(base_path)[0]
syspath.append(base_path)

data_df = get_etim_database(base_path, 'etymwn3.tsv')

print('start')
for i, row in data_df.iterrows():
    pyDatalog.assert_fact(row[1][4:],
                          row[0][:3], row[0][5:],
                          row[2][:3], row[2][5:])


# -----------------------------------------------------------------------------

def word_in_language(word, language):
    """
    ● Determinar si una palabra está relacionada con un idioma (Si / No)

    :param word: <string> indica la palabra utilizada para
    encontrar una posible existencia en el idioma <language>
    :param language: <string> para indicar el idioma sobre el que
    se determinará la existencia de la palabra <word>
    :return: <booleano> para indicar si la palabra tiene relación o no
    con el idioma
    """

    question = "is_derived_from(" + language + ",X,_," + word + ")"

    return pyDatalog.ask(question)


# -----------------------------------------------------------------------------

def set_of_words_in_language(word, language):
    """
    ● Obtener el conjunto de todas las palabras en un idioma originadas
    por una palabra específica (e.g. una palabra específica en latín puede
    originar múltiples palabras en español)

    :param word: <string> indica la palabra utilizada para
    encontrar el conjunto de palabras que genera en un idioma <language>
    :param language: <string> indica el idioma sobre el que se determinará
    la existencia del conjunto de palabras
    :return: <array> con el conjunto de palabras en un idioma
    que pueden ser generadas por una palabra específica
    """

    question = "is_derived_from(" + language + ",X,_," + word + ")"

    return pyDatalog.ask(question)


# -----------------------------------------------------------------------------

def set_of_languages_x_word(word):
    """
    ● Listar los idiomas relacionados con una palabra

    :param word: <string> de la palabra sobre la cual se determinaran
    los idiomas que la misma genera
    :return: <array> del conjunto de idiomas que estan relacionados
    con una palabra en específico
    """

    question = "is_derived_from(" + 'afr' + ",X,_," + word + ")"

    return pyDatalog.ask(question)


# -----------------------------------------------------------------------------
# PRUEBAS DE LAS FUNCIONES
# -----------------------------------------------------------------------------
word_aux = 'aand'
language_aux = 'afr'

print(word_in_language(word_aux, language_aux))
print(set_of_words_in_language(word_aux, language_aux))
print(set_of_languages_x_word(word_aux))
