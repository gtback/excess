"""
xs.element
------------

Implementation of xs:element
"""

from .compat import etree
from .core import _Component
from .simpletypes import _SimpleType


class Element(_Component):
    """Python representation of an xs:element.

    This should be used when defining the content of a `ComplexType` (as part
    of an xs.Sequence or xs.Choice).

    To define an element which occurs at the top level of a schema, use the
    `TopLevelElement` class.
    """

    def __init__(self, name, type_, default=None):
        """Create a new Element.

        If `value` is not `None`, it must be of type `type_`.
        """
        super(Element, self).__init__(name, type_, default=default)
        #TODO: add other xs:element-specific properties

    def __call__(self, value):
        """Pseudo-factory to create instances of this type of element.

        `value` must be of the correct type.
        """
        return TopLevelElement(self.name, self.type_, value=value)

    @property
    def multiple(self):
        #TODO: support maxOccurs>1
        return False

    def to_etree(self, value):
        """Return an ElementTree with the contents of this Element"""
        root = etree.Element(self.name)

        if issubclass(self.type_, _SimpleType):
            root.text = self.type_.to_xml(value)
        else:
            root.append(self.type_.to_etree(value))

        return root


class TopLevelElement(Element):
    """An Element which is not part of a ComplexType"""

    def __init__(self, *args, **kwargs):
        """Create a top-level schema element.

        You do not need to specify a value on creation, but it needs to be
        specified before calling to_etree.
        """
        value = kwargs.pop('value', None)
        super(TopLevelElement, self).__init__(*args, **kwargs)
        self.value = value

    @property
    def value(self):
        """
        The value contained in this TopLevelElement.
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Set the value of this TopLevelElement.

        `value` must be either None or the proper type for this Element
        """
        if value is None:
            self._value = None
        else:
            self._value = self.type_.check_value(value)

    def __getattr__(self, name):
        """Allow accessing the attributes of a contained complexType.

        If 'name' is not an attribute of the `Element` class itself,
        assume it is a property of the contained ComplexType object.
        """
        return getattr(self.value, name)

    def __setattr__(self, name, value):
        """ Allow setting the attributes of the contained complexType.
        """
        if name in ('name', 'type_', 'default', '_default', 'value', '_value'):
            object.__setattr__(self, name, value)
        else:
            # Create a contained object of the Element's type.
            if self.value is None:
                self.value = self.type_()
            object.__setattr__(self.value, name, value)

    def to_etree(self):
        if self.value is None:
            raise ValueError("Element has not been given a value")

        if issubclass(self.type_, _SimpleType):
            root = etree.Element(self.name)
            root.text = self.type_.to_xml(self.value)
        else:
            root = self.type_.to_etree(self.value, name=self.name)

        return root

    def to_xml(self):
        return etree.tostring(self.to_etree())

