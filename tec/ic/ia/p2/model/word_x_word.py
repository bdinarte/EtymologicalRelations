# -----------------------------------------------------------------------------

from pyDatalog import pyDatalog

# -----------------------------------------------------------------------------

# X proviene de Y.
child(X, Y) <= etymology(LX, X, LY, Y)
child(X, Y) <= etymological_origin_of(LY, Y, LX, X)
child(X, Y) <= has_derived_form(LY, Y, LX, X)
child(X, Y) <= is_derived_from(LX, X, LY, Y)

# -----------------------------------------------------------------------------

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
ancestor(X, Y) <= parent(X, A) & ancestor(A, Y)

# -----------------------------------------------------------------------------

# X es hermano del término Y. Es bidireccional.
siblings(X, Y) <= siblings(Y, X)
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
    parent(X, H) & ancestor_level(H, Y, L2) & (L == L2 + 1)
)

# -----------------------------------------------------------------------------

# X es primo del término Y. Es bidireccional.
# Son primos si tienen un ancestro con la misma lejanía
cousins(X, Y) <= cousins(Y, X)
cousins(X, Y) <= (
    ~siblings(X, Y) & ~(X == Y) &
    ancestor_level(A, X, L) & ancestor_level(A, Y, L)
)

# -----------------------------------------------------------------------------

# Si X es primo de Y entonces True.
# Forma para obtener una relación con false en vez de una lista vacía.
are_cousins(X, Y, True) <= cousins(X, Y)
are_cousins(X, Y, False) <= ~cousins(X, Y)

# -----------------------------------------------------------------------------

# Determina el grado de primos basado en la cantidad de ancestros
# que existen antes de llegar a un ancestro A que tengan en común X y Y
cousins_level(X, Y, 0) <= ~cousins(X, Y)
cousins_level(X, Y, L) <= (cousins_level[X, Y] == L)

(cousins_level[X, Y] == min_(L, order_by=L)) <= (
    cousins(X, Y) &
    ancestor_level(A, X, L2) &
    ancestor_level(A, Y, L2) &
    ~(X == Y) & (L == L2 - 1)
)

# -----------------------------------------------------------------------------

# T es el tío de X
# Todos los ancestros del primo de X, a excepción de los ancestros de X,
# son tíos de X. Esto incluye tío, tío abuelo, tío segundo, tíos abuelo...
uncle(T, X) <= parent(P, X) & siblings(P, T)
uncle(T, X) <= cousins(X, Y) & ancestor(T, Y) & ~ancestor(T, X)

# -----------------------------------------------------------------------------

# Si T es tío de X entonces True.
# Forma para obtener una relación con false en vez de una lista vacía.
uncle(T, X, True) <= uncle(T, X)
uncle(T, X, False) <= ~uncle(T, X)

# -----------------------------------------------------------------------------
