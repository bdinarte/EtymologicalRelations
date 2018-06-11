# -----------------------------------------------------------------------------

from pyDatalog import pyDatalog

# -----------------------------------------------------------------------------

def test_are_siblings():
    assert 1 == 1

# -----------------------------------------------------------------------------

def test_are_cousins():
    assert 1 == 1

# -----------------------------------------------------------------------------

def test_is_son():

    @pyDatalog.program()
    def case_is_son():

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

        is_son(X, Y, True) <= (
                has_derived_form(LY, Y, LX, X) &
                is_derived_from(LX, X, LY, Y)
        )

        assert is_son("beeste", "bees", R) == [(True,)]
        assert is_son("aktinium", "actinium", R) == [(True,)]
        assert is_son("verbuiging", "-ing", R) == [(True,)]



# -----------------------------------------------------------------------------

def test_is_uncle():
    assert 1 == 1


# -----------------------------------------------------------------------------

def test_cousins_grade():
    assert 1 == 1

# -----------------------------------------------------------------------------