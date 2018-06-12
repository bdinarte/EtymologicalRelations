
from pyDatalog import pyDatalog
from os import path as ospath
from util.file_management import get_etim_database, get_file_content
import re

# ----------------------------------------------------------------------------

# TODO Eliminar este apartado
# Definir la ruta del proyecto
file_path = ospath.abspath(__file__)
file_folder = ospath.split(file_path)[0]
project_path = ospath.split(file_folder)[0]
# TODO Hasta aquí se elimina

languages = [
    'aaq', 'abe', 'abs', 'adt', 'afr', 'aii', 'ain', 'akk', 'akz', 'ale', 'alq',
    'amh', 'amj', 'ang', 'apw', 'ara', 'arg', 'arn', 'arq', 'arw', 'ary', 'arz',
    'ase', 'ast', 'auc', 'ava', 'ave', 'axm', 'ayl', 'aym', 'aze', 'bak', 'bar',
    'bdy', 'bel', 'ben', 'bft', 'bis', 'bod', 'bre', 'bua', 'bul', 'byn', 'cat',
    'ccc', 'ceb', 'ces', 'cha', 'chc', 'che', 'chn', 'cho', 'chr', 'chu', 'cic',
    'cmn', 'cop', 'cor', 'cre', 'crh', 'csb', 'cym', 'dan', 'del', 'dep', 'deu',
    'div', 'dsb', 'dtd', 'dum', 'efi', 'egy', 'ell', 'emn', 'eng', 'enm', 'enn',
    'epo', 'ess', 'est', 'ett', 'eus', 'evn', 'ewe', 'fao', 'fas', 'fij', 'fin',
    'fon', 'fra', 'frc', 'frk', 'frm', 'fro', 'frp', 'fry', 'fur', 'gae', 'gez',
    'gil', 'gla', 'gle', 'glg', 'glv', 'gmh', 'gml', 'gmy', 'goh', 'got', 'grc',
    'grn', 'grv', 'gsw', 'gug', 'guj', 'gul', 'gwi', 'hak', 'hat', 'hau', 'haw',
    'hbs', 'heb', 'hif', 'hil', 'hin', 'hit', 'hop', 'hsb', 'hun', 'hur', 'hye',
    'idb', 'ido', 'ike', 'ikt', 'iku', 'ina', 'ind', 'inz', 'ipk', 'isl', 'ita',
    'jam', 'jav', 'jbo', 'jpn', 'kal', 'kan', 'kat', 'kaw', 'kaz', 'kbd', 'khm',
    'kin', 'kir', 'kjh', 'kju', 'kky', 'kld', 'kmb', 'kok', 'kon', 'kor', 'kri',
    'krl', 'ksd', 'ksh', 'kum', 'kur', 'kzj', 'lad', 'lao', 'lat', 'lav', 'lij',
    'lim', 'lin', 'lit', 'liv', 'lkt', 'lld', 'lmo', 'lng', 'lou', 'ltc', 'ltz',
    'lua', 'lug', 'luo', 'lut', 'lzh', 'mah', 'mak', 'mal', 'mar', 'mas', 'mav',
    'mbc', 'mfr', 'mga', 'mic', 'min', 'mkd', 'mlg', 'mlt', 'mnc', 'mnk', 'mod',
    'moe', 'moh', 'mon', 'mri', 'msa', 'mwl', 'mxi', 'mya', 'myv', 'nah', 'nan',
    'nap', 'naq', 'nav', 'nay', 'nci', 'ndo', 'nds', 'nep', 'nld', 'nno', 'nob',
    'non', 'nor', 'nov', 'nys', 'obr', 'obt', 'oci', 'oco', 'odt', 'ofs', 'oge',
    'oji', 'okm', 'ood', 'orc', 'ori', 'orv', 'osp', 'oss', 'osx', 'ota', 'otk',
    'owl', 'p_gem', 'p_gmw', 'p_ine', 'p_sla', 'pal', 'pan', 'pap', 'pau', 'pcd',
    'pdt', 'peo', 'phn', 'pim', 'pis', 'pjt', 'pli', 'pml', 'pol', 'por', 'pox',
    'ppl', 'prg', 'pro', 'pus', 'quc', 'que', 'qwc', 'rap', 'rhg', 'rme', 'rmf',
    'rmq', 'roh', 'rom', 'ron', 'rop', 'rue', 'ruo', 'rup', 'rus', 'ryu', 'san',
    'sat', 'scn', 'sco', 'see', 'sei', 'sga', 'shh', 'sin', 'slk', 'slv', 'sme',
    'smo', 'sms', 'sna', 'som', 'sot', 'spa', 'sqi', 'srd', 'srn', 'srs', 'stg',
    'sth', 'stq', 'sun', 'sux', 'swa', 'swe', 'syc', 'szl', 'tah', 'tam', 'tat',
    'tcs', 'tcy', 'tel', 'tet', 'tew', 'tgk', 'tgl', 'tha', 'tir', 'tiv', 'tnq',
    'ton', 'tpi', 'tpw', 'tsn', 'tuk', 'tur', 'twf', 'twi', 'txb', 'tzm', 'uga',
    'uig', 'ukr', 'ulk', 'umb', 'umu', 'urd', 'uzb', 'vai', 'vec', 'vep', 'vie',
    'vls', 'vma', 'vol', 'wam', 'wit', 'wlm', 'wln', 'wol', 'wrh', 'wym', 'xaa',
    'xbm', 'xce', 'xcl', 'xho', 'xmb', 'xng', 'xno', 'xnt', 'xon', 'xpr', 'xtg',
    'xto', 'yid', 'yol', 'yor', 'yua', 'yue', 'yur', 'yxg', 'zai', 'zko', 'zku',
    'zsm', 'zul']
lang_index = eval(get_file_content(project_path, 'lang_index.txt'))

# ----------------------------------------------------------------------------


def get_lang_rows(dataframe, language):
    """
    Obtiene las filas del dataframe que corresponden al lenguaje definido
    :param dataframe: pandas dataframe con 3 columnas
    :param language: cadena de texto con la abreviación del lenguaje
    :return: un dataframe con las filas requeridas
    """
    start_row = lang_index[language][0]
    end_row = lang_index[language][1]

    return dataframe.iloc[start_row:end_row]


def get_relations_rows(dataframe, relations_list):
    """
    Obtiene las filas de un dataframe que contienen únicamente los tipos de
    relaciones buscadas
    :param dataframe: pandas dataframe con 3 columnas
    :param relations_list: lista de nombres del tipo de relaciones buscadas
    :return: un dataframe con las filas requeridas
    """
    escaped_relations = [re.escape(rel) for rel in relations_list]
    return dataframe[dataframe[1].str.contains('|'.join(escaped_relations))]


def assert_facts_from_dataframe(dataframe):
    """
    Dado un dataframe con una fila por cada hecho, se procesa cada
    fila y se insertan los hechos a la base de conocimiento
    :param dataframe: pandas dataframe con una fila por cada hecho a insertar
    :return: None
    """
    for i, row in dataframe.iterrows():

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

        pyDatalog.assert_fact(rel_name, lang1, word1, lang2, word2)
