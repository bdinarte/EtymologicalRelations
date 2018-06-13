# -----------------------------------------------------------------------------

from model.word_x_word import *

# -----------------------------------------------------------------------------

def exec_are_siblings(first_word, second_word):
    are_siblings = are_siblings(first_word, second_word, R).v()[0]
    return "SI" if are_siblings else "NO"

# -----------------------------------------------------------------------------

def exec_are_cousins(first_word, second_word):
    are_cousins = are_cousins(first_word, second_word, R).v()[0]
    return "SI" if are_cousins else "NO"

# -----------------------------------------------------------------------------

def exec_is_child(parent_word, child_word):
    is_child = is_child(parent_word, child_word, R).v()[0]
    return "SI" if is_child else "NO"

# -----------------------------------------------------------------------------

def exec_is_uncle(uncle_word, nephew_word):
    is_uncle = is_uncle(uncle_word, nephew_word, R).v()[0]
    return "SI" if is_child else "NO"

# -----------------------------------------------------------------------------

def exec_cousins_level(first_word, second_word):
    level = cousins_level(first_word, second_word, L).v()[0]
    return "No son primos" if level is 0 else "Son primos " + str(level) + "°"

# -----------------------------------------------------------------------------

