# -----------------------------------------------------------------------------

def test_are_siblings():
    assert 1 == 1

# -----------------------------------------------------------------------------

def test_are_cousins():
    assert 1 == 1

# -----------------------------------------------------------------------------

def test_is_son():

    from pyDatalog import pyDatalog

    @pyDatalog.program()
    def case_son():

        # El hijo de "bees" es "beeste"
        + has_derived_form("afr", "bees", "afr", "beeste")
        + is_derived_from("afr", "beeste", "afr", "bees")

        # X = Primera palabra
        # LY = Lenguaje de la segunda palabra
        # Y = Segunda palabra
        son(X, LY, Y) <= (has_derived_form(LX, X, LY, Y) &
                          is_derived_from(LY, Y, LX, X))

        print("Evaluando caso de son")
        print(son(X, LY,"beeste"))
        # assert son(X, None, None) == []
        # assert son(X, LY,"beeste") == [("bees", "afr")]
        # assert son("bees", LY, Y) == [("afr", "beeste")]

    @pyDatalog.program()
    def case_is_son():
        is_son(X, Y, False)
        is_son(X, Y, True) <= son(X, LY, Y)
        print(is_son("bees", "beeste", R))


    def is_son():
        return len(pyDatalog.ask("son('bees', LY, Y)").answers) > 0

    assert is_son()

        # El hijo es
        # + etymological_origin_of("afr", "Griekwa", "eng", "Griqua")
        # is_son(X, Y) <= (etymological_origin_of(L1, X, L2, Y))


# -----------------------------------------------------------------------------

def test_is_uncle():
    assert 1 == 1


# -----------------------------------------------------------------------------

def test_cousins_grade():
    assert 1 == 1

# -----------------------------------------------------------------------------