# -----------------------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from model.word_x_word import *

# -----------------------------------------------------------------------------

def exec_are_siblings(first_word, second_word):
    """
    Determina si dos palabras son hermanas, es decir,
    tienen un padre en común.
    :param first_word: <string> Palabra 1
    :param second_word: <string> Palabra 2
    :return: True si first_word es hermana de second_word
    """

    return are_siblings(first_word, second_word, R).v()[0]

# -----------------------------------------------------------------------------

def exec_are_cousins(first_word, second_word):
    """
    Determina si dos palabras son primas. Esto es significa que tienen
    al menos un ancestro en común con la misma lejanía y no es el padre
    :param first_word: <string> Palabra 1
    :param second_word: <string> Palabra 2
    :return: True si first_word es prima de second_word
    """

    return are_cousins(first_word, second_word, R).v()[0]

# -----------------------------------------------------------------------------

def exec_is_child(child_word, parent_word):
    """
    Determina si la primera palabra es hija de la segunda. Por ejemplo, al
    decir que la segunda palabra tiene como forma derivada la primera
    :param child_word: <string> Posible palabra derivada
    :param parent_word: <string> Posible palabra de la que se deriva
    :return: True si child_word es hija de parent_word
    """

    return is_child(child_word, parent_word, R).v()[0]

# -----------------------------------------------------------------------------

def exec_is_uncle(uncle_word, nephew_word):
    """
    Determina si la primera palabra es tía de la segunda. En este caso
    se consideran todas las variedades de tíos incluyendo tíos abuelos,
    tios bisabuelos, tios segundos. De forma general se considera como tío
    cualquier ancestro de un primo de nephew_word que no sea ancestros de este.
    :param uncle_word: <string> Posible tío
    :param nephew_word: <string> Posible sobrino
    :return: True si uncle_word si es tío de nephew_word
    """

    return is_uncle(uncle_word, nephew_word, R).v()[0]

# -----------------------------------------------------------------------------

def exec_cousins_distance(first_word, second_word):
    """
    Determina la lejanía entre dos palabras que son primas. Por ejemplo, para
    un primo tercero, la distancia es 3. Si ambas palabras no son primas
    entonces la distancia es cero.
    :param first_word: <string> Palabra 1
    :param second_word: <string> Palabra 2
    :return: 0 si no son primas, sino, la lejanía de primos entre ambas
    """

    result = cousins_distance(first_word, second_word, L)
    return 0 if result == [] else result

# -----------------------------------------------------------------------------

