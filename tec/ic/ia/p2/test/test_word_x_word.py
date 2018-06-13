# -----------------------------------------------------------------------------

import pytest
from controller.word_x_word import *

# -----------------------------------------------------------------------------
#
#             Árbol de pruebas utilizado para la relaciones de
#             is_child, siblings, uncle, cousins, cousin_grade
#
#                 <tatarabuelo TTA>
#                     __\______________
#                    |                 \
#           <tio_bisabuelo TB>    <bisabuelo B>
#                 /                _____\_________
#      <tio_abuelo_seg TAS>       |               \
#              |            <tio_abuelo TA>   <abuelo A>
#       <tio_ter TT>           /             _______\_____
#            |          <tio_seg TS>        |             \
#      <primo_ter PT>        |           <tio T>       <padre P>
#                     <primo_seg PS>       |           _____\_____
#                                      <primo PR>      \          \
#                                                 <hermano H>  <persona X>
#
# -----------------------------------------------------------------------------

def setup_module(module): # Debe llamarse así

    + etymology("-", "padre P", "-", "persona X")
    + is_derived_from("-", "persona X", "-", "padre T")
    + etymological_origin_of("-", "persona X", "-", "padre P")
    + has_derived_form("-", "tatarabuelo TTA", "-", "bisabuelo B")
    + has_derived_form("-", "tatarabuelo TTA", "-", "tio_bisabuelo TB")
    + has_derived_form("-", "tio_bisabuelo TB", "-", "tio_abuelo_seg TAS")
    + has_derived_form("-", "tio_abuelo_seg TAS", "-", "tio_tercero TT")
    + has_derived_form("-", "tio_tercero TT", "-", "primo_ter PT")
    + has_derived_form("-", "bisabuelo B", "-", "abuelo A")
    + has_derived_form("-", "bisabuelo B", "-", "tio_abuelo TA")
    + has_derived_form("-", "abuelo A", "-", "padre P")
    + has_derived_form("-", "abuelo A", "-", "tio T")
    + has_derived_form("-", "padre P", "-", "persona X")
    + has_derived_form("-", "padre P", "-", "hermano H")
    + has_derived_form("-", "tio T", "-", "primo PR")
    + has_derived_form("-", "tio_abuelo TA", "-", "tio_seg TS")
    + has_derived_form("-", "tio_seg TS", "-", "primo_seg PS")

# -----------------------------------------------------------------------------

def test_are_siblings_positive():
    self.assertTrue(exec_are_siblings("persona X", "hermano H") ==
            exec_are_siblings("abuelo A", "tio_abuelo TA") == True)

def test_are_siblings_negative():
    assert (exec_are_siblings(" ", " ") ==
            exec_are_siblings(" ", "tio_abuelo TA") ==
            exec_are_siblings("hermano H", "primo PR") == False)

# -----------------------------------------------------------------------------

# def test_are_cousins_positivee():
#     assert 1 == 1

#     # print("cousins('primo_ter PT', 'persona X', R)")
#     # print(are_cousins("primo_ter PT", "persona X", R))
#     #
#     # print("cousins('hermano H', 'persona X', R)")
#     # print(are_cousins("hermano H", "persona X", R))
#     #
#     # print("cousins(X, 'primo PR')")
#     # print(cousins(X, "primo PR"))
#     #
#     # print("cousins('persona X', X)")
#     # print(cousins("persona X", X))
#     #
#     # print("cousins(None, X)")
#     # print(cousins(None, X))

    # print(exec_are_cousins('primo PR', 'hermano H'))
    # assert (exec_are_cousins("primo PR", "persona X") ==
    #         exec_are_cousins("primo_ter PT", "hermano H") ==
    #         exec_are_cousins("abuelo A", "tio_abuelo TB") == True)

# -----------------------------------------------------------------------------

# def test_is_child_positive():
#     assert exec_is_child("persona X", "padre P") == True
#
# def test_is_child_negative():
#     assert (exec_is_child(" ", " ") ==
#             exec_is_child(" ", "padre P") ==
#             exec_is_child("persona X", "primo PR") == False)
#
# # -----------------------------------------------------------------------------
#
# def test_is_uncle_positive():
#     print(uncle("tio T", X))
#     # assert exec_is_uncle("tio T", "persona X") == True
# #
# # def test_is_uncle_negative():
# #     assert 1 == 1
#
# # -----------------------------------------------------------------------------
#
# def test_cousins_grade():
#     assert 1 == 1

# -----------------------------------------------------------------------------