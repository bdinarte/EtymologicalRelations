# -----------------------------------------------------------------------------

import pandas as pd
from pyDatalog import pyDatalog

# -----------------------------------------------------------------------------

pyDatalog.create_terms("LX, X, LY, Y, R, "
                       "has_derived_form, is_derived_from, "
                       "etymology, etymological_origin_of, is_son")

# "beeste" es hijo de "bees"
+ has_derived_form("afr", "bees", "afr", "beeste")

# Todas las reglas has_derived_form tienen como contrario
# is_derived_from
+ is_derived_from("afr", "beeste", "afr", "bees")

# "aktinium" es hijo de "actininum"
+ etymology("afr", "aktinium", "nld", "actinium")

# "verbuiging" es hijo de "-ing"
+ etymological_origin_of("afr", "-ing", "afr", "verbuiging")

# X = Primera palabra
# Y = Segunda palabra
# True es que X si es hija de Y

is_son(X, Y, True) <= is_son(X, Y)
is_son(X, Y, False) <= ~is_son(X, Y, True)

is_son(X, Y) <= etymology(LX, X, LY, Y)
is_son(X, Y) <= etymological_origin_of(LY, Y, LX, X)
is_son(X, Y) <= has_derived_form(LY, Y, LX, X)
is_son(X, Y) <= is_derived_from(LX, X, LY, Y)

print("is_son('beeste', 'bees', R)")
print(is_son("beeste", "bees", R))

print("is_son('aktinium', 'actinium', R)")
print(is_son("aktinium", "actinium", R))

print("is_son('verbuiging', '-ing', R) == [(True, )]")
print(is_son("verbuiging", "-ing", R) == [(True, )])

# -----------------------------------------------------------------------------
#
# pyDatalog.create_terms("P, are_siblings")
#
# # "persoonlik" y "tydelik" son hijos de "-lik".
# + etymological_origin_of("afr", "-lik", "afr", "persoonlik")
# + etymological_origin_of("afr", "-lik", "afr", "tydelik")
#
# # 2 Palabras que son hijas de "aand"
# + has_derived_form("afr", "aand", "afr", "aandete")
# + has_derived_form("afr", "aand", "afr", "aandjie")
#
# + is_derived_from("afr", "aandjete", "afr", "aand")
#
# are_siblings(X, Y, False) <= ~are_siblings(X, Y, True)
# are_siblings(X, Y, True) <= are_siblings(Y, X, True)
# are_siblings(X, Y, True) <= is_son(X, P, True) & is_son(Y, P, True) & ~(X == Y)
#
# print("are_siblings('persoonlik', 'tydelik', R)")
# print(are_siblings("persoonlik", "tydelik", R))
#
# print("are_siblings('aandete', 'aandjie', R)")
# print(are_siblings("aandete", "aandjie", R))
#
# print("are_siblings(None, 'aandjie', R)")
# print(are_siblings(None, "aandjie", R))
#
# print("are_siblings('perro', 'gato', R)")
# print(are_siblings("perro", "gato", R))
#
# print("are_siblings(X, Y, R)")
# print(are_siblings(X, Y, True))
#
# # -----------------------------------------------------------------------------
#
# #               [tatarabuelo TTA]
# #               _____\_______________
# #              |                     \
# #     [tio_bisabuelo TB]        [bisabuelo B]
# #             |                  _____\_________
# #    [tio_abuelo_seg TAS]       |               \
# #            |            [tio_abuelo TA]   [abuelo A]
# #     [tio_ter TT]            |            _______\_____
# #                       [tio_seg TS]      |             \
# #                            |         [tio T]       [padre P]
# #                    [primo_seg PS]      |           _____\_____
# #                                    [primo PR]      \          \
# #                                               [hermano H] *[persona X]*
#
# pyDatalog.create_terms("H, P, A, T, PR, B, TA, TS, "
#                        "PS, TTA, TB, TAS, TT, is_uncle")
#
# + has_derived_form(None, "tatarabuelo TTA", None, "tio_bisabuelo TB")
# + has_derived_form(None, "tio_bisabuelo TB", None, "tio_abuelo_seg TAS")
# + has_derived_form(None, "tio_abuelo_seg TAS", None, "tio_tercero TT")
# + has_derived_form(None, "bisabuelo B", None, "abuelo A")
# + has_derived_form(None, "bisabuelo B", None, "tio_abuelo TA")
# + has_derived_form(None, "abuelo A", None, "padre P")
# + has_derived_form(None, "abuelo A", None, "tio T")
# + has_derived_form(None, "padre P", None, "persona X")
# + has_derived_form(None, "padre P", None, "hermano H")
# + has_derived_form(None, "tio T", None, "primo PR")
# + has_derived_form(None, "tio_abuelo TA", None, "tio_seg TS")
# + has_derived_form(None, "tio_seg TS", None, "primo_seg TS")
#
# is_uncle(T, X, False) <= ~is_uncle(T, X, True)
# # is_uncle(TA, X, True) <= is_son(X, P, True) & is_uncle(TA, P, True)
# # is_uncle(TA, X, True) <= is_uncle(T, X, True) & is_uncle(TA, T, True)
# is_uncle(T, X, True) <= are_siblings(P, T, True) & is_son(X, P, True)
# is_uncle(T, X, True) <= is_uncle(T, X, True) & is_uncle(TA, X, True) & is_uncle(TA, T, True)
# # is_uncle(TA, X, True) <= is_son(X, P, True) & is_son(P, A, True) & are_siblings(A, TA, True)
#
# print("is_uncle('tio T', 'persona X', R)")
# print(is_uncle("tio T", "persona X", R))
#
# print("is_uncle('tio_abuelo TA', 'padre P', R)")
# print(is_uncle("tio_abuelo TA", "padre P", R))
#
# print("is_uncle('tio_abuelo TA', 'persona X')")
# print(is_uncle("tio_abuelo TA", "persona X", R))
#
# print("is_uncle('tio_bisabuelo TB', 'persona X')")
# print(is_uncle(X, Y, R))
#
# # tio_bisabuelo TB
#
#
#
# # -----------------------------------------------------------------------------
#
# # if __name__ == '__main__':
# #     print("Fin")
# #     database = get_database()
# #     print(pyDatalog.ask("factorial_of(4, R)"))
# #     print(pyDatalog.ask("factorial[4] == R"))
# #     print(pyDatalog.ask("managers_of('Mary', R)"))
#
# # -----------------------------------------------------------------------------
