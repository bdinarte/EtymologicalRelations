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

+ etymological_origin_of('','','','')
+ has_derived_form('','','','')
+ etymology('','','','')
+ etymologically_related('','','','')
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
pyDatalog.create_terms('input_percent')

# Relaciones para la función input_percent
