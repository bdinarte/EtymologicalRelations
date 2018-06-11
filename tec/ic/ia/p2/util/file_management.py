
# -----------------------------------------------------------------------------

from pandas import read_csv
from os import path as ospath

# -----------------------------------------------------------------------------


def get_etim_database(base_path, filename='etymwn.tsv'):

    database_path = ospath.join(base_path, 'files', filename)
    data = read_csv(database_path, sep='\t', header=None)

    return data


def get_file_content(base_path, filename):

    file_path = ospath.join(base_path, 'files', filename)

    with open(file_path, encoding='utf-8') as file_content:
        content = file_content.read()

    return content