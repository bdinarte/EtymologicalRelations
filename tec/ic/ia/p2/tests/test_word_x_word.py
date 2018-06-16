# -----------------------------------------------------------------------------

from ..model.word_x_word import *

# -----------------------------------------------------------------------------
#
#                   <tatarabuelo>
#                   ____\_____________
#                  |                  \
#            <tio_bisabuelo>       <bisabuelo>
#                 |                 ____\_____________
#                |                 |                  \
#         <tio_abuelo_seg>    <tio_abuelo>       <abuelo>
#              |                 |             ________\______
#             |                 |             |               \
#         <tio_ter>        <tio_seg>       <tio>          <padre>
#           |                 |              |            _____\_______
#           \                 \              \            \            \
#        <primo_ter>      <primo_seg>      <primo>     <hermano>     <ego>

# -----------------------------------------------------------------------------
# ------- Definición del KB con el que se generan las pruebas unitarias -------
# -----------------------------------------------------------------------------

def setup_module(module):

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

    + etymological_origin_of("ind", "tio_bisabuelo", "ape", "tio_abuelo_seg")
    + etymological_origin_of("spa", "padre", "spa", "ego")
    + etymological_origin_of("spa", "bisabuelo", "por", "tio_abuelo")
    + etymological_origin_of("nor", "tio", "ita", "primo")

    + etymology_active(True)
    + has_derived_form_active(True)
    + etymological_origin_of_active(True)

# -----------------------------------------------------------------------------

def test_siblings():
    """
    Verfica todos los pares de hermanos que existen en la KB de pruebas
    """

    answer = siblings(X, Y).data

    expected = [
        ("ego", "hermano"),
        ("tio_abuelo", "abuelo"),
        ("hermano", "ego"),
        ("bisabuelo", "tio_bisabuelo"),
        ("tio", "padre"),
        ("abuelo", "tio_abuelo"),
        ("tio_bisabuelo", "bisabuelo"),
        ("padre", "tio")
    ]

    assert set(expected) == set(answer)

# -----------------------------------------------------------------------------

def test_are_siblings_positive_case():
    """
    Verifica que tenga correspondencia con la función test_siblings
    """
    answer = are_siblings("hermano", "ego", R).data
    answer = answer + are_siblings("tio", "padre", R).data
    assert set(answer) == set([(True,)])

def test_are_siblings_negative_case():
    """
    Verifica que se retorne una False en vez de una lista vacía
    en caso de que los términos no sean hermanos
    """
    answer = are_siblings("primo", "ego", R).data
    answer = answer + are_siblings("", "padre", R).data
    assert set(answer) == set([(False,)])

def test_are_siblings_same_terms():
    """
    Verifica que se retorne una False en vez de una lista vacía
    en caso de que los términos no sean hermanos
    """
    answer = are_siblings("ego", "ego", R).data
    answer = answer + are_siblings("padre", "padre", R).data
    assert set(answer) == set([(False,)])

# -----------------------------------------------------------------------------

def test_cousins_of_ego():
    """
    Verifica todos los primos de ego, incluyendo primo segundo y tercero
    """
    answer = cousins("ego", Y).data
    expected = [("primo_ter",), ("primo",), ("primo_seg",)]
    assert set(answer) == set(expected)

def test_cousins_of_parent():
    """
    Verifica todos los primos del padre de ego para probar que no solo sirve
    en los términos "hojas"
    """
    answer = cousins("padre", Y).data
    expected = [("tio_seg",), ("tio_ter",)]
    assert set(answer) == set(expected)

def test_cousins_of_sibling():
    """
    Verifica todos los primos del término hermano de ego sean los mismo
    """
    ego = cousins("ego", Y).data
    sibling = cousins("hermano", Y).data

    assert set(ego) == set(sibling)

# -----------------------------------------------------------------------------

def test_are_cousins_positive_case():
    """
    Verifica el que dos términos son primos si tiene un ancestro en común
    con la misma lejanía, pero no es el término hermano.
    """
    answer = are_cousins("ego", "primo", R).data
    answer = answer + are_cousins("ego", "hermano", R).data
    assert set(answer) == set([(True,), (False,)])


def test_are_cousins_negative_case():
    """
    Verifica que siempre se obtenga false y no una lista vacía en caso
    de que los términos no sea primos
    """
    answer = are_cousins("ego", "hermano", R).data
    assert set(answer) == set([(False,)])

def test_are_cousins_same_term():
    """
    Verifica que un término no sea primo de si mismo
    """
    answer = are_cousins("ego", "ego", R).data
    expected = [(False,)]
    assert set(answer) == set(expected)


# -----------------------------------------------------------------------------

def test_child_has_one_parent():
    """
    Verifica que ego tenga solo un padre
    """
    answer = child("ego", P).data
    expected = [("padre",)]
    assert set(answer) == set(expected)

def test_child_get_all_of():
    """
    Verifica que el abuelo de ego tiene solo los dos hijos
    """
    answer = child(P, "bisabuelo").data
    expected = [("abuelo",), ("tio_abuelo",)]
    assert set(answer) == set(expected)

def test_child_get_all_of_empty():
    """
    Verifica que ego no tienen hijos
    """
    answer = child(P, "ego").data
    assert set(answer) == set([])

def test_child_has_no_parent():
    """
    El término tatarabuelo no tiene ningún padre
    """
    answer = child("tatarabuelo", P).data
    assert set(answer) == set([])

def test_child_someone_not_exists():
    """
    Verifica que se retorne una lista vacía si alguno de los
    involucrados en la pregunta es no existe en la KB.
    """
    answer = child("", P).data
    answer = answer + child(P, "").data
    assert set(answer) == set([])

# -----------------------------------------------------------------------------

def test_is_child_positive_case():
    """
    Verifica que ego es derivado del término padre
    """
    answer = is_child("ego", "padre", R).data
    answer = answer + is_child("hermano", "padre", R).data
    assert set(answer) == set([(True,), (True,)])

def test_is_child_negative_case():
    """
    Verifica que el término padre de ego no es padre de tambíén
    del término abuelo.
    """
    answer = is_child("abuelo", "padre", R).data
    answer = answer + is_child("hermano", "ego", R).data
    assert set(answer) == set([(False,), (False,)])

def test_is_child_someone_not_exists():
    """
    Verfica que la lista sea vacía en caso que alguno de los términos no
    existe.
    """
    answer = is_child("", "padre", R).data
    answer = answer + is_child("hermano", "", R).data
    assert set(answer) == set([(False,)])

# -----------------------------------------------------------------------------

def test_uncle_get_all():
    """
    Se obtienen todos los términos tíos; siendo un tío cualquier ancestro
    de un primo que no sea ancestro del término buscado.
    """
    answer = uncle(T, "ego").data

    expected = [
        ("tio",),
        ("tio_seg",),
        ("tio_abuelo",),
        ("tio_abuelo_seg",),
        ("tio_bisabuelo",),
        ("tio_ter",)
    ]

    assert set(expected) == set(answer)

def test_uncle_get_all_nephews():
    """
    Se obtienen todos los términos que son sobrinos de otro.
    """
    answer = uncle("tio", X).data
    expected = [('primo_seg',), ('primo_ter',), ('hermano',), ('ego',)]
    assert set(expected) == set(answer)

# -----------------------------------------------------------------------------

def test_is_uncle_positive_case():
    """
    Verifica términos que son tíos de otros
    """
    answer = is_uncle("padre", "primo", R).data
    answer = answer + is_uncle("tio_abuelo", "hermano", R).data
    answer = answer + is_uncle("tio_bisabuelo", "ego", R).data
    assert set(answer) == set([(True,), (True,), (True,)])

def test_is_uncle_negative_case():
    """
    Verifica términos que son tíos de otros
    """
    answer = is_uncle("padre", "hermano", R).data
    answer = answer + is_uncle("ego", "padre", R).data
    answer = answer + is_uncle("ego", "abuelo", R).data
    assert set(answer) == set([(False,), (False,), (False,)])

# -----------------------------------------------------------------------------

def test_cousins_distance_ego_and_sibling_case():
    """
    Verifica todos los primos de un determinado término junto con su lejanía.
    El término hermano obtiene los mismo resultados al tener los mismos primos
    """
    answer = cousins_distance("ego", Y, L).data
    answer = answer + cousins_distance("hermano", Y, L).data
    expected = [("primo", 1), ("primo_seg", 2), ("primo_ter", 3),]
    assert set(answer) == set(expected)

def test_cousins_distance_parent_and_uncle_case():
    """
    Verifica todos los primos de un determinado término junto con su lejanía.
    El término tío obtiene los mismo resultados al tener los mismos primos
    """
    answer = cousins_distance(X, "padre", L).data
    answer = answer + cousins_distance(X, "tio", L).data
    expected = [('tio_seg', 1), ('tio_ter', 2)]
    assert set(answer) == set(expected)

def test_cousins_distance_using_specific_distance():
    """
    Verifica todos los primos de un determinado término junto con su lejanía.
    """
    answer = cousins_distance(X, "ego", 2).data
    assert set(answer) == set([("primo_seg",)])

def test_cousins_distance_not_cousins():
    """
    Verifica que si dos términos no son primns, se obtiene una distancia de 0
    """
    answer = cousins_distance("no primo", "ego", R).data
    assert set(answer) == set([(0,)])

# -----------------------------------------------------------------------------