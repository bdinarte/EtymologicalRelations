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


# ----------------------------------------------------------------------------

# Términos para la función words_in_common
pyDatalog.create_terms('lang_common_words, word_related_lang, '
                       'Lang, Word, X, Y')

# Relaciones para la función words_in_common
# Verifica si existe un hecho en el KB que tenga la relación
word_related_lang(Word, Lang) <= (
    etymology(Lang, Word, X, Y) & etymology_active(True)
)
word_related_lang(Word, Lang) <= (
    etymology(X, Y, Lang, Word) & etymology_active(True)
)
word_related_lang(Word, Lang) <= (
    etymological_origin_of(X, Y, Lang, Word) &
    etymological_origin_of_active(True)
)
word_related_lang(Word, Lang) <= (
    etymological_origin_of(Lang, Word, X, Y) &
    etymological_origin_of_active(True)
)
word_related_lang(Word, Lang) <= (
    etymologically_related(Lang, Word, X, Y) &
    etymologically_related_active(True)
)
word_related_lang(Word, Lang) <= (
    etymologically_related(X, Y, Lang, Word) &
    etymologically_related_active(True)
)
word_related_lang(Word, Lang) <= (
    has_derived_form(X, Y, Lang, Word) & has_derived_form_active(True)
)
word_related_lang(Word, Lang) <= (
    has_derived_form(Lang, Word, X, Y) & has_derived_form_active(True)
)
# Retorna las palabras en común
lang_common_words(Lang1, Lang2, Word) <= (word_related_lang(Word, Lang1) &
                                          word_related_lang(Word, Lang2))

# ----------------------------------------------------------------------------

# Términos para la función common_words_count
pyDatalog.create_terms('count_lang_common_words')

# Relaciones para la función words_in_common
(count_lang_common_words[Lang1, Lang2] == len_(Word1)) <= (
    lang_common_words(Lang1, Lang2, Word1)
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
pyDatalog.create_terms('max_input, Max_Percent')

(max_input[Max_Percent, Lang2] == max_(Max_Percent, order_by=Total)) <= (
    all_lang_inputs(Lang1, Lang2, Total) &
    (Max_Percent == (Total, Lang1, Lang2))
)

max_input(Total, Lang2) <= (Total == max_input[Max_Percent, Lang2])
