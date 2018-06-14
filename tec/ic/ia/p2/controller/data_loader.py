# -----------------------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -----------------------------------------------------------------------------

import re
import multiprocessing
from test.timeit import timeit
from pyDatalog import pyDatalog
from itertools import takewhile, repeat

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

    cpu_count = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cpu_count)
    n_lines = get_file_rows_amount(filename)
    create_and_exec_chunks(pool, filename, n_lines, cpu_count)
    pool.close()

# -----------------------------------------------------------------------------

def create_and_exec_chunks(pool, filename, n_lines, cpu_count):

    current_line = 0
    last_line = n_x_cpu = n_lines // cpu_count

    jobs = []

    for _ in range(cpu_count - 1):
        args = (filename, current_line, last_line,)
        jobs.append(pool.apply_async(load_facts_from_chunk, args))
        last_line += n_x_cpu
        current_line += n_x_cpu

    args = (filename, last_line, n_lines,)
    jobs.append(pool.apply_async(load_facts_from_chunk, args))

    for job in jobs:
        job.get()

# -----------------------------------------------------------------------------

def exec_async_chunks(pool, filename, start, end):
    args = (filename, start, end,)
    pool.apply_async(load_facts_from_chunk, args).get()

# -----------------------------------------------------------------------------

def load_facts_from_chunk(filename, start, end):
    pattern = get_pattern_to_match_facts()
    with open(filename, mode="r", encoding="utf8") as file:
        for i, line in enumerate(file):
            if start <= i < end:
                match_and_assert_fact(pattern, line)

# -----------------------------------------------------------------------------

def match_and_assert_fact(pattern, line):
    match = re.search(pattern, line)
    if match and match.group(3) in get_valid_relations():
        assert_fact_from_match(match)

# -----------------------------------------------------------------------------

def assert_fact_from_match(match):
    pyDatalog.assert_fact(
        match.group(3),
        match.group(1), match.group(2),
        match.group(4), match.group(5)
    )

# -----------------------------------------------------------------------------

if __name__ ==  '__main__':
    filename = "C:\\Git\\EtymologicalRelations\\tec\\ic\\ia\\p2\\files\\etymwn.tsv"
    load_facts_from_databse(filename)

# -----------------------------------------------------------------------------
