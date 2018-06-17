
from pyDatalog import pyDatalog

pyDatalog.create_terms('etymology_active,'
                       'etymological_origin_of_active,'
                       'has_derived_form_active,'
                       'etymologically_related_active')

+ etymology_active(True)
+ has_derived_form_active(True)
+ etymologically_related_active(True)
+ etymological_origin_of_active(True)


def switch_etymology_state(new_state):
    - etymology_active(not new_state)
    + etymology_active(new_state)


def switch_has_derived_form_state(new_state):
    - has_derived_form_active(not new_state)
    + has_derived_form_active(new_state)


def switch_etymologically_related_state(new_state):
    - etymologically_related_active(not new_state)
    + etymologically_related_active(new_state)


def switch_etymological_origin_of_state(new_state):
    - etymological_origin_of_active(not new_state)
    + etymological_origin_of_active(new_state)
