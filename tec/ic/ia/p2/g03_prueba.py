
# -----------------------------------------------------------------------------

from os import path as ospath
from sys import path as syspath

# -----------------------------------------------------------------------------

from util.file_management import get_etim_database
from user_interface import *

# -----------------------------------------------------------------------------

mainfile_path = ospath.abspath(__file__)
base_path = ospath.split(mainfile_path)[0]
syspath.append(base_path)


if __name__ == '__main__':
    pass
    # UserInterface().mainloop()

# -----------------------------------------------------------------------------

data_df = get_etim_database(base_path)

from pyDatalog import pyDatalog

print('comienza')
for i, row in data_df.iterrows():
    pyDatalog.assert_fact(row[1][4:],
                          row[0][:3], row[0][5:],
                          row[2][:3], row[2][5:])
    if int(i) % 500000 == 0:
        print('millon')

print(pyDatalog.ask("etymological_origin_of(aaq,'Pawanobskewi',_,X)"))