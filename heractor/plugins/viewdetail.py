#coding:utf-8

"""
Построение View/Detail структур страниц
"""


def before(structure, config, env={}, extra={}):
    """
    Ищет в структуре компонент, и достраивает подэлементы
    """