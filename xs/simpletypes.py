from .core import _DataType


class _SimpleType(_DataType):
    """A base class for built-in, atomic datatypes."""

    @classmethod
    def from_xml(cls, value):
        return cls._pytype(value)

    @staticmethod
    def to_xml(value):
        return value

    @classmethod
    def can_contain(cls, value):
        return isinstance(value, cls._pytype)


class Boolean(_SimpleType):
    """A class used to represent xs:boolean values."""

    _pytype = bool

    @staticmethod
    def from_xml(value):
        if value in ('0', 'false'):
            return False
        else:
            return True

    @staticmethod
    def to_xml(value):
        if value:
            return 'true'
        else:
            return 'false'

class String(_SimpleType):
    """A class used to represent xs:string values."""

    _pytype = unicode
