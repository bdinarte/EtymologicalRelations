# -----------------------------------------------------------------------------

from pyDatalog import pyDatalog

# -----------------------------------------------------------------------------

def are_siblings():
    assert 1 == 1


# -----------------------------------------------------------------------------

def are_cousins():
    assert 1 == 1


# -----------------------------------------------------------------------------

@pyDatalog.program()
def is_son():
    """
    Determina si la palabra X es hija o derivada de Y
    :param X Primera palabra
    :param Y Segunda palabra
    :return: True si X es hija de Y
    """

    is_son(X, Y, False) <= ~is_son(X, Y, True)
    is_son(X, Y, True) <= etymology(LX, X, LY, Y)
    is_son(X, Y, True) <= etymological_origin_of(LY, Y, LX, X)

    is_son(X, Y, True) <= (
            has_derived_form(LY, Y, LX, X) &
            is_derived_from(LX, X, LY, Y)
    )


# -----------------------------------------------------------------------------

def is_uncle():
    assert 1 == 1


# -----------------------------------------------------------------------------

def cousins_grade():
    assert 1 == 1

# -----------------------------------------------------------------------------