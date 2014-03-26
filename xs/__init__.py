'''
Base module for the `xs` package.

Types should be imported from here, as the other files might be reorganized in
the future.
'''

from .simpletypes import (Boolean, Date, Decimal, Integer, NMTOKEN,
        PositiveInteger, String)
from .attribute import Attribute
from .complextype import ComplexType
from .content import Sequence
from .element import Element, TopLevelElement, UNBOUNDED
from .restriction import Restriction


__version__ = "0.1"
