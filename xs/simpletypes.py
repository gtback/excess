from datetime import date
from decimal import Decimal

from .compat import basestring, etree, str
from .core import _DataType


class _SimpleType(_DataType):
    """A base class for built-in, atomic datatypes."""

    @classmethod
    def from_xml(cls, value):
        return cls.check_value(value)

    @staticmethod
    def to_xml(value):
        return str(value)

    @classmethod
    def check_value(cls, value):
        return cls._pytype(value)


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


class Date(_SimpleType):
    """A class used to represent xs:date values."""

    _pytype = date

    @staticmethod
    def from_xml(value):
        #TODO: should we be be a bit more flexible here?

        return date(*[int(x) for x in value.split('-')])

    @staticmethod
    def to_xml(value):
        return value.isoformat()

    @classmethod
    def check_value(cls, value):
        # TODO: roll into _SimpleType.check_value
        if isinstance(value, date):
            return value
        elif isinstance(value, basestring):
            return cls.from_xml(value)
        raise ValueError("Invalid value for Date object: %s (type %s)" %
                         (value, type(value)))


class Integer(_SimpleType):
    """A class used to represent xs:integer values."""

    _pytype = int


class PositiveInteger(Integer):
    """A class used to represent xs:positiveInteger values."""

    @classmethod
    def check_value(cls, value):
        value = super(PositiveInteger, cls).check_value(value)
        if value <= 0:
            raise ValueError("%s is not positive" % value)
        return value


class Decimal(_SimpleType):
    """A class used to represent xs:decimal values."""

    _pytype = Decimal


class String(_SimpleType):
    """A class used to represent xs:string values."""

    _pytype = str  # Unicode string


class NMTOKEN(String):
    """A class used to represent xs:NMTOKEN values."""

    #TODO: actually restrict to not including whitespace
    pass
