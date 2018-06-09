
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

data_df = get_etim_database(base_path, filename="etymwn.tsv")
print('obtenida la base')
# print(data_df.iloc[1036:1037])

# indexes = data_df.index[data_df[0].str.contains('afr')].tolist()
col0 = data_df[0].tolist()
print(set([x.split(sep=':')[0] for x in col0]))
# print(indexes)

"""

for i, row in data_df.iterrows():
    pyDatalog.assert_fact(row[1][4:],
                          row[0][:3], row[0][5:],
                          row[2][:3], row[2][5:])
    if int(i) % 10000 == 0:
        print(i)

print(pyDatalog.ask("etymological_origin_of(aaq,'Pawanobskewi',_,X)"))
"""