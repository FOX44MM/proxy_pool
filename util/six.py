# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     six
   Description :
   Author :        JHao
   date：          2020/6/22
-------------------------------------------------
   Change Activity:
                   2020/6/22:
-------------------------------------------------
"""
__author__ = 'JHao'

from urllib.parse import urlparse
from importlib import reload as reload_six
from queue import Empty, Queue


def iteritems(d, **kw):
    return iter(d.items(**kw))


def withMetaclass(meta, *bases):
    """Create a base class with a metaclass."""

    class MetaClass(meta):

        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)

    return type.__new__(MetaClass, 'temporary_class', (), {})
