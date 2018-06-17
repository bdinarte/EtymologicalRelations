
from pyDatalog import pyDatalog

pyDatalog.create_terms('etymology_active,'
                       'etymological_origin_of_active,'
                       'has_derived_form_active,'
                       'etymologically_related_active')

# Definición inicial del estado de cada una de las relaciones disponibles
+ etymology_active(False)
+ has_derived_form_active(False)
+ etymologically_related_active(False)
+ etymological_origin_of_active(False)


def switch_etymology_state(new_state):
    """
    Cambio del estado de la relación sea activa/desactivada
    :param new_state: True (activa) / False (desactivada)
    :return: None
    """
    - etymology_active(not new_state)
    + etymology_active(new_state)


def switch_has_derived_form_state(new_state):
    """
    Cambio del estado de la relación sea activa/desactivada
    :param new_state: True (activa) / False (desactivada)
    :return: None
    """
    - has_derived_form_active(not new_state)
    + has_derived_form_active(new_state)


def switch_etymologically_related_state(new_state):
    """
    Cambio del estado de la relación sea activa/desactivada
    :param new_state: True (activa) / False (desactivada)
    :return: None
    """
    - etymologically_related_active(not new_state)
    + etymologically_related_active(new_state)


def switch_etymological_origin_of_state(new_state):
    """
    Cambio del estado de la relación sea activa/desactivada
    :param new_state: True (activa) / False (desactivada)
    :return: None
    """
    - etymological_origin_of_active(not new_state)
    + etymological_origin_of_active(new_state)
