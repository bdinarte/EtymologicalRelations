
"""
Este código no es necesario ejecutarlo, su función es la de generar un
archivo procesado con los hechos a agregarse a la base de conocimiento del
programa
"""

from pyDatalog import pyDatalog
from util.file_management import get_etim_database
from os import path as ospath

# Definir la ruta de la base de datos
file_path = ospath.abspath(__file__)
file_folder = ospath.split(file_path)[0]
project_path = ospath.split(file_folder)[0]
"""
print('Cargando base de datos a memoria...')
data_df = get_etim_database(project_path, filename="etymwn.tsv")
print('Base de datos cargada a memoria!')
"""

def get_file_content(filename):
    with open(filename, encoding='utf-8') as f:
        content = f.read()
    return content

"""
with open('facts.txt', 'a', encoding='UTF-8') as facts_file:
    for i, row in data_df.iterrows():
        delim1 = '"' if "'" in row[0][5:] else "'"
        delim2 = '"' if "'" in row[2][5:] else "'"
        line = str('+ '
                   + row[1][4:] + '('
                   + row[0][:3] + ','
                   + delim1 + row[0][5:] + delim1 + ','
                   + row[2][:3] + ','
                   + delim2 + row[2][5:] + delim2 + ')\n')

        facts_file.write(line)

        if int(i+1) % 1000 == 0:
            print(i)
"""

pyDatalog.load(get_file_content('facts.txt'))


"""
p_gmw = (5149120, 5149122)
p_gem: (5149108, 5149120)
p_ine: (5149122, 5149125)
p_sla: (5149125, 5149249)
"""
