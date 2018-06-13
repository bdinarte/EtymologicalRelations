# -----------------------------------------------------------------------------

from model.word_x_word import *

# -----------------------------------------------------------------------------

def exec_are_siblings(first_word, second_word):
    return are_siblings(first_word, second_word, R).v()[0]

# -----------------------------------------------------------------------------

def exec_are_cousins(first_word, second_word):
    query = are_cousins(first_word, second_word, R)

    return are_cousins(first_word, second_word, R).v()[0]

# -----------------------------------------------------------------------------

def exec_is_child(parent_word, child_word):
    return is_child(parent_word, child_word, R).v()[0]

# -----------------------------------------------------------------------------

def exec_is_uncle(uncle_word, nephew_word):
    return is_uncle(uncle_word, nephew_word, R).v()[0]

# -----------------------------------------------------------------------------

def exec_cousins_level(first_word, second_word):
    return cousins_level(first_word, second_word, L).v()[0]

# -----------------------------------------------------------------------------

