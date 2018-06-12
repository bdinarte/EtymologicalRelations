# -----------------------------------------------------------------------------

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
etymologically_related
orthography
"""

mainfile_path = ospath.abspath(__file__)
base_path = ospath.split(mainfile_path)[0]
base_path = ospath.split(base_path)[0]
syspath.append(base_path)

data_df = get_etim_database(base_path, 'etymwn3.tsv')

print('Creating Facts...')
for i, row in data_df.iterrows():
    pyDatalog.assert_fact(row[1][4:],
                          row[0][:3], row[0][5:],
                          row[2][:3], row[2][5:])


# -----------------------------------------------------------------------------
print('Creating Terms...')
# Términos que se usan en este archivo

pyDatalog.create_terms('word_related_lang, set_of_words_in_lang, Word, '
                       'Lang, X, Y, LX, LY, A, B')

pyDatalog.create_terms('etymology, etymological_origin_of,'
                       'etymologically_related, has_derived_form,'
                       'is_derived_from, orthography')

pyDatalog.create_terms("is_son, is_ancestor, is_parent")

# -----------------------------------------------------------------------------

word_related_lang(Word, Lang, True) <= (
    etymology(Lang, Word, X, Y)
)
word_related_lang(Word, Lang, True) <= (
    etymological_origin_of(X, Y, Lang, Word)
)
word_related_lang(Word, Lang, True) <= (
    etymologically_related(Lang, Word, X, Y)
)
word_related_lang(Word, Lang, True) <= (
    has_derived_form(X, Y, Lang, Word)
)
word_related_lang(Word, Lang, True) <= (
    is_derived_from(Lang, Word, X, Y)
)

word_related_lang(Word, Lang, False) <= ~word_related_lang(Word, Lang, True)


def word_related_language(word, language):
    """
    ● Determinar si una palabra está relacionada con un idioma (Si / No)

    :param word: <string> indica la palabra utilizada para
    encontrar una posible existencia en el idioma <language>
    :param language: <string> para indicar el idioma sobre el que
    se determinará la existencia de la palabra <word>
    :return: <booleano> para indicar si la palabra tiene relación o no
    con el idioma
    """

    query = word_related_lang(word, language, Y)
    value = query.v()[0]
    return value


# -----------------------------------------------------------------------------

# X = Primera palabra
# Y = Segunda palabra
# True es que X si es hija de Y
is_son(X, Y, LX, True) <= is_son(X, Y, LX)
is_son(X, Y, LX, False) <= ~is_son(X, Y, LX)

is_son(X, Y, LX) <= etymology(LX, X, LY, Y)
is_son(X, Y, LX) <= etymological_origin_of(LY, Y, LX, X)
is_son(X, Y, LX) <= has_derived_form(LY, Y, LX, X)
is_son(X, Y, LX) <= is_derived_from(LX, X, LY, Y)

# -----------------------------------------------------------------------------
# Pruebas para is_ancestor e is_parent
# -----------------------------------------------------------------------------

is_parent(X, Y, LX) <= is_son(Y, X, LX)

is_ancestor(A, LX, B) <= is_parent(A, B, LX)
is_ancestor(X, LX, Y) <= is_parent(X, A, LX) & is_ancestor(A, LX, Y)


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

    query = is_ancestor(word, language, X)

    return query


# -----------------------------------------------------------------------------

def set_of_languages_related_word(word):
    """
    ● Listar los idiomas relacionados con una palabra

    :param word: <string> de la palabra sobre la cual se determinaran
    los idiomas que la misma genera
    :return: <array> del conjunto de idiomas que estan relacionados
    con una palabra en específico
    """

    question = "etymology(X,"+word+",Y,Z)"
    answer = pyDatalog.ask(question)

    set_of_langs = []
    if answer:
        for i in answer.answers:
            set_of_langs.append(i[0])

    return list(set(set_of_langs))


# -----------------------------------------------------------------------------
# PRUEBAS DE LAS FUNCIONES
# -----------------------------------------------------------------------------
word_aux = 'aand'
language_aux = 'afr'

# -------------------------------------------
print('\n** word_related_language... **')
answer = word_related_language(word_aux, language_aux)

confirm = 'SI' if answer else 'NO'
resp = "La palabra '%s' %s está relacionada con el lenguaje '%s'"\
       % (word_aux, confirm, language_aux)
print(resp)

# -------------------------------------------
print('\n** set_of_words_in_language... **')
words_aux = set_of_words_in_language(word_aux, language_aux)

words_aux = words_aux.data
if len(words_aux) > 0:
    resp = "La palabra '%s' genera las siguientes palabras" \
           " en el lenguaje '%s':" % (word_aux, language_aux)
    print(resp)
    for i in words_aux:
        print('\t%s' %i)
else:
    resp = "La palabra '%s' no genera ninguna otra en el lenguaje '%s'" \
           % (word_aux, language_aux)
    print(resp)

# -------------------------------------------
print('\n** set_of_languages_related_word... **')
langs_aux = set_of_languages_related_word(word_aux)

if len(langs_aux) > 0:
    resp = "La palabra '%s' está relacionada con los siguientes idiomas:" \
           % word_aux
    print(resp)
    print('\t%s' % '\n\t'.join(map(str, langs_aux)))
else:
    resp = "La palabra '%s' no está relacionada con ningún idioma" \
           % word_aux
    print(resp)
