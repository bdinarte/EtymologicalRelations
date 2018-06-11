# -----------------------------------------------------------------------------

import pandas as pd
from pyDatalog import pyDatalog

# -----------------------------------------------------------------------------

def get_database(filename="B:\\etymwn3.tsv"):
    dataframe = pd.read_csv(filename, sep="\t", header=None)
    return dataframe.values.tolist()

# -----------------------------------------------------------------------------

@pyDatalog.program()
def factorial():
    factorial[N] = N * factorial[N - 1]
    factorial[1] = 1
    factorial_of(X, Y) <= (factorial[X] == Y)

# -----------------------------------------------------------------------------

@pyDatalog.program()
def tutorial():
    manager['Mary'] = 'John'
    manager['Sam'] = 'Mary'
    manager['Tom'] = 'Mary'
    managers_of(X, Y) <= (manager[Y] == X)

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
is_son(X, Y, False) <= ~is_son(X, Y, True)
is_son(X, Y, True) <= etymology(LX, X, LY, Y)
is_son(X, Y, True) <= etymological_origin_of(LY, Y, LX, X)
is_son(X, Y, True) <= has_derived_form(LY, Y, LX, X)
is_son(X, Y, True) <= is_derived_from(LX, X, LY, Y)

print("is_son('beeste', 'bees', R)")
print(is_son("beeste", "bees", R))

print("is_son('aktinium', 'actinium', R)")
print(is_son("aktinium", "actinium", R))

print("is_son('verbuiging', '-ing', R) == [(True, )]")
print(is_son("verbuiging", "-ing", R) == [(True, )])

# -----------------------------------------------------------------------------

pyDatalog.create_terms("P, are_siblings")

# "persoonlik" y "tydelik" son hijos de "-lik".
+ etymological_origin_of("afr", "-lik", "afr", "persoonlik")
+ etymological_origin_of("afr", "-lik", "afr", "tydelik")

# 2 Palabras que son hijas de "aand"
+ has_derived_form("afr", "aand", "afr", "aandete")
+ has_derived_form("afr", "aand", "afr", "aandjie")

+ is_derived_from("afr", "aandjete", "afr", "aand")

are_siblings(X, Y, False) <= ~are_siblings(X, Y, True)
are_siblings(X, Y, True) <= are_siblings(Y, X, True)
are_siblings(X, Y, True) <= is_son(X, P, True) & is_son(Y, P, True) & ~(X == Y)

print("are_siblings('persoonlik', 'tydelik', R)")
print(are_siblings("persoonlik", "tydelik", R))

print("are_siblings('aandete', 'aandjie', R)")
print(are_siblings("aandete", "aandjie", R))

print("are_siblings(None, 'aandjie', R)")
print(are_siblings(None, "aandjie", R))

print("are_siblings('perro', 'gato', R)")
print(are_siblings("perro", "gato", R))

print("are_siblings(X, Y, R)")
print(are_siblings(X, Y, True))

# -----------------------------------------------------------------------------

#                                   [bisabuelo B]
#                            ____________|_____________
#                           |                         |
#                      [abuelo A]              [tio_abuelo TA]
#                   _______|__________               |
#                  |                 |         [tio_seg TS]
#           [padre P]             [tio T]           |
#         _____|_____               |        [primo_seg PS]
#        |          |           [primo PR]
#  [persona X] [hermano H]

pyDatalog.create_terms("A, T, PR, is_cousin, is_uncle")

+ has_derived_form(None, "bisabuelo B", None, "abuelo A")
+ has_derived_form(None, "bisabuelo B", None, "tio_abuelo TA")
+ has_derived_form(None, "abuelo A", None, "padre P")
+ has_derived_form(None, "abuelo A", None, "tio T")
+ has_derived_form(None, "padre P", None, "persona X")
+ has_derived_form(None, "padre P", None, "hermano H")
+ has_derived_form(None, "tio T", None, "primo PR")
+ has_derived_form(None, "tio_abuelo TA", None, "tio_seg TS")
+ has_derived_form(None, "tio_seg TS", None, "primo_seg TS")

is_uncle(T, X, False) <= ~is_uncle(T, X, True)
is_uncle(T, X, True) <= is_son(X, P, True) & are_siblings(P, T, True)

print("is_uncle('tio T', 'persona X', R)")
print(is_uncle("tio T", "persona X", R))

print("is_uncle('tio_abuelo TA', 'padre P', R)")
print(is_uncle("tio_abuelo TA", "padre P", R))

# is_cousin(X, Y, False) <= ~is_cousin(X, Y, True)
#
# ís_cousin(X, PR, True) <= is_son(X, _, True)
#
# print(is_son(X, Y, True))

# & is_son(P, A, True) & is_son(T, A, True) & is_son(PR, T, True)

# print(is_cousin("persona X", "primo PR", R))


# -----------------------------------------------------------------------------

# if __name__ == '__main__':
#     print("Fin")
#     database = get_database()
#     print(pyDatalog.ask("factorial_of(4, R)"))
#     print(pyDatalog.ask("factorial[4] == R"))
#     print(pyDatalog.ask("managers_of('Mary', R)"))

# -----------------------------------------------------------------------------
