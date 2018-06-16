# -----------------------------------------------------------------------------

import re
import os
import sys
from util.timeit import timeit
from pyDatalog import pyDatalog
sys.path.insert(0, os.path.abspath('..'))

# -----------------------------------------------------------------------------

valid_relations = ['etymological_origin_of', 'has_derived_form',
                   'etymology', 'etymologically_related']

# -----------------------------------------------------------------------------

lang_blacklist = ["xcl", "rus", "kat", "urd", "tha", "tel"]

# -----------------------------------------------------------------------------

def get_pattern_to_match_facts():
    return re.compile(
        u"([^:]+):\s*([^\s]+)\s*[^:]+:([^\s]+)\s*([^:]+):\s*(.+)",
        re.UNICODE
    )

# -----------------------------------------------------------------------------

def match_and_assert_fact(pattern, line):

    match = re.search(pattern, line)

    if match:
        if match.group(3) in valid_relations:
            if match.group(1) not in lang_blacklist:
                if match.group(4) not in lang_blacklist:
                    assert_fact_from_match(match)

# -----------------------------------------------------------------------------

def assert_fact_from_match(match):
    pyDatalog.assert_fact(
        match.group(3),
        match.group(1), match.group(2),
        match.group(4), match.group(5)
    )

# -----------------------------------------------------------------------------

@timeit
def load_facts_from_database(filename):

    print("Cargando datos...")

    pattern = get_pattern_to_match_facts()
    with open(filename, 'r', encoding='UTF-8') as input:

        for i, line in enumerate(input):
            match_and_assert_fact(pattern,  line)

            if int(i) % 50000 == 0:
                print(i)

# -----------------------------------------------------------------------------

if __name__ == '__main__':
    load_facts_from_database()

# -----------------------------------------------------------------------------