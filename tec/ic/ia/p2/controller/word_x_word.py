# -----------------------------------------------------------------------------

from model.word_x_word import *

# TODO: Hechos para probar la interfaz gráfica
+ etymology("-", "padre", "-", "ego")
+ is_derived_from("-", "ego", "-", "padre")
+ etymological_origin_of("-", "ego", "-", "padre")
+ has_derived_form("-", "tatarabuelo", "-", "bisabuelo")
+ has_derived_form("-", "tatarabuelo", "-", "tio_bisabuelo")
+ has_derived_form("-", "tio_bisabuelo", "-", "tio_abuelo_seg")
+ has_derived_form("-", "tio_abuelo_seg", "-", "tio_ter")
+ has_derived_form("-", "tio_ter", "-", "primo_ter")
+ has_derived_form("-", "bisabuelo", "-", "abuelo")
+ has_derived_form("-", "bisabuelo", "-", "tio_abuelo")
+ has_derived_form("-", "abuelo", "-", "padre")
+ has_derived_form("-", "abuelo", "-", "tio")
+ has_derived_form("-", "padre", "-", "ego")
+ has_derived_form("-", "padre", "-", "hermano")
+ has_derived_form("-", "tio", "-", "primo")
+ has_derived_form("-", "tio_abuelo", "-", "tio_seg")
+ has_derived_form("-", "tio_seg", "-", "primo_seg")

# -----------------------------------------------------------------------------

def exec_are_siblings(first_word, second_word):
    answer = are_siblings(first_word, second_word, R).v()[0]
    return "SI" if answer else "NO"

# -----------------------------------------------------------------------------

def exec_are_cousins(first_word, second_word):
    answer = are_cousins(first_word, second_word, R).v()[0]
    return "SI" if answer else "NO"

# -----------------------------------------------------------------------------

def exec_is_child(parent_word, child_word):
    answer = is_child(parent_word, child_word, R).v()[0]
    return "SI" if answer else "NO"

# -----------------------------------------------------------------------------

def exec_is_uncle(uncle_word, nephew_word):
    answer = is_uncle(uncle_word, nephew_word, R).v()[0]
    return "SI" if answer else "NO"

# -----------------------------------------------------------------------------

def exec_cousins_level(first_word, second_word):
    level = cousins_level(first_word, second_word, L).v()[0]
    return "No son primos" if level is 0 else "Son primos " + str(level) + "°"

# -----------------------------------------------------------------------------

