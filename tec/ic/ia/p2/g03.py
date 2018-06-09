
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
    UserInterface().mainloop()

# -----------------------------------------------------------------------------

