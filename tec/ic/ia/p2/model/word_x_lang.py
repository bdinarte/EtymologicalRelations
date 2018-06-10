# -----------------------------------------------------------------------------

from pyDatalog import pyDatalog
from os import path as ospath
from sys import path as syspath

from util.file_management import get_etim_database

# -----------------------------------------------------------------------------

"""
Además deberán poder realizarse las siguientes operaciones entre 
una palabra e idioma(s):

● Determinar si una palabra está relacionada con un idioma (Si / No)
● Obtener el conjunto de todas las palabras en un idioma originadas
por una palabra específica (e.g. una palabra específica en latín puede
originar múltiples palabras en español)
● Listar los idiomas relacionados con una palabra
"""


# -----------------------------------------------------------------------------

mainfile_path = ospath.abspath(__file__)
base_path = ospath.split(mainfile_path)[0]
base_path = ospath.split(base_path)[0]
syspath.append(base_path)


# -----------------------------------------------------------------------------

if __name__ == '__main__':

    data_df = get_etim_database(base_path)

    print('start')
    for i, row in data_df.iterrows():
        pyDatalog.assert_fact(row[1][4:],
                              row[0][:3], row[0][5:],
                              row[2][:3], row[2][5:])

    print(pyDatalog.ask("etymological_origin_of(aaq,'Pawanobskewi',_,X)"))

# -----------------------------------------------------------------------------