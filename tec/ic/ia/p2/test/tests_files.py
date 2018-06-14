# -----------------------------------------------------------------------------

import os
import re
from multiprocessing import Pool, cpu_count
from test.timeit import timeit
from pyDatalog import pyDatalog
from itertools import (takewhile,repeat)

import logging
from pyDatalog import pyEngine
# pyEngine.Logging = True
# logging.basicConfig(level=logging.DEBUG)

# -----------------------------------------------------------------------------

pattern = re.compile(u"([^:]+):\s*([^\s]+)\s*[^:]+:([^\s]+)\s*([^:]+):\s*(.+)", re.LOCALE)
filename = "C:\\Git\\EtymologicalRelations\\tec\\ic\\ia\\p2\\files\\etymwn.tsv"

# -----------------------------------------------------------------------------

@timeit
def rawincount(filename):
    f = open(filename, 'rb')
    bufgen = takewhile(lambda x: x, (f.raw.read(1024*1024) for _ in repeat(None)))
    return sum(buf.count(b'\n') for buf in bufgen) + 1

# -----------------------------------------------------------------------------

valid_relations = ['etymological_origin_of',
                   'has_derived_form',
                   'etymology',
                   'etymologically_related']

# @timeit
def check_and_assert_line(line):
    match = re.search(pattern, line)
    if match and match.group(3) in valid_relations:
        pyDatalog.assert_fact(match.group(3), match.group(1), match.group(2),
                              match.group(4), match.group(5))
    elif not match:
        print(line)

# -----------------------------------------------------------------------------


def process_line(line_string):
    """
    Dada una cadena de texto con representando una fila de tres columnas
    separadas con \t, se procesa la fila y se inserta el hecho a la base de
    conocimiento
    :param line_string: linea representando una fila de 3 columnas
    :return: None
    """

    split_line = line_string.split(sep='\t')

    rel_name = split_line[1][4:]

    if rel_name in valid_relations:
        if split_line[0][:2] == 'p_':
            lang1 = split_line[0][:5]
            word1 = split_line[0][7:]
        else:
            lang1 = split_line[0][:3]
            word1 = split_line[0][5:]

        if split_line[2][:2] == 'p_':
            lang2 = split_line[2][:5]
            word2 = split_line[2][7:]
        else:
            lang2 = split_line[2][:3]
            word2 = split_line[2][5:]

        pyDatalog.assert_fact(rel_name, lang1, word1, lang2, word2)

# -----------------------------------------------------------------------------

def process_wrapper(start, end):
    with open(filename, mode="r", encoding="utf8") as file:
        for i, line in enumerate(file):
            if start <= i < end:
                check_and_assert_line(line)

# -----------------------------------------------------------------------------

@timeit
def proccess_text(filename):

    processes_count = cpu_count()

    pool = Pool(processes=processes_count)
    jobs = []

    lines_count = rawincount(filename)

    # 1 parte de las muestras serán generadas por cada proceso
    lines_per_processes = lines_count // processes_count
    remaining_lines = lines_count - (lines_per_processes * processes_count)

    current_line = 0
    last_line = lines_per_processes

    for n in range(processes_count-1):
        jobs.append(
            pool.apply_async(process_wrapper, (current_line, last_line,))
        )
        current_line += lines_per_processes
        last_line += lines_per_processes

    jobs.append(
        pool.apply_async(process_wrapper, (last_line, last_line + remaining_lines,))
    )

    for job in jobs:
        job.get()

    pool.close()

# -----------------------------------------------------------------------------

if __name__ ==  '__main__':
    proccess_text(filename)

# -----------------------------------------------------------------------------
