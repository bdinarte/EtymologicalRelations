
# -----------------------------------------------------------------------------

import os
import sys
import logging
from pyDatalog import pyDatalog, pyEngine

parentdir = os.path.abspath(".")
projectdir = os.path.join(parentdir, "tec", "ic", "ia", "p2")
sys.path.insert(0, projectdir)

from tec.ic.ia.p2.view.user_interface import *

pyEngine.Logging = True
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

# -----------------------------------------------------------------------------


def run():
    UserInterface().mainloop()

if __name__ == '__main__':
    run()

# -----------------------------------------------------------------------------
