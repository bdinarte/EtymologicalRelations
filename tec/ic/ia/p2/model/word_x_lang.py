# -----------------------------------------------------------------------------

from pyDatalog import pyDatalog


# -----------------------------------------------------------------------------
# ------------------------------ Creating Terms -------------------------------
# -----------------------------------------------------------------------------

pyDatalog.create_terms('word_related_lang, set_of_words_in_lang, Word, '
                       'Lang, X, Y, LX, LY, A, B')

pyDatalog.create_terms('etymology, etymological_origin_of,'
                       'etymologically_related, has_derived_form,'
                       'is_derived_from, orthography')

pyDatalog.create_terms("is_son, is_ancestor, is_parent, lang_related_word,"
                       "is_son2, is_ancestor2, is_parent2")


# -----------------------------------------------------------------------------

word_related_lang(Word, Lang, True) <= word_related_lang(Word, Lang)

word_related_lang(Word, Lang, False) <= ~word_related_lang(Word, Lang)

word_related_lang(Word, Lang) <= (
    etymology(Lang, Word, X, Y)
)
word_related_lang(Word, Lang) <= (
    etymological_origin_of(X, Y, Lang, Word)
)
word_related_lang(Word, Lang) <= (
    etymologically_related(Lang, Word, X, Y)
)
word_related_lang(Word, Lang) <= (
    has_derived_form(X, Y, Lang, Word)
)
word_related_lang(Word, Lang) <= (
    is_derived_from(Lang, Word, X, Y)
)


# -----------------------------------------------------------------------------

# X = Primera palabra
# Y = Segunda palabra
# True es que X si es hija de Y
is_son(X, Y, LX, True) <= is_son(X, Y, LX)
is_son(X, Y, LX, False) <= ~is_son(X, Y, LX)

is_son(X, Y, LX) <= etymology(LX, X, LY, Y)
is_son(X, Y, LX) <= etymological_origin_of(LY, Y, LX, X)
is_son(X, Y, LX) <= has_derived_form(LY, Y, LX, X)
is_son(X, Y, LX) <= is_derived_from(LX, X, LY, Y)

is_parent(X, Y, LX) <= is_son(Y, X, LX)

is_ancestor(A, LX, B) <= is_parent(A, B, LX)
is_ancestor(X, LX, Y) <= is_parent(X, A, LX) & is_ancestor(A, LX, Y)


# -----------------------------------------------------------------------------

# X = Primera palabra
# Y = Segunda palabra
# True es que X si es hija de Y
is_son2(X, Y, LY, True) <= is_son2(X, Y, LY)
is_son2(X, Y, LY, False) <= ~is_son2(X, Y, LY)

is_son2(X, Y, LY) <= etymology(LX, X, LY, Y)
is_son2(X, Y, LY) <= etymological_origin_of(LY, Y, LX, X)
is_son2(X, Y, LY) <= has_derived_form(LY, Y, LX, X)
is_son2(X, Y, LY) <= is_derived_from(LX, X, LY, Y)

is_parent2(X, Y, LY) <= is_son2(Y, X, LY)

is_ancestor2(A, LX, B) <= is_parent2(A, B, LX)
is_ancestor2(X, LX, Y) <= is_parent2(X, Y, LX) & is_ancestor2(A, LX, X)

lang_related_word(X, LX) <=  is_ancestor(X, LX, B)
lang_related_word(X, LX) <=  is_ancestor2(Y, LX, X)
