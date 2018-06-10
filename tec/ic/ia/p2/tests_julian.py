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

if __name__ == '__main__':
    database = get_database()
    # print(pyDatalog.ask("factorial_of(4, R)"))
    # print(pyDatalog.ask("factorial[4] == R"))
    # print(pyDatalog.ask("managers_of('Mary', R)"))

# -----------------------------------------------------------------------------
