
# -----------------------------------------------------------------------------

from pandas import read_csv
from os import path as ospath

# -----------------------------------------------------------------------------

def get_etim_database(base_path):

    database_path = ospath.join(base_path, "files", "etymwn3.tsv")
    data = read_csv(database_path, sep='\t', header=None)

    return data
