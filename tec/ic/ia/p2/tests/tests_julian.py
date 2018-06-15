# -----------------------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from model.word_x_word import *

# -----------------------------------------------------------------------------
#
#                <ind:tatarabuelo>
#                   ____\_____________
#                  |                  \
#         <ind:tio_bisabuelo>    <por:bisabuelo>
#                 |                 ____\_____________
#                |                 |                  \
#      <chi:tio_abuelo_seg> <spa:tio_abuelo>    <chi:abuelo>
#              |                 |             ________\______
#             |                 |             |               \
#      <por:tio_ter>     <lat:tio_seg>    <nor:tio>       <lat:padre>
#           |                 |              |            _____\_______
#           \                 \              \            \            \
#     <lat:primo_ter>   <ita:primo_seg>   <ita:primo>  <ape:hermano>  <spa:ego>
#
# -----------------------------------------------------------------------------

+ etymology("lat", "padre", "spa", "ego")
+ etymological_origin_of("spa", "ego", "lat", "padre")
+ has_derived_form("ind", "tatarabuelo", "por", "bisabuelo")
+ has_derived_form("ita", "ttatatattaatarabuelo", "ind", "tatarabuelo")
+ has_derived_form("ind", "tio_bisabuelo", "chi", "tio_abuelo_seg")
+ has_derived_form("chi", "tio_abuelo_seg", "por", "tio_ter")
+ has_derived_form("por", "tio_ter", "lat", "primo_ter")
+ has_derived_form("por", "bisabuelo", "chi", "abuelo")
+ has_derived_form("por", "bisabuelo", "spa", "tio_abuelo")
+ has_derived_form("chi", "abuelo", "lat", "padre")
+ has_derived_form("chi", "abuelo", "nor", "tio")
+ has_derived_form("lat", "padre", "ape", "hermano")
+ has_derived_form("nor", "tio", "ita", "primo")
+ has_derived_form("spa", "tio_abuelo", "lat", "tio_seg")
+ has_derived_form("lat", "tio_seg", "ita", "primo_seg")

pyDatalog.create_terms("LA, lang_related_word")

# -----------------------------------------------------------------------------
# Pruebas para is_child
# -----------------------------------------------------------------------------

print("child(X, P)")
print(child(X, P))

# -----------------------------------------------------------------------------
# Pruebas para ancestor e parent
# -----------------------------------------------------------------------------

print("parent(P, X)")
print(parent(P, X))

# -----------------------------------------------------------------------------
# Pruebas para siblings
# -----------------------------------------------------------------------------

print("siblings(X, Y)")
print(siblings(X, Y))

# -----------------------------------------------------------------------------
# Pruebas para ancestor_level
# -----------------------------------------------------------------------------

print("ancestor_level(A, 'ego', L)")
print(ancestor_level(A, "ego", L))

# -----------------------------------------------------------------------------
# Pruebas para cousins
# -----------------------------------------------------------------------------

print("are_cousins(X, Y)")
print(cousins("ego", X))

# -----------------------------------------------------------------------------
# Pruebas para cousins_level
# -----------------------------------------------------------------------------

print("cousins_level('ego', Y, L)")
print(cousins_level("ego", Y, L))


# -----------------------------------------------------------------------------
# Pruebas para uncle
# -----------------------------------------------------------------------------

print("uncle(T, 'ego', R)")
print(uncle(T, "ego"))

# -----------------------------------------------------------------------------

# X proviene de Y.
child(X, Y, LX, LY) <= child(X, Y, LX, LY) & ~(X == Y)
child(X, Y, LX, LY) <= etymology(LY, Y, LX, X)
child(X, Y, LX, LY) <= etymological_origin_of(LX, X, LY, Y)
child(X, Y, LX, LY) <= has_derived_form(LY, Y, LX, X)

# -----------------------------------------------------------------------------

# X es padre de Y.
parent(X, Y, LX, LY) <= child(Y, X, LY, LX)

# -----------------------------------------------------------------------------

# X es ancestro de Y.
ancestor(X, Y, LX, LY) <= parent(X, Y, LX, LY)
ancestor(X, Y, LX, LY) <= parent(X, A, LX, LA) & ancestor(A, Y, LA, LY) & ~(X == Y)

# -----------------------------------------------------------------------------

lang_related_word(X, LX) <= ancestor(X, Y, LX, LY)
lang_related_word(X, LY) <= ancestor(X, Y, LX, LY)
lang_related_word(X, LX) <= ancestor(Y, X, LY, LX)
lang_related_word(X, LY) <= ancestor(Y, X, LY, LX)

print(lang_related_word('abuelo', L))


