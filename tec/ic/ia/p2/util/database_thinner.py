# -----------------------------------------------------------------------------

import re
from random import randint
# -----------------------------------------------------------------------------

valid_relations = ['etymological_origin_of', 'has_derived_form',
                   'etymology', 'etymologically_related']


# -----------------------------------------------------------------------------

target_langs = []

# -----------------------------------------------------------------------------


def generate_thinned_db(filename):

    print("Recortando datos...")

    pattern = re.compile(
        u"([^:]+):\s*([^\s]+)\s*[^:]+:([^\s]+)\s*([^:]+):\s*(.+)",
        re.UNICODE
    )
    lang_percent = 2
    with open(filename, 'r', encoding='utf8') as _input:
        with open('..\\files\\thinned.tsv', 'a', encoding='utf8') as _output:
            for i, line in enumerate(_input):
                if randint(0, 99) < lang_percent:
                    match = re.search(pattern, line)

                    if match:
                        if match.group(3) in valid_relations:
                            if match.group(1) not in target_langs or \
                                    match.group(
                                    4) not in target_langs:
                                _output.write(line)

                if int(i+1) % 50000 == 0:
                    print('Recortados: ' + str(i+1))

# -----------------------------------------------------------------------------


if __name__ == '__main__':
    generate_thinned_db('..\\files\\etymwn.tsv')

# -----------------------------------------------------------------------------