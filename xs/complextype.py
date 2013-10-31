import inspect

from .attribute import Attribute
from .core import _DataType


def _is_attribute(obj):
    return isinstance(obj, Attribute)


class ComplexType(_DataType):

    def __init__(self):
        self._fields = {}

    @classmethod
    def _get_attributes(cls):
        for (name, obj) in inspect.getmembers(cls, _is_attribute):
            yield obj
