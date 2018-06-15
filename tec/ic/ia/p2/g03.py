
# -----------------------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath(".."))

import logging
from pyDatalog import pyDatalog, pyEngine

pyEngine.Logging = True
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

from view.user_interface import *

# -----------------------------------------------------------------------------


def run():
    UserInterface().mainloop()

if __name__ == '__main__':
    run()

# -----------------------------------------------------------------------------
