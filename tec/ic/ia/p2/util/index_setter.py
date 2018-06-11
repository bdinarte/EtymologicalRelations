
"""
Este código no es necesario ejecutarlo, su función es la de obtener datos
previos a la ejecución del programa principal que sirven para implementación
de ciertos algoritmos para alcanzar una mejor eficiencia.
"""

from util.file_management import get_etim_database
from os import path as ospath

# Definir la ruta de la base de datos
file_path = ospath.abspath(__file__)
file_folder = ospath.split(file_path)[0]
project_path = ospath.split(file_folder)[0]

print('Cargando base de datos a memoria...')
data_df = get_etim_database(project_path, filename="etymwn3.tsv")
print('Base de datos cargada a memoria!')

# Obtener los valores únicos que representan cada idioma
# first_col = data_df[0].tolist()
first_col = data_df[0].tolist()
print('\nObteniendo conjunto de idiomas:')
prefixes = list(set([value.split(':')[0] for value in first_col]))
prefixes.sort()
print(prefixes)

indexes = {}

# Obtener los prefijos que son más largos de lo común
long_prefixes = [prefix for prefix in prefixes if len(prefix) > 3]
# Obtener los índices de los prefijos largos y luego eliminarlos de la lista
for prefix in long_prefixes:
    print('Empezando: ' + prefix)
    index_list = data_df.index[data_df[0].str.contains(prefix)].tolist()
    indexes[prefix] = (index_list[0], index_list[-1]+1)
    print('Listo: ' + prefix)
    prefixes.remove(prefix)

# Recortar la columna con los prefijos para dejar solo el prefijo
data_df[0] = data_df[0].str[:3]
# Buscar los índices de cada prefijo de idioma
for prefix in prefixes:
    print('Empezando: ' + prefix)
    index_list = data_df.index[data_df[0].str.contains(prefix)].tolist()
    indexes[prefix] = (index_list[0], index_list[-1]+1)
    print('Listo: ' + prefix)

print(indexes)

