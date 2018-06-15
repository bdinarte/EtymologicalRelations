# -----------------------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -----------------------------------------------------------------------------

import re
from util.timeit import timeit
from pyDatalog import pyDatalog, Logic

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

def load_facts(filename):
    pattern = get_pattern_to_match_facts()
    with open(filename, mode="r", encoding="utf8") as file:
        for i, line in enumerate(file):
            match_and_assert_fact(pattern, line)
            if(i%10000 == 0):
                print(i)


class MyLogic(Logic):

    def __init__(self):
        self.__dict__ = Logic.__dict__

# -----------------------------------------------------------------------------

if __name__ ==  '__main__':


    import dill
    filename = "C:\\Git\\EtymologicalRelations\\tec\\ic\\ia\\p2\\files\\etymwn3.tsv"
    Db = "C:\\Git\\EtymologicalRelations\\tec\\ic\\ia\\p2\\files\\Db.pkl"
    Pred_registry = "C:\\Git\\EtymologicalRelations\\tec\\ic\\ia\\p2\\files\\Pred_registry.pkl"
    session = "C:\\Git\\EtymologicalRelations\\tec\\ic\\ia\\p2\\files\\Pred_registry.pkl"

    from pprint import pprint

    # x = [50, 20, 10]
    # dill.dump_session(session)
    dill.load_session(session)

    print(x)
    # print(pyDatalog.ask("etymology('afr', 'denkbeeldig', X , Y)"))

# -----------------------------------------------------------------------------
