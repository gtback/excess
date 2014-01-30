"""
xs.attribute
------------

Implementation of xs:attribute
"""

from .core import _Component
from .simpletypes import _SimpleType


class Attribute(_Component):
    """Python representation of an xs:attribute.

    This class should be used to populate the "attributes" field in a
    ComplexType class.
    """

    def __init__(self, name, type_, default=None):
        """Create a new Attribute.

        type_ must be a _SimpleType.
        """
        if not issubclass(type_, _SimpleType):
            raise TypeError("The type of an Attribute must be a SimpleType")
        super(Attribute, self).__init__(name, type_, default=default)
        #TODO: add other xs:attribute-specific properties

    @property
    def multiple(self):
        return False
