# ----------------------------------------------------------------------------

from pyDatalog import pyDatalog

# ----------------------------------------------------------------------------

# Definición de términos comunes a la mayoría de predicados
pyDatalog.create_terms('etymological_origin_of_active,'
                       'has_derived_form_active,'
                       'etymology_active,'
                       'etymologically_related_active')
pyDatalog.create_terms('etymological_origin_of,'
                       'has_derived_form,'
                       'etymology,'
                       'etymologically_related')
pyDatalog.create_terms('Lang1, Lang2, Word1, Word2, Total')

+ etymological_origin_of_active(True)
+ has_derived_form_active(True)
+ etymology_active(True)
+ etymologically_related_active(True)

# ----------------------------------------------------------------------------

# Términos para la función words_in_common
pyDatalog.create_terms('lang_common_words')

# Relaciones para la función words_in_common
lang_common_words(Lang1, Word1, Lang2, Word1) <= (
    etymology(Lang1, Word1, Lang2, Word1) &
    etymology_active(True)
)
lang_common_words(Lang1, Word1, Lang2, Word1) <= (
    etymological_origin_of(Lang1, Word1, Lang2, Word1) &
    etymological_origin_of_active(True)
)
lang_common_words(Lang1, Word1, Lang2, Word1) <= (
    has_derived_form(Lang1, Word1, Lang2, Word1) &
    has_derived_form_active(True)
)
lang_common_words(Lang1, Word1, Lang2, Word1) <= (
    etymologically_related(Lang1, Word1, Lang2, Word1) &
    etymologically_related_active(True)
)

# ----------------------------------------------------------------------------

# Términos para la función common_words_count
pyDatalog.create_terms('count_lang_common_words')

# Relaciones para la función words_in_common
(count_lang_common_words[Lang1, Lang2] == len_(Word1)) <= (
    lang_common_words(Lang1, Word1, Lang2, Word1)
)

# ----------------------------------------------------------------------------

# Términos para la función input_words
pyDatalog.create_terms('input_words')

# Relaciones para la función input_words
# Obtiene cuales palabras aportó un lenguaje a otro
input_words(Lang1, Word1, Lang2, Word2) <= (
    has_derived_form(Lang1, Word1, Lang2, Word2) &
    has_derived_form_active(True)
)
input_words(Lang1, Word1, Lang2, Word2) <= (
    etymology(Lang2, Word2, Lang1, Word1) &
    etymology_active(True)
)
input_words(Lang1, Word1, Lang2, Word2) <= (
    etymological_origin_of(Lang1, Word1, Lang2, Word2) &
    etymological_origin_of_active(True)
)

# ----------------------------------------------------------------------------

# Términos para la función count_input_words
pyDatalog.create_terms('count_input_words')

# Relaciones para la función count_input_words
(count_input_words[Lang1, Lang2] == len_(Word2)) <= (
    input_words(Lang1, Word1, Lang2, Word2)
)

# ----------------------------------------------------------------------------

# Términos para la función count_words_received
pyDatalog.create_terms('count_words_received')

# Relaciones para la función count_words_received
(count_words_received[Lang1] == len_(Word1)) <= (
    input_words(Lang2, Word2, Lang1, Word1)
)

# ----------------------------------------------------------------------------

# Términos para la función input_percent
pyDatalog.create_terms('input_percent', 'Percent', 'Partial')

# Relaciones para la función input_percent
# Obtiene el porcentaje que el lenguaje uno le aportó al segundo
(input_percent[Lang1, Lang2] == Percent) <= (
    (Partial == count_input_words[Lang1, Lang2]) &
    (Total == count_words_received[Lang2]) &
    (Percent == Partial/Total)
)

# ----------------------------------------------------------------------------

# Términos para la función all_lang_inputs
pyDatalog.create_terms('all_lang_inputs, inputs_words')

# Relaciones para la función all_lang_inputs
# Obtiene los lenguajes que aportan a otro lenguaje
inputs_words(Lang2, Lang1) <= (
    etymology(Lang2, Word2, Lang1, Word1) &
    etymology_active(True)
)
inputs_words(Lang2, Lang1) <= (
    etymological_origin_of(Lang1, Word1, Lang2, Word2) &
    etymological_origin_of_active(True)
)
inputs_words(Lang2, Lang1) <= (
    has_derived_form(Lang1, Word1, Lang2, Word2) &
    has_derived_form_active(True)
)

# Agrega el porcentaje de aporte
all_lang_inputs(Lang1, Lang2, Total) <= (
    inputs_words(Lang2, Lang1) &
    (Total == input_percent[Lang1, Lang2])
)

# ----------------------------------------------------------------------------

# Términos para la función max_input
pyDatalog.create_terms('max_input, max_orig, max_dest, Max_Orig, Max_Dest')

(max_orig[Max_Orig, Lang2] == max_(Max_Orig, order_by=Total)) <= (
    all_lang_inputs(Lang1, Lang2, Total) &
    (Max_Orig == (Total, Lang1, Lang2))
)

max_orig(Total, Lang2) <= (Total == max_orig[Max_Orig, Lang2])


+ etymology('abs', 'beta', 'zsm', 'beta')
+ etymology('aaq', 'prueba1', 'eng', 'prueba1')
+ etymology('aaq', 'senabe', 'eng', 'sannup')
+ etymological_origin_of('abe', 'waniigan', 'eng', 'waniigan')
+ etymological_origin_of('aaq', 'prueba2', 'eng', 'prueba2')
+ etymology('aaq', 'prueba3', 'eng', 'prueba3')
+ has_derived_form('equ', 'father', 'isd', 'son')
+ has_derived_form('equ', 'father', 'isd', 'son2')
+ etymology('isd', 'son3', 'equ', 'father3')
+ etymological_origin_of('sas', 'mom', 'isd', 'son4')
+ has_derived_form('sss', 'mom', 'isd', 'son5')
+ etymologically_related('lla','ma','alp','aca')

query_results = max_orig(Total, Lang2)
print(query_results)


print('\n------\n')
query_results = all_lang_inputs(Lang1, Lang2, Total)

print(query_results)
