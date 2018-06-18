# -----------------------------------------------------------------------------


import logging
from pyDatalog import pyDatalog, pyEngine

# pyEngine.Logging = True
# logging.basicConfig(level=logging.DEBUG, format="%(message)s")

# -----------------------------------------------------------------------------

pyDatalog.create_terms("X, LX, Y, LY, R, H, P, A, T, PR, B, D, D1, D2")
pyDatalog.create_terms("TA, TS, PS, TTA, TB, TAS, TT, L, L1, L2, LA, LP, LT")

pyDatalog.create_terms("has_derived_form, etymologically_related")
pyDatalog.create_terms("etymology, etymological_origin_of")
pyDatalog.create_terms("child, is_child, parent, ancestor")
pyDatalog.create_terms("siblings, are_siblings, ancestor_distance")
pyDatalog.create_terms("cousins, are_cousins, cousins_distance")
pyDatalog.create_terms("uncle, is_uncle, has_derived_form_active")
pyDatalog.create_terms("etymology_active, etymological_origin_of_active")
pyDatalog.create_terms("etymologically_related_active")

+ etymology("por", "ego", "chi", "padre")
+ etymology("por", "tio_ter", "chi", "tio_abuelo_seg")
+ etymology("por", "padre", "chi", "abuelo")
+ etymology("spa", "tio_seg", "chi", "tio_abuelo")

+ has_derived_form("ind", "tatarabuelo", "por", "bisabuelo")
+ has_derived_form("ind", "tatarabuelo", "ind", "tio_bisabuelo")
+ has_derived_form("por", "tio_ter", "lat", "primo_ter")
+ has_derived_form("por", "bisabuelo", "ape", "abuelo")
+ has_derived_form("chi", "abuelo", "nor", "tio")
+ has_derived_form("lat", "padre", "ape", "hermano")
+ has_derived_form("lat", "tio_seg", "ita", "primo_seg")
# + etymological_origin_of("por", "abuelo", "padre", "prueba")
+ etymological_origin_of("por", "padre", "spa", "prueba")
+ etymological_origin_of("ind", "tio_bisabuelo", "ape", "tio_abuelo_seg")
+ etymological_origin_of("spa", "padre", "spa", "ego")
+ etymological_origin_of("spa", "padre", "esp", "padre") ## aqui
+ etymological_origin_of("spa", "bisabuelo", "por", "tio_abuelo")
+ etymological_origin_of("nor", "tio", "ita", "primo")

+ etymologically_related("spa", "ego", "ape", "hermano")
+ etymologically_related("nor", "tio", "lat", "padre")

+ has_derived_form("eng", "bisabuelo", "esp", "abuelo")
+ has_derived_form("esp", "abuelo", "eng", "padre")
+ has_derived_form("esp", "abuelo", "nor", "tio")

+ has_derived_form("eng", "padre", "esp", "padre") ## bug
+ has_derived_form("esp", "padre", "eng", "padre") ## bug

+ has_derived_form("eng", "padre", "eng", "ego")
+ has_derived_form("eng", "padre", "eng", "hermano")
+ has_derived_form("eng", "padre", "spa", "hermano")
+ has_derived_form("eng", "padre", "eng", "prueba")
+ has_derived_form("eng", "padre", "eng", "padre")

+ etymology_active(True)
+ has_derived_form_active(True)
+ etymological_origin_of_active(True)
+ etymologically_related_active(True)

# -----------------------------------------------------------------------------

# X proviene de Y.

child(X, LX, Y, LY) <= (
        etymology_active(True) &
        etymology(LX, X, LY, Y) & ~(X == Y)
)

child(X, LX, Y, LY) <= (
        etymology_active(True) &
        etymology(LX, X, LY, Y) & ~(LX == LY)
)

child(X, LX, Y, LY) <= (
        etymological_origin_of_active(True) &
        etymological_origin_of(LY, Y, LX, X) & ~(X == Y)
)

child(X, LX, Y, LY) <= (
        etymological_origin_of_active(True) &
        etymological_origin_of(LY, Y, LX, X) & ~(LX == LY)
)

child(X, LX, Y, LY) <= (
        has_derived_form_active(True) &
        has_derived_form(LY, Y, LX, X) & ~(X == Y)
)

child(X, LX, Y, LY) <= (
        has_derived_form_active(True) &
        has_derived_form(LY, Y, LX, X) & ~(LX == LY)
)

# print(child("padre", LX, "ego", LY))

# -----------------------------------------------------------------------------

# Si X proviene de Y entonces True.
# Forma para obtener una relación con false en vez de una lista vacía.
is_child(X, Y, True) <= child(X, LX, Y, LY)
is_child(X, Y, False) <= ~child(X, LX, Y, LY)

# print(is_child(X, Y, R))

# -----------------------------------------------------------------------------

# X es padre de Y.
parent(X, LX, Y, LY) <= child(Y, LY, X, LX)

# print(parent("padre", LX, "ego", LY))

# -----------------------------------------------------------------------------

# X es ancestro de Y.
ancestor(X, LX, Y, LY) <= parent(X, LX, Y, LY)
ancestor(X, LX, Y, LY) <= parent(X, LX, A, LA) & ancestor(A, LA, Y, LY)

# print(ancestor(X, LX, "padre", LY))

# -----------------------------------------------------------------------------

# X es hermano del término Y. Es bidireccional.
siblings(X, LX, Y, LY) <= siblings(Y, LY, X, LX)

# Pueden ser en el mismo lenguaje pero deben ser palabras distintas o
siblings(X, LX, Y, LY) <= (
        child(X, LX, P, LP) &
        child(Y, LY, P, LP) & ~(X == Y)
)

# Pueden ser las mismas palabras pero en lenguaje distinto
siblings(X, LX, Y, LY) <= (
        child(X, LX, P, LP) &
        child(Y, LY, P, LP) & ~(LX == LY)
)

# print(siblings("padre", LX, Y, LY))

# -----------------------------------------------------------------------------

# Si X es hermano de Y entonces True.
# Forma para obtener una relación con false en vez de una lista vacía.
are_siblings(X, Y, True) <= siblings(X, LX, Y, LY)
are_siblings(X, Y, False) <= ~siblings(X, LX, Y, LY)

# print(are_siblings("padre", Y, R))

# -----------------------------------------------------------------------------

# X es ancestro de Y.
# D es la cantidad de ancestros que existen antes de llegar al ancestro X.
# Sirve para determinar los primos a partir del segundo.
# Sirve para determinar las clases de cada uno de los tíos.

# ancestor_distance(X, LX, Y, LY, 0) <=
ancestor_distance(X, LX, Y, LY, 1) <= parent(X, LX, Y, LY)

# BUGFIX: Se evita que el programa se encicle
ancestor_distance(X, LX, Y, LY, D2) <= (
        parent(X, LX, A, LA) &
        ~parent(A, LA, X, LX) &
        ancestor_distance(A, LA, Y, LY, D) &
        (D2 == D + 1)
)

# print(ancestor(X, LX, "padre", LY))
# print(ancestor("padre", LX, Y, LY))
# print(ancestor_distance("padre", LX, Y, LY, R))
# print(ancestor_distance(X, LX, "padre", LY, R))

# -----------------------------------------------------------------------------

# X es primo del término Y. Es bidireccional.
# Son primos si tienen un ancestro con la misma lejanía

cousins(X, LX, Y, LY) <= cousins(Y, LY, X, LX)

cousins(X, LX, Y, LY) <= (
        ancestor_distance(A, LA, X, LX, D) &
        ancestor_distance(A, LA, Y, LY, D) &
        ~(X == Y) & ~siblings(X, LX, Y, LY)
)

cousins(X, LX, Y, LY) <= (
        ancestor_distance(A, LA, X, LX, D) &
        ancestor_distance(A, LA, Y, LY, D) &
        ~(LX == LY) & ~siblings(X, LX, Y, LY)
)

# print(~siblings(X, LX, Y, LY))
# print(cousins("padre", LX, Y, LY))

# -----------------------------------------------------------------------------

# Si X es primo de Y entonces True.
# Forma para obtener una relación con false en vez de una lista vacía.
are_cousins(X, LX, Y, LY, True) <= cousins(X, LX, Y, LY)
are_cousins(X, LX, Y, LY, False) <= ~cousins(X, LX, Y, LY)

# print(are_cousins("padre", LX, Y, LY, R))

# -----------------------------------------------------------------------------

# Determina el grado de primos basado en la cantidad de ancestros
# que existen antes de llegar a un ancestro A que tengan en común X y Y

(cousins_distance[X, LX, Y, LY] == min_(D, order_by=D)) <= (
        ancestor_distance(A, LA, X, LX, D2) &
        ancestor_distance(A, LA, Y, LY, D2) &
        ~(X == Y) & ~siblings(X, LX, Y, LY) & (D == D2 - 1)
)

(cousins_distance[X, LX, Y, LY] == min_(D, order_by=D)) <= (
        ancestor_distance(A, LA, X, LX, D2) &
        ancestor_distance(A, LA, Y, LY, D2) &
        ~(LX == LY) & ~siblings(X, LX, Y, LY) & (D == D2 - 1)
)

cousins_distance(X, LX, Y, LY, 0) <= ~cousins(X, LX, Y, LY)
cousins_distance(X, LX, Y, LY, D) <= (cousins_distance[X, LX, Y, LY] == D)
cousins_distance(X, LX, Y, LY, D) <= cousins_distance(Y, LY, X, LX, D)

print(cousins_distance("ego", LX, "primo", LY, D))
# print(cousins_distance("ego", LX, "primo", LY, D))

# -----------------------------------------------------------------------------

# T es el tío de X
# Todos los ancestros del primo de X, a excepción de los ancestros de X,
# son tíos de X. Esto incluye tío, tío abuelo, tío segundo, tíos abuelo...
uncle(T, LT, X, LX) <= parent(P, LP, X, LX) & siblings(P, LP, T, LT)

uncle(T, LT, X, LX) <= (
        cousins(X, LX, Y, LY) &
        ancestor(T, LT, Y, LY) & ~ancestor(T, LT, X, LX)
)

# print(uncle(T, LT, X, LX))

# -----------------------------------------------------------------------------

# Si T es tío de X entonces True.
# Forma para obtener una relación con false en vez de una lista vacía.
is_uncle(T, X, True) <= uncle(T, LT, X, LX)
is_uncle(T, X, False) <= ~uncle(T, LT, X, LX)

# print(is_uncle(T, X, R))

# -----------------------------------------------------------------------------
