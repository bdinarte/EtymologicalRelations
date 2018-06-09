
from util.file_management import get_etim_database
from os import path as ospath

file_path = ospath.abspath(__file__)
file_folder = ospath.split(file_path)[0]
project_path = ospath.split(file_folder)[0]

print('Cargando base de datos a memoria...')
data_df = get_etim_database(project_path, filename="etymwn.tsv")
print('Base de datos cargada a memoria!')

first_col = data_df[0].tolist()
print('\nObteniendo conjunto de idiomas:')
prefixes = list(set([value.split(':')[0] for value in first_col]))
prefixes.sort()
print(prefixes)

# Conjunto de idiomas:
"""
['aaq', 'abe', 'abs', 'adt', 'afr', 'aii', 'ain', 'akk', 'akz', 'ale', 'alq', 
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
'zsm', 'zul']"""

