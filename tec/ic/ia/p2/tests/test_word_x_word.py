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

    + etymological_origin_of("por", "padre", "spa", "prueba")
    + etymological_origin_of("ind", "tio_bisabuelo", "ape", "tio_abuelo_seg")
    + etymological_origin_of("spa", "padre", "spa", "ego")
    + etymological_origin_of("spa", "bisabuelo", "por", "tio_abuelo")
    + etymological_origin_of("nor", "tio", "ita", "primo")

    + etymologically_related("spa", "ego", "ape", "hermano")
    + etymologically_related("nor", "tio", "lat", "padre")

    + etymology_active(True)
    + has_derived_form_active(True)
    + etymological_origin_of_active(True)
    + etymologically_related_active(True)

# -----------------------------------------------------------------------------

def test_siblings():
    """
    'tío' y 'padre' un mismo padre por lo que son hermanos. Este caso
    aplica cuando el idioma de 'tío' es 'nor' y el  de 'padre' es 'por'.
    """

    answer = siblings("tio", LX, "padre", LY).data
    expected = [("nor", "por",)]
    assert set(expected) == set(answer)

# -----------------------------------------------------------------------------

def test_are_siblings_positive_case():
    """
    Verifica que dos palabras son hermanas <=> tiene un padre en común

    A continuación, se pueden ver los hechos que cumplen la relación de
    hermano entre 'tio' y 'padre' (Note que el padre en este caso en la
    palabra 'abuelo' en idioma 'chi')

        + has_derived_form("chi", "abuelo", "nor", "tio")
        + etymology("por", "padre", "chi", "abuelo")

    En este otro párrafo se mostrarán las que cumplen la misma relación
    entre las palabras: 'bisabuelo' y 'tio_bisabuelo':

        + has_derived_form("ind", "tatarabuelo", "por", "bisabuelo")
        + has_derived_form("ind", "tatarabuelo", "ind", "tio_bisabuelo")

         (Note que el padre en este caso en la palabra 'abuelo'
         en idioma 'chi')

    La respuesta esperada es un set con el valor de 'True'
    """

    answer = are_siblings("bisabuelo", "tio_bisabuelo", R).data

    answer = answer + are_siblings("tio", "padre", R).data

    assert set(answer) == set([(True,)])

def test_are_siblings_negative_case():
    """
    Verifica que se retorne una False en vez de una lista vacía
    en caso de que los términos no sean hermanos

        Note que la respuesta a la relación de hermanos para las palabras:
            'primo'     -   'ego'
            'bisabuelo' -   'padre'

        es negativa debido a que en la base de conocimiento, no existen
        hechos con un mismo padre para niguna de las dos relaciones
        presentadas en estas palabras.
    """

    answer = are_siblings("primo", "ego", R).data
    answer = answer + are_siblings("bisabuelo", "padre", R).data

    assert set(answer) == set([(False,)])

def test_are_siblings_same_terms():
    """
    Verifica que se retorne un False en vez de una lista vacía
    en caso de que los términos no sean hermanos.

        Tal como sucede en la prueba anterior, no se cumple que estas palabras
        sean herman@s porque no existen hechos en el KB donde las palabras
        estén en idiomas distintos, y que procedan de un mismo padre
    """

    answer = are_siblings("ego", "ego", R).data
    answer = answer + are_siblings("padre", "padre", R).data
    assert set(answer) == set([(False,)])

# -----------------------------------------------------------------------------

def test_cousins_of_prueba():
    """
    Verifica todos los primos de la palabra 'prueba', incluyendo los de
    primer segundo y tercero grado
    """

    answer = cousins("prueba", LX, Y, LY).data
    expected = [('spa', 'primo', 'ita')]

    assert set(answer) == set(expected)


# -----------------------------------------------------------------------------

def test_are_cousins_positive_case():
    """
    Verifica el que dos términos son primos si tiene un ancestro en común
    con la misma lejanía, pero no es el término hermano.
    """

    answer = are_cousins("tio", LX, "prueba", LY, R).data

    assert answer


def test_are_cousins_negative_case():
    """
    Verifica que siempre se obtenga false y no una lista vacía en caso
    de que los términos no sea primos
    """

    answer = are_cousins("tatarabuelo", LX, "ego", LY, R).data

    assert not answer

# def test_are_cousins_same_term():
#     """
#     Verifica que un término no sea primo de si mismo
#     """
#     answer = are_cousins("ego", "ego", R).data
#     expected = [(False,)]
#     assert set(answer) == set(expected)
#
#
# -----------------------------------------------------------------------------

def test_child_has_one_parent():
    """
    Verifica que ego tenga solo un padre
    """
    answer = child("ego", "spa", Y, LY).data
    expected = [('padre', 'spa')]
    assert set(answer) == set(expected)

def test_child_get_all_of():
    """
    Verifica que el abuelo de ego tiene solo los dos hijos
    """
    answer = child(X, LX, "bisabuelo", LY).data

    # Existe una versión de abuelo en 'spa' y otra en 'por'
    expected = [('abuelo', 'ape', 'por'), ('tio_abuelo', 'por', 'spa')]
    assert set(answer) == set(expected)

def test_child_get_all_of_empty():
    """
    Verifica que ego no tienen hijos
    """
    answer = child(X, LX, "ego", "ita").data
    assert set(answer) == set([])

def test_child_has_no_parent():
    """
    El término tatarabuelo no tiene ningún padre
    """
    answer = child("tatarabuelo", "ind", P, LP).data
    assert set(answer) == set([])

def test_child_someone_not_exists():
    """
    Verifica que se retorne una lista vacía si alguno de los
    involucrados en la pregunta es no existe en la KB.
    """
    answer = child("ego", "", P, LP).data
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

def test_uncle_get():
    """
    Se obtienen todos los términos tíos; siendo un tío cualquier ancestro
    de un primo que no sea ancestro del término buscado.
    """
    answer = uncle(T, LT, "primo", "ita").data
    assert set(answer) == set([('padre', 'por')])

def test_uncle_get_nephew():
    """
    Se obtienen todos los términos que son sobrinos de otro.
    """
    answer = uncle("tio", "nor", X, LX).data
    assert set(answer) == set([('prueba', 'spa')])

# -----------------------------------------------------------------------------

def test_is_uncle_positive_case():
    """
    Verifica términos que son tíos de otros
    """
    answer = is_uncle("padre", "primo", R).data
    assert set(answer) == set([(True,)])

def test_is_uncle_negative_case():
    """
    Verifica términos que son tíos de otros
    """
    answer = is_uncle("padre", "hermano", R).data
    answer = answer + is_uncle("ego", "padre", R).data
    answer = answer + is_uncle("ego", "abuelo", R).data
    assert set(answer) == set([(False,), (False,), (False,)])

# -----------------------------------------------------------------------------

def test_cousins_distance_using_specific_distance():
    """
    Verifica que dos primos 'directos' obtengan una distancía de 1
    """
    answer = cousins_distance("abuelo", "ape", Y, LY, 1).data
    assert set(answer) == set([('tio_abuelo_seg', 'ape')])

def test_cousins_distance_not_cousins():
    """
    Verifica que si dos términos no son primns, se obtiene una lista vacía
    """
    answer = cousins_distance("padre", LX, "ego", LY, R).data
    assert set(answer) == set([])

# # -----------------------------------------------------------------------------