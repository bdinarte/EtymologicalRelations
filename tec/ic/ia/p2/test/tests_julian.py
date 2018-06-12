# -----------------------------------------------------------------------------

import pandas as pd
from pyDatalog import pyDatalog


# -----------------------------------------------------------------------------
#
#             Árbol de pruebas utilizado para la relaciones de
#        is_son, are_siblings, is_uncle, are_cousins, cousin_grade
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

# Términos que se usan en este archivo

pyDatalog.create_terms("X, LX, Y, LY, R, H, P, A, T, PR,"
                       "B, TA, TS, PS, TTA, TB, TAS, TT, L, L1, L2")

pyDatalog.create_terms("has_derived_form, is_derived_from,"
                       "etymology, etymological_origin_of")

pyDatalog.create_terms("is_son, is_parent, is_ancestor, ancestor_level, grade, "
                       "are_siblings, is_uncle, are_cousins, cousins_level")

# -----------------------------------------------------------------------------

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
# Pruebas para is_son
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

# X = Primera palabra
# Y = Segunda palabra
# True es que X si es hija de Y
is_son(X, Y, True) <= is_son(X, Y)
is_son(X, Y, False) <= ~is_son(X, Y)

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

# Persona Y no está definida
print("is_son('persona X', 'persona Y', R)")
print(is_son("persona X", "persona Y", R))

# Despliega que el padre de persona X es padre P
print("is_son('persona X', P)")
print(is_son("persona X", P))

# Los hijos del abuelo de uno son el tío T y el padre P
print("is_son(X, 'abuelo A')")
print(is_son(X, "abuelo A"))

# Se obtiene una lista vacia
print("is_son(None, None)")
print(is_son(None, None))

# Se obtiene el valor de R que debe ser False
print("is_son(None, None, R)")
print(is_son(None, None, R))

print("is_son(None, 'persona X', R)")
print(is_son(None, "persona X", R))

# -----------------------------------------------------------------------------
# Pruebas para is_ancestor e is_parent
# -----------------------------------------------------------------------------

is_parent(X, Y) <= is_son(Y, X)

# Despliega que el padre de persona X es padre P
print("is_parent(P, 'persona X')")
print(is_parent(P, "persona X"))

is_ancestor(A, B) <= is_parent(A, B)
is_ancestor(X, Y) <= is_parent(X, A) & is_ancestor(A, Y)

# Se obtiene del desde el padre hasta el tatarabuelo
print("is_ancestor(A, 'persona X')")
print(is_ancestor(A, "persona X"))

# Se obtiene el ego, el padre, el tio, primos y hermanos
print("is_ancestor('abuelo A', X)")
print(is_ancestor("abuelo A", X))

# -----------------------------------------------------------------------------
# Pruebas para are_siblings
# -----------------------------------------------------------------------------

# "persoonlik" y "tydelik" son hijos de "-lik".
+ etymological_origin_of("afr", "-lik", "afr", "persoonlik")
+ etymological_origin_of("afr", "-lik", "afr", "tydelik")

# 2 Palabras que son hijas de "aand"
+ has_derived_form("afr", "aand", "afr", "aandete")
+ has_derived_form("afr", "aand", "afr", "aandjie")
+ is_derived_from("afr", "aandjete", "afr", "aand")

are_siblings(X, Y, True) <= are_siblings(X, Y)
are_siblings(X, Y, False) <= ~are_siblings(X, Y)

are_siblings(X, Y) <= are_siblings(Y, X)
are_siblings(X, Y) <= is_son(X, P) & is_son(Y, P) & ~(X == Y)

print("are_siblings('persoonlik', 'tydelik', R)")
print(are_siblings("persoonlik", "tydelik", R))

print("are_siblings('aandete', 'aandjie', R)")
print(are_siblings("aandete", "aandjie", R))

print("are_siblings(None, 'aandjie', R)")
print(are_siblings(None, "aandjie", R))

# Relación que no existe
print("are_siblings('padre P', 'persona X', R)")
print(are_siblings("padre P", "persona X", R))

# Tienen que haber 2 hermanos para aandjie
print("are_siblings(X, 'aandjie')")
print(are_siblings('aandjie', Y))

# Lista vacía
print("are_siblings(None, X)")
print(are_siblings(None, X))

# -----------------------------------------------------------------------------
# Pruebas para ancestor_level
# -----------------------------------------------------------------------------

# ancestor_level(X, Y, 0) <= ~ancestor_level(X, Y, L)

ancestor_level(X, Y, 1) <= is_parent(X, Y)

ancestor_level(X, Y, L) <= (
    is_parent(X, H) & ancestor_level(H, Y, L2) & (L == L2 + 1)
)

# Nivel 1
print("ancestor_level('padre P', 'persona X', L)")
print(ancestor_level("padre P", "persona X", L))

# Nivel 2
print("ancestor_level('abuelo A', 'persona X', L)")
print(ancestor_level("abuelo A", "persona X", L))

# Nivel 4
print("ancestor_level('tatarabuelo TTA', 'persona X', L)")
print(ancestor_level("tatarabuelo TTA", "persona X", L))

print("ancestor_level(A, 'persona X', L)")
print(ancestor_level(A, "persona X", L))

print("ancestor_level(A, 'primo PR', L)")
print(ancestor_level(A, "primo PR", L))

print("ancestor_level(None, None, L)")
print(ancestor_level(None, None, L))

# -----------------------------------------------------------------------------
# Pruebas para are_cousins
# -----------------------------------------------------------------------------

are_cousins(X, Y, True) <= are_cousins(X, Y)
are_cousins(X, Y, False) <= ~are_cousins(X, Y)

are_cousins(X, Y) <= are_cousins(Y, X)

are_cousins(X, Y) <= (
    ancestor_level(A, X, L) &
    ancestor_level(A, Y, L) &
    ~are_siblings(X, Y) & ~(X == Y)
)

print("are_cousins('primo PR', 'hermano H', R)")
print(are_cousins("primo PR", "hermano H", R))

print("are_cousins('primo_ter PT', 'persona X', R)")
print(are_cousins("primo_ter PT", "persona X", R))

print("are_cousins('hermano H', 'persona X', R)")
print(are_cousins("hermano H", "persona X", R))

print("are_cousins(X, 'primo PR')")
print(are_cousins(X, "primo PR"))

print("are_cousins('persona X', X)")
print(are_cousins("persona X", X))

print("are_cousins(None, X)")
print(are_cousins(None, X))

# -----------------------------------------------------------------------------
# Pruebas para cousin_grade
# -----------------------------------------------------------------------------

(cousins_level[X, Y] == min_(L2, order_by=L2)) <= (
    are_cousins(X, Y) &
    ancestor_level(A, X, L) &
    ancestor_level(A, Y, L) &
    ~(X == Y) & (L2 == L - 1)
)

cousins_level(X, Y, 0) <= ~are_cousins(X, Y)
cousins_level(X, Y, L) <= (cousins_level[X, Y] == L)

print("cousins_level('persona X', Y, L)")
print(cousins_level("persona X", Y, L))

print("cousins_level('primo PR', Y, L)")
print(cousins_level("primo PR", Y, L))

print("cousins_level('persona X', 'primo_seg PS', L)")
print(cousins_level("persona X", "primo_seg PS", L))

# -----------------------------------------------------------------------------
# Pruebas para is_uncle
# -----------------------------------------------------------------------------

is_uncle(T, X, True) <= is_uncle(T, X)
is_uncle(T, X, False) <= ~is_uncle(T, X)
is_uncle(T, X) <= is_parent(P, X) & are_siblings(P, T)
is_uncle(T, X) <= are_cousins(X, Y) & is_ancestor(T, Y) & ~is_ancestor(T, X)

print("is_uncle('tio T', 'persona X', R)")
print(is_uncle("tio T", "persona X", R))

print("is_uncle('tio_abuelo TA', 'padre P', R)")
print(is_uncle("tio_abuelo TA", "padre P", R))

# Deben de ser True al considerar tíos abuelos
print("is_uncle('tio_abuelo TA', 'persona X', R)")
print(is_uncle("tio_abuelo TA", "persona X", R))

print("is_uncle('tio_bisabuelo TB', 'persona X', R)")
print(is_uncle("tio_bisabuelo TB", "persona X", R))

# Deberia mostrar toda la ascendencia de tíos no solo el primero
print("is_uncle(T, 'persona X')")
print(is_uncle(T, "persona X"))

# Muestra toda la descendencia del hermano
print("is_uncle('tio_bisabuelo TB', X)")
print(is_uncle("tio_bisabuelo TB", X))

print("is_uncle(None, None, R)")
print(is_uncle(None, None, R))

print("is_uncle(None, 'persona X', R)")
print(is_uncle(None, "persona X", R))

# -----------------------------------------------------------------------------