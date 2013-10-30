"""Foundational types for the `xs` library

These do not correspond to actual types in the XML Schema Definition language,
but are rather used to encapsulate common functionality.  These should not
be used outside the xs library.
"""


class _DataType(object):

    def can_contain(self, value):
        """Test whether `value` is valid for this type"""
        raise NotImplementedError


class _Component(object):
    """Base class for Element and Attribute.

    This corresponds roughly to a "Declaration Component" as defined in XML
    Schema.
    """

    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_
