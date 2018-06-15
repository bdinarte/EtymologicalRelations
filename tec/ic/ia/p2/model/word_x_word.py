# -----------------------------------------------------------------------------

from pyDatalog import pyDatalog

# -----------------------------------------------------------------------------

pyDatalog.create_terms("X, LX, Y, LY, R, H, P, A, T, PR, B")
pyDatalog.create_terms("TA, TS, PS, TTA, TB, TAS, TT, L, L1, L2")

pyDatalog.create_terms("has_derived_form")
pyDatalog.create_terms("etymology, etymological_origin_of")
pyDatalog.create_terms("child, is_child, parent, ancestor")
pyDatalog.create_terms("siblings, are_siblings, ancestor_level")
pyDatalog.create_terms("cousins, are_cousins, cousins_level")
pyDatalog.create_terms("uncle, is_uncle")

# -----------------------------------------------------------------------------

# X proviene de Y.
child(X, Y) <= child(X, Y) & ~(X == Y)
child(X, Y) <= etymology(LY, Y, LX, X)
child(X, Y) <= etymological_origin_of(LX, X, LY, Y)
child(X, Y) <= has_derived_form(LY, Y, LX, X)

# Si X proviene de Y entonces True.
# Forma para obtener una relación con false en vez de una lista vacía.
is_child(X, Y, True) <= child(X, Y)
is_child(X, Y, False) <= ~child(X, Y)

# -----------------------------------------------------------------------------

# X es padre de Y.
parent(X, Y) <= child(Y, X)

# -----------------------------------------------------------------------------

# X es ancestro de Y.
ancestor(X, Y) <= parent(X, Y)
ancestor(X, Y) <= parent(X, A) & ancestor(A, Y) & ~(X == Y)

# -----------------------------------------------------------------------------

# X es hermano del término Y. Es bidireccional.
siblings(X, Y) <= siblings(Y, X) & ~(X == Y)
siblings(X, Y) <= child(X, P) & child(Y, P) & ~(X == Y)

# -----------------------------------------------------------------------------

# Si X es hermano de Y entonces True.
# Forma para obtener una relación con false en vez de una lista vacía.
are_siblings(X, Y, True) <= siblings(X, Y)
are_siblings(X, Y, False) <= ~siblings(X, Y)

# -----------------------------------------------------------------------------

# X es ancestro de Y.
# L es la cantidad de ancestros que existen antes de llegar al ancestro X.
# Sirve para determinar los primos a partir del segundo.
# Sirve para determinar las clases de cada uno de los tíos.
ancestor_level(X, Y, 1) <= parent(X, Y)
ancestor_level(X, Y, L) <= (
    parent(X, H) & ancestor_level(H, Y, L2) & (L == L2 + 1) & ~(X == Y)
)

# -----------------------------------------------------------------------------

# X es primo del término Y. Es bidireccional.
# Son primos si tienen un ancestro con la misma lejanía
cousins(X, Y) <= cousins(Y, X)
cousins(X, Y) <= (
    ancestor_level(A, X, L) &
    ancestor_level(A, Y, L) &
    ~siblings(X, Y) & ~(X == Y)
)

# -----------------------------------------------------------------------------

# Si X es primo de Y entonces True.
# Forma para obtener una relación con false en vez de una lista vacía.
are_cousins(X, Y, True) <= cousins(X, Y)
are_cousins(X, Y, False) <= ~cousins(X, Y)

# -----------------------------------------------------------------------------

# Determina el grado de primos basado en la cantidad de ancestros
# que existen antes de llegar a un ancestro A que tengan en común X y Y

(cousins_level[X, Y] == min_(L2, order_by=L2)) <= (
    cousins(X, Y) &
    ancestor_level(A, X, L) &
    ancestor_level(A, Y, L) &
    ~(X == Y) & (L2 == L - 1)
)

cousins_level(X, Y, 0) <= ~cousins(X, Y)
cousins_level(X, Y, L) <= (cousins_level[X, Y] == L)

# -----------------------------------------------------------------------------

# T es el tío de X
# Todos los ancestros del primo de X, a excepción de los ancestros de X,
# son tíos de X. Esto incluye tío, tío abuelo, tío segundo, tíos abuelo...
uncle(T, X) <= parent(P, X) & siblings(P, T)
uncle(T, X) <= cousins(X, Y) & ancestor(T, Y) & ~ancestor(T, X)

# -----------------------------------------------------------------------------

# Si T es tío de X entonces True.
# Forma para obtener una relación con false en vez de una lista vacía.
is_uncle(T, X, True) <= uncle(T, X)
is_uncle(T, X, False) <= ~uncle(T, X)

# -----------------------------------------------------------------------------
