# -----------------------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -----------------------------------------------------------------------------

from pyDatalog import pyDatalog
from model.word_x_word import *
from model.word_x_lang import *
from model.lang_x_lang import *

# -----------------------------------------------------------------------------
#
#                <ind:tatarabuelo>
#                   ____\_____________
#                  |                  \
#         <ind:tio_bisabuelo>    <por:bisabuelo>
#                 |                 ____\_____________
#                |                 |                  \
#      <chi:tio_abuelo_seg> <spa:tio_abuelo>    <chi:abuelo>
#              |                 |             ________\______
#             |                 |             |               \
#      <por:tio_ter>     <lat:tio_seg>    <nor:tio>       <lat:padre>
#           |                 |              |            _____\_______
#           \                 \              \            \            \
#     <lat:primo_ter>   <ita:primo_seg>   <ita:primo>  <ape:hermano>  <spa:ego>
#
# -----------------------------------------------------------------------------

+ etymology("spa", "ego", "lat", "padre")
+ etymological_origin_of("lat", "padre", "spa", "ego")

+ has_derived_form("ind", "tatarabuelo", "por", "bisabuelo")
+ has_derived_form("ind", "tatarabuelo", "ind", "tio_bisabuelo")

+ etymological_origin_of("ind", "tio_bisabuelo", "chi", "tio_abuelo_seg")
+ etymology("por", "tio_ter", "chi", "tio_abuelo_seg")

+ has_derived_form("por", "tio_ter", "lat", "primo_ter")
+ has_derived_form("por", "bisabuelo", "chi", "abuelo")

+ etymological_origin_of("por", "bisabuelo", "spa", "tio_abuelo")
+ etymology("lat", "padre", "chi", "abuelo")

+ has_derived_form("chi", "abuelo", "nor", "tio")
+ has_derived_form("lat", "padre", "ape", "hermano")

+ etymological_origin_of("nor", "tio", "ita", "primo")
+ etymology("lat", "tio_seg", "spa", "tio_abuelo")

+ has_derived_form("lat", "tio_seg", "ita", "primo_seg")

+ etymologically_related("spa", "ego", "ape", "hermano")
+ etymologically_related("nor", "tio", "lat", "padre")

# -----------------------------------------------------------------------------