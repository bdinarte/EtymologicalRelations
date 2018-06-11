# -----------------------------------------------------------------------------

import pandas as pd
from pyDatalog import pyDatalog
print("pyDatalog version " + pyDatalog.__version__)

# -----------------------------------------------------------------------------

def get_database(filename="B:\\etymwn.tsv"):
    dataframe = pd.read_csv(filename, sep="\t", header=None)
    return dataframe.values.tolist()

# -----------------------------------------------------------------------------

@pyDatalog.program()
def factorial():
    factorial[N] = N * factorial[N - 1]
    factorial[1] = 1
    factorial_of(X, Y) <= (factorial[X] == Y)

# -----------------------------------------------------------------------------

@pyDatalog.program()
def tutorial():
    manager['Mary'] = 'John'
    manager['Sam'] = 'Mary'
    manager['Tom'] = 'Mary'
    managers_of(X, Y) <= (manager[Y] == X)

# -----------------------------------------------------------------------------

# @pyDatalog.program()
# def case_son():
#
#     # El hijo de "bees" es "beeste"
#     + has_derived_form("afr", "bees", "afr", "beeste")
#     + is_derived_from("afr", "beeste", "afr", "bees")
#
#     # X = Primera palabra
#     # LY = Lenguaje de la segunda palabra
#     # Y = Segunda palabra
#     son(X, LY, Y) <= (has_derived_form(LX, X, LY, Y) &
#                       is_derived_from(LY, Y, LX, X))
#
#     print(son("bees", LY, Y))

# -----------------------------------------------------------------------------

@pyDatalog.program()
def case_is_son():

    # El hijo de "bees" es "beeste"
    + has_derived_form("afr", "bees", "afr", "beeste")
    + is_derived_from("afr", "beeste", "afr", "bees")

    # El hijo de "actininum" es "aktinium"
    + etymology("afr", "aktinium", "nld", "actinium")

    # En este caso "verbuiging" es hijo de "-ing"
    # + etymological_origin_of("afr", "-ing", "afr", "verbuiging")

    # X = Primera palabra
    # Y = Segunda palabra
    # True es que X si es hija de Y
    is_son(X, Y, True) <= (
        has_derived_form(LX, X, LY, Y) &
        is_derived_from(LY, Y, LX, X)
    )

    is_son(X, Y, True) <= (
        etymology(LX, X, LY, Y)
    )

    is_son(X, Y, False) <= ~is_son(X, Y, True)

    # # is_son(X, Y, R) <= (R == False)
    # #
    # is_son(X, Y, R) <= (has_derived_form(LX, X, LY, Y) &
    #                     is_derived_from(LY, Y, LX, X) & (R == True))
    #
    # is_son(X, X, R) <= (R == True)
    #
    print(is_son("bees", "beeste", R))

    print(is_son("aktinium", "actinium", R))

# -----------------------------------------------------------------------------

if __name__ == '__main__':
    print("Fin")
    # database = get_database()
    # print(pyDatalog.ask("factorial_of(4, R)"))
    # print(pyDatalog.ask("factorial[4] == R"))
    # print(pyDatalog.ask("managers_of('Mary', R)"))

# -----------------------------------------------------------------------------
