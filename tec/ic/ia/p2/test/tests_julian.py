# -----------------------------------------------------------------------------

import pandas as pd
from model.word_x_word import *

# import logging
# from pyDatalog import pyEngine
# pyEngine.Logging = True
# logging.basicConfig(level=logging.DEBUG)

# Hechos provenientes del árbol

+ has_derived_form(None, "tatarabuelo TTA", None, "bisabuelo B")
+ has_derived_form(None, "tatarabuelo TTA", None, "tio_bisabuelo TB")
+ has_derived_form(None, "tio_bisabuelo TB", None, "tio_abuelo_seg TAS")
+ has_derived_form(None, "tio_abuelo_seg TAS", None, "tio_tercero TT")
+ has_derived_form(None, "tio_tercero TT", None, "primo_ter PT")
+ has_derived_form(None, "bisabuelo B", None, "abuelo A")
+ has_derived_form(None, "bisabuelo B", None, "tio_abuelo TA")
+ has_derived_form(None, "abuelo A", None, "padre P")
+ has_derived_form(None, "abuelo A", None, "tio T")
+ has_derived_form(None, "padre P", None, "persona X")
+ has_derived_form(None, "padre P", None, "hermano H")
+ has_derived_form(None, "tio T", None, "primo PR")
+ has_derived_form(None, "tio_abuelo TA", None, "tio_seg TS")
+ has_derived_form(None, "tio_seg TS", None, "primo_seg PS")

# -----------------------------------------------------------------------------
# Pruebas para is_child
# -----------------------------------------------------------------------------

# "beeste" es hijo de "bees"
+ has_derived_form("afr", "bees", "afr", "beeste")

# Todas las reglas has_derived_form tienen como contrario
# is_derived_from
+ is_derived_from("afr", "beeste", "afr", "bees")

# "aktinium" es hijo de "actininum"
+ etymology("afr", "aktinium", "nld", "actinium")

# "verbuiging" es hijo de "-ing"
+ etymological_origin_of("afr", "-ing", "afr", "verbuiging")
#
# print("is_child('beeste', 'bees', R)")
# print(is_child("beeste", "bees", R))
#
# print("is_child('aktinium', 'actinium', R)")
# print(is_child("aktinium", "actinium", R))
#
# print("is_child('verbuiging', '-ing', R) == [(True, )]")
# print(is_child("verbuiging", "-ing", R) == [(True, )])
#
# # Persona Y no está definida
# print("is_child('persona X', 'persona Y', R)")
# print(is_child("persona X", "persona Y", R))
#
# # Despliega que el padre de persona X es padre P
# print("is_child('persona X', P)")
# print(child("persona X", P))
#
# # Los hijos del abuelo de uno son el tío T y el padre P
# print("is_child(X, 'abuelo A')")
# print(child(X, "abuelo A"))
#
# # Se obtiene una lista vacia
# print("is_child(None, None)")
# print(child(None, None))
#
# # Se obtiene el valor de R que debe ser False
# print("is_child(None, None, R)")
# print(is_child(None, None, R))
#
# print("is_child(None, 'persona X', R)")
# print(is_child(None, "persona X", R))

# -----------------------------------------------------------------------------
# Pruebas para ancestor e parent
# -----------------------------------------------------------------------------

# parent(X, Y) <= child(Y, X)
#
# # Despliega que el padre de persona X es padre P
# print("parent(P, 'persona X')")
# print(parent(P, "persona X"))
#
# # Se obtiene del desde el padre hasta el tatarabuelo
# print("ancestor(A, 'persona X')")
# print(ancestor(A, "persona X"))
#
# # Se obtiene el ego, el padre, el tio, primos y hermanos
# print("ancestor('abuelo A', X)")
# print(ancestor("abuelo A", X))

# -----------------------------------------------------------------------------
# Pruebas para siblings
# -----------------------------------------------------------------------------

# # "persoonlik" y "tydelik" son hijos de "-lik".
# + etymological_origin_of("afr", "-lik", "afr", "persoonlik")
# + etymological_origin_of("afr", "-lik", "afr", "tydelik")
#
# # 2 Palabras que son hijas de "aand"
# + has_derived_form("afr", "aand", "afr", "aandete")
# + has_derived_form("afr", "aand", "afr", "aandjie")
# + is_derived_from("afr", "aandjete", "afr", "aand")
#
# print("siblings('persoonlik', 'tydelik', R)")
# print(are_siblings("persoonlik", "tydelik", R))
#
# print("siblings('aandete', 'aandjie', R)")
# print(are_siblings("aandete", "aandjie", R))
#
# print("siblings(None, 'aandjie', R)")
# print(are_siblings(None, "aandjie", R))
#
# # Relación que no existe
# print("siblings('padre P', 'persona X', R)")
# print(are_siblings("padre P", "persona X", R))
#
# # Tienen que haber 2 hermanos para aandjie
# print("siblings(X, 'aandjie')")
# print(siblings('aandjie', Y))
#
# # Lista vacía
# print("siblings(None, X)")
# print(siblings(None, X))

# -----------------------------------------------------------------------------
# Pruebas para ancestor_level
# -----------------------------------------------------------------------------

# # Nivel 1
# print("ancestor_level('padre P', 'persona X', L)")
# print(ancestor_level("padre P", "persona X", L))
#
# # Nivel 2
# print("ancestor_level('abuelo A', 'persona X', L)")
# print(ancestor_level("abuelo A", "persona X", L))
#
# # Nivel 4
# print("ancestor_level('tatarabuelo TTA', 'persona X', L)")
# print(ancestor_level("tatarabuelo TTA", "persona X", L))
#
# print("ancestor_level(A, 'persona X', L)")
# print(ancestor_level(A, "persona X", L))
#
# print("ancestor_level(A, 'primo PR', L)")
# print(ancestor_level(A, "primo PR", L))
#
# print("ancestor_level(None, None, L)")
# print(ancestor_level(None, None, L))

# -----------------------------------------------------------------------------
# Pruebas para cousins
# -----------------------------------------------------------------------------

# print("cousins('primo PR', 'hermano H', R)")
# print(are_cousins("primo PR", "hermano H", R))
#
# print("cousins('primo_ter PT', 'persona X', R)")
# print(are_cousins("primo_ter PT", "persona X", R))
#
# print("cousins('hermano H', 'persona X', R)")
# print(are_cousins("hermano H", "persona X", R))
#
# print("cousins(X, 'primo PR')")
# print(cousins(X, "primo PR"))
#
# print("cousins('persona X', X)")
# print(cousins("persona X", X))
#
# print("cousins(None, X)")
# print(cousins(None, X))

# -----------------------------------------------------------------------------
# Pruebas para cousin_grade
# -----------------------------------------------------------------------------

# print("cousins_level('persona X', Y, L)")
# print(cousins_level("persona X", Y, L))
#
# print("cousins_level('primo PR', Y, L)")
# print(cousins_level("primo PR", Y, L))
#
# print("cousins_level('persona X', 'primo_seg PS', L)")
# print(cousins_level("persona X", "primo_seg PS", L))
#
# print("cousins_level('persona X', 'abuelo A', L)")
# print(cousins_level("persona X", "abuelo A", L))
#
# print("cousins_level(None, 'abuelo A', L)")
# print(cousins_level(None, "abuelo A", L))
#
# print("cousins_level(None, None, L)")
# print(cousins_level(None, None, L))

# -----------------------------------------------------------------------------
# Pruebas para uncle
# -----------------------------------------------------------------------------

# print("uncle('tio T', 'persona X', R)")
# print(is_uncle("tio T", "persona X", R))
#
# print("uncle('tio_abuelo TA', 'padre P', R)")
# print(is_uncle("tio_abuelo TA", "padre P", R))
#
# # Deben de ser True al considerar tíos abuelos
# print("uncle('tio_abuelo TA', 'persona X', R)")
# print(is_uncle("tio_abuelo TA", "persona X", R))
#
# print("uncle('tio_bisabuelo TB', 'persona X', R)")
# print(is_uncle("tio_bisabuelo TB", "persona X", R))
#
# # Deberia mostrar toda la ascendencia de tíos no solo el primero
# print("uncle(T, 'persona X')")
# print(uncle(T, "persona X"))
#
# # Muestra toda la descendencia del hermano
# print("uncle('tio_bisabuelo TB', X)")
# print(uncle("tio_bisabuelo TB", X))
#
# print("uncle(None, None, R)")
# print(is_uncle(None, None, R))
#
# print("uncle(None, 'persona X', R)")
# print(is_uncle(None, "persona X", R))

# -----------------------------------------------------------------------------