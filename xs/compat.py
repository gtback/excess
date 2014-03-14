"""
Python version compatibility
"""

import sys

# Syntax sugar.
_ver = sys.version_info

#: Python 2.x?
is_py2 = (_ver[0] == 2)

#: Python 3.x?
is_py3 = (_ver[0] == 3)


if is_py2:
    bytes = str
    str = unicode
    basestring = basestring


elif is_py3:
    str = str
    bytes = bytes
    basestring = (str, bytes)


class UnicodeMixin(object):
    """Let __str__ and __unicode functions work as expected on Python 2 and 3.

    This code was adapted from:
        http://lucumr.pocoo.org/2011/1/22/forwards-compatible-python/
    """
    if is_py3:
        __str__ = lambda x: x.__unicode__()
    else:
        __str__ = lambda x: unicode(x).encode('utf-8')


#TODO: test using lxml etree.
import xml.etree.cElementTree as etree
