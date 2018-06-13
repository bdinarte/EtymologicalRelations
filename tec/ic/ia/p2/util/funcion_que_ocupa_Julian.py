

from pyDatalog import pyDatalog

valid_relations = ['etymological_origin_of',
                   'has_derived_form',
                   'etymology',
                   'etymologically_related']


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


line = 'xcl: ծանրաբեկ\trel:has_derived_form\txcl: ծանր'

process_line(line)

pyDatalog.create_terms('has_derived_form, X, Y')
print(pyDatalog.ask("has_derived_form(xcl,'ծանրաբեկ',X,Y)"))
