# -----------------------------------------------------------------------------

from model.word_x_word import *

# -----------------------------------------------------------------------------

+ etymology("-", "padre P", "-", "persona X") ## Este wey
+ is_derived_from("-", "persona X", "-", "padre P")
+ etymological_origin_of("-", "persona X", "-", "padre P") ## ESte wey
+ has_derived_form("-", "tatarabuelo TTA", "-", "bisabuelo B")
+ has_derived_form("-", "tatarabuelo TTA", "-", "tio_bisabuelo TB")
+ has_derived_form("-", "tio_bisabuelo TB", "-", "tio_abuelo_seg TAS")
+ has_derived_form("-", "tio_abuelo_seg TAS", "-", "tio_ter TT")
+ has_derived_form("-", "tio_ter TT", "-", "primo_ter PT")
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
# Pruebas para is_child
# -----------------------------------------------------------------------------

print("child(X, P)")
print(child(X, P))

# -----------------------------------------------------------------------------
# Pruebas para ancestor e parent
# -----------------------------------------------------------------------------

print("parent(P, X)")
print(parent(P, X))

# -----------------------------------------------------------------------------
# Pruebas para siblings
# -----------------------------------------------------------------------------

print("siblings(X, Y)")
print(siblings(X, Y))

# -----------------------------------------------------------------------------
# Pruebas para ancestor_level
# -----------------------------------------------------------------------------

print("ancestor_level(A, 'persona X', L)")
print(ancestor_level(A, "persona X", L))

# -----------------------------------------------------------------------------
# Pruebas para cousins
# -----------------------------------------------------------------------------

print("are_cousins(X, Y)")
print(cousins("persona X", X))

# -----------------------------------------------------------------------------
# Pruebas para cousin_grade
# -----------------------------------------------------------------------------

print("cousins_level('persona X', Y, L)")
print(cousins_level("persona X", Y, L))


# -----------------------------------------------------------------------------
# Pruebas para uncle
# -----------------------------------------------------------------------------

print("uncle(T, 'persona X', R)")
print(uncle(T, "persona X"))

# -----------------------------------------------------------------------------