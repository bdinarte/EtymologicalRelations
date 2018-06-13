
"""
Este código no es necesario ejecutarlo, su función es la de generar un
archivo procesado con los hechos a agregarse a la base de conocimiento del
programa
"""

from pyDatalog import pyDatalog
from util.file_management import get_etim_database
from os import path as ospath
from util.file_management import get_file_content
from time import time

# Definir la ruta de la base de datos
file_path = ospath.abspath(__file__)
file_folder = ospath.split(file_path)[0]
project_path = ospath.split(file_folder)[0]

print('Cargando base de datos a memoria...')
s = time()
data_df = get_etim_database(project_path, filename="etymwn.tsv")
print('Base de datos cargada a memoria! ' + str(time() - s) + ' segundos.')

s = time()
with open('..\\files\\facts.txt', 'a', encoding='UTF-8') as facts_file:
    for i, row in data_df.iterrows():

        delim1 = '"' if "'" in row[0][5:] else "'"
        delim2 = '"' if "'" in row[2][5:] else "'"

        if row[0][:2] == 'p_':
            lang1 = row[0][:5]
            word1 = row[0][7:]
        else:
            lang1 = row[0][:3]
            word1 = row[0][5:]

        if row[2][:2] == 'p_':
            lang2 = row[2][:5]
            word2 = row[2][7:]
        else:
            lang2 = row[2][:3]
            word2 = row[2][5:]

        rel_name = row[1][4:].replace(':', '_')

        line = str('+ '
                   + rel_name + '('
                   + lang1 + ','
                   + delim1 + word1 + delim1 + ','
                   + lang2 + ','
                   + delim2 + word2 + delim2 + ')\n')

        if not(i + 1 == 8074 or i + 1 == 9662):
            facts_file.write(line)

        if int(i+1) % 500000 == 0:
            print(i)

print('Creación del archivo: ' + str(time() - s) + ' segundos.')

s = time()
print('Cargando a pyDatalog...')
pyDatalog.load(get_file_content(project_path, 'facts.txt'))
print('Carga completa! ' + str(time() - s) + ' segundos.')
