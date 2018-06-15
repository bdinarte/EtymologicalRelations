# -----------------------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -----------------------------------------------------------------------------

import re
import multiprocessing
from threading import Thread
from util.timeit import timeit
from pyDatalog import pyDatalog, Logic
from itertools import takewhile, repeat

import logging
from pyDatalog import pyEngine

pyEngine.Logging = True
logging.basicConfig(level=logging.DEBUG)


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

def get_file_rows_amount(filename):
    with open(filename, mode="rb") as file:
        size = 1048576 # 1020 * 1024
        buf = (file.raw.read(size) for _ in repeat(None))
        bufgen = takewhile(lambda x: x, buf)
        return sum(buf.count(b'\n') for buf in bufgen) + 1

# -----------------------------------------------------------------------------

@timeit
def load_facts_from_databse(filename):
    cpu_count = 50
    n_lines = get_file_rows_amount(filename)
    create_and_exec_chunks(filename, n_lines, cpu_count)

# -----------------------------------------------------------------------------

def create_and_exec_chunks(filename, n_lines, cpu_count):

    Logic()
    facts_set = Logic(True)

    current_line = 0
    last_line = n_x_cpu = n_lines // cpu_count

    threads = []

    for _ in range(cpu_count - 1):
        args = (facts_set, filename, current_line, last_line,)
        threads.append(Thread(target=load_facts_from_chunk, args=args))
        last_line += n_x_cpu
        current_line += n_x_cpu

    args = (facts_set, filename, last_line, n_lines,)
    threads.append(Thread(target=load_facts_from_chunk, args=args))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

# -----------------------------------------------------------------------------

def load_facts_from_chunk(facts_set, filename, start, end):
    # print(facts_set)
    print("thread procesando de {} hasta {}".format(start, end))
    pattern = get_pattern_to_match_facts()
    with open(filename, mode="r", encoding="utf8") as file:
        for i, line in enumerate(file):
            if start <= i < end:
                match_and_assert_fact(pattern, line)
                if(i%1000 == 0):
                    print(i)

# -----------------------------------------------------------------------------

def match_and_assert_fact(pattern, line):
    match = re.search(pattern, line)
    if match and match.group(3) in get_valid_relations():
        assert_fact_from_match(match)

# -----------------------------------------------------------------------------

def assert_fact_from_match(match):
    pass
    # pyDatalog.assert_fact(
    #     match.group(3),
    #     match.group(1), match.group(2),
    #     match.group(4), match.group(5)
    # )

# -----------------------------------------------------------------------------

if __name__ ==  '__main__':

    filename = "C:\\Git\\EtymologicalRelations\\tec\\ic\\ia\\p2\\files\\etymwn.tsv"

    # load_facts_from_databse(filename)
    # Logic()
    # logic_set = Logic(True)
    # print(logic_set)

    load_facts_from_databse(filename)
    # load_facts_from_chunk(None, filename, 0, 300)
    # print(pyDatalog.ask("etymology('afr', 'denkbeeldig', X , Y)"))


# -----------------------------------------------------------------------------
