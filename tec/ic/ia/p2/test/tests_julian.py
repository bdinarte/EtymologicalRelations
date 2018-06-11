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

# if __name__ == '__main__':
#     print("Fin")
#     database = get_database()
#     print(pyDatalog.ask("factorial_of(4, R)"))
#     print(pyDatalog.ask("factorial[4] == R"))
#     print(pyDatalog.ask("managers_of('Mary', R)"))

# -----------------------------------------------------------------------------
