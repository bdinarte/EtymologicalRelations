# -----------------------------------------------------------------------------

import logging
from model.word_x_word import *

# pyEngine.Logging = True
# logging.basicConfig(level=logging.DEBUG)

# -----------------------------------------------------------------------------
#
#             Árbol de pruebas utilizado para la relaciones de
#             is_child, siblings, uncle, cousins, cousin_grade
#
#                 <tatarabuelo>
#                     __\______________
#                    |                 \
#             <tio_bisabuelo>      <bisabuelo>
#                 /                _____\_________
#        <tio_abuelo_seg>         |               \
#              |            <tio_abuelo>        <abuelo>
#         <tio_ter>            /             _______\_____
#            |            <tio_seg>         |             \
#      <primo_ter>           |            <tio>         <padre>
#                       <primo_seg>        |           _____\_____
#                                       <primo>        \          \
#                                                   <hermano>   <ego X>
#
# -----------------------------------------------------------------------------

def setup_module(module):
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

def test_siblings():

    answer = siblings(X, Y).data

    expected = [
        ("ego", "hermano"),
        ("tio_abuelo", "abuelo"),
        ("hermano", "ego"),
        ("bisabuelo", "tio_bisabuelo"),
        ("tio", "padre"),
        ("abuelo", "tio_abuelo"),
        ("tio_bisabuelo", "bisabuelo"),
        ("padre", "tio")
    ]

    assert set(answer) == set(expected)

# -----------------------------------------------------------------------------

def test_cousins():
    answer = cousins("ego", Y).data
    expected = [("primo_ter",), ("primo",), ("primo_seg",)]
    assert set(answer) == set(expected)

# -----------------------------------------------------------------------------

def test_child_has_parent():
    answer = child("ego", P).data
    expected = [("padre",)]
    assert set(answer) == set(expected)

# -----------------------------------------------------------------------------

def test_child_has_no_parent():
    answer = child("tatarabuelo", P).data
    assert set(answer) == set([])

# -----------------------------------------------------------------------------

def test_uncle():

    answer = uncle(T, "ego").data
    print(answer)

    expected = [
        ("tio",),
        ("tio_seg",),
        ("tio_abuelo",),
        ("tio_abuelo_seg",),
        ("tio_bisabuelo",),
        ("tio_ter",)
    ]

    assert set(answer) == set(expected)

# -----------------------------------------------------------------------------

def test_cousins_level():
    answer = cousins_level("ego", Y, L).data
    expected = [("primo", 1), ("primo_seg", 2), ("primo_ter", 3),]
    assert set(answer) == set(expected)

# -----------------------------------------------------------------------------