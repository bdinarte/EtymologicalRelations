# -----------------------------------------------------------------------------

"""
Este código no es necesario ejecutarlo, su función es la de generar un
archivo procesado con los hechos a agregarse a la base de conocimiento del
programa
"""

import re
import os
import sys
from pyDatalog import pyDatalog
sys.path.insert(0, os.path.abspath('..'))
data = 'C:\\Git\\EtymologicalRelations\\tec\\ic\\ia\\p2\\files\\etymwn.tsv'
path = 'C:\\Git\\EtymologicalRelations\\tec\\ic\\ia\\p2\\files\\facts_julian.txt'


# -----------------------------------------------------------------------------

def get_valid_relations():
    return ['etymological_origin_of', 'has_derived_form',
            'etymology', 'etymologically_related']

# -----------------------------------------------------------------------------

def get_pattern_to_match_facts():
    return re.compile(
        u"([^:]+):\s*([^\s]+)\s*[^:]+:([^\s]+)\s*([^:]+):\s*(.+)",
        re.UNICODE
    )

# -----------------------------------------------------------------------------

def match_and_assert_fact(pattern, line):
    match = re.search(pattern, line)
    if match and match.group(3) in get_valid_relations():
        create_fact_string(match)

# -----------------------------------------------------------------------------

def create_fact_string(match):
    pyDatalog.assert_fact(
        match.group(3),
        match.group(1), match.group(2),
        match.group(4), match.group(5)
    )

# -----------------------------------------------------------------------------

from util.timeit import timeit

@timeit
def save_facts():

    pattern = get_pattern_to_match_facts()

    # with open(path, 'w', encoding='UTF-8') as output:
    with open(data, 'r', encoding='UTF-8') as input:

        for i, line in enumerate(input):
            match = re.search(pattern, line)

            if match and match.group(3) in get_valid_relations():
                create_fact_string(match)
                # string = create_fact_string(match)
                # output.write(string)

            if int(i) % 50000 == 0:
                print(i)

if __name__ == '__main__':
    save_facts()