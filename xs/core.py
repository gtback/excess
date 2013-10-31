"""Foundational types for the `xs` library

These do not correspond to actual types in the XML Schema Definition language,
but are rather used to encapsulate common functionality.  These should not
be used outside the xs library.
"""


class _DataType(object):
    """Base class for both simple and complex types."""

    @classmethod
    def check_value(cls, value):
        """Test whether `value` is valid for this type.

        This function should either convert `value` to a suitable value or
        raise a ValueError.
        """
        if not isinstance(value, cls):
            msg = "%s (type: %s) is not a %s" % (value, type(value), cls)
            raise ValueError(msg)
        return value


class _Component(object):
    """Base class for Element and Attribute.

    This corresponds roughly to a "Declaration Component" as defined in XML
    Schema.
    """

    def __init__(self, name, type_, default=None):
        self.name = name
        self.type_ = type_
        self.default = default

    @property
    def default(self):
        """Return the default value of this element.

        If minOccurs is 0, this will be either None or [], depending on whether
        maxOccurs is >1 or not.
        """
        if self._default is not None:
            return self._default
        elif self.multiple:
            return []
        else:
            return None

    @default.setter
    def default(self, value):
        self._default = value

    @property
    def multiple(self):
        raise NotImplementedError
