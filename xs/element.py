from .compat import etree
from .complextype import ComplexType
from .core import _Component
from .simpletypes import _SimpleType


class Element(_Component):
    """Python representation of an xs:element.

    This class can be used in several ways:
    - By creating an instance.  The resulting object is a pseudo-type, and can
      be used as factory to create duplicate Elements with the same name and
      type.  These objects store their value (whose type must match the type
      of the element) in the .value property.
    - By adding to the `content` of a ComplexType class, as part of an
      xs.Sequence or xs.Choice.
    """

    def __init__(self, name, type_, default=None, value=None):
        """Create a new Element.

        If `value` is not `None`, it must be of type `type_`.
        """
        super(Element, self).__init__(name, type_, default=default)
        if value is not None:
            self.value = value
        #TODO: add other xs:element-specific properties

    def __call__(self, value):
        """Pseudo-factory to create instances of this type of element.

        `value` must be of the correct type.
        """
        return Element(self.name, self.type_, value=value)

    @property
    def multiple(self):
        #TODO: support maxOccurs>1
        return False

    # For Element instances (as opposed to components of xs.Sequence or
    # xs.Choice objects)
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = self.type_.check_value(value)

    def to_etree(self, obj=None):
        root = etree.Element(self.name)

        if obj:
            value = obj
        else:
            value = self.value

        if issubclass(self.type_, _SimpleType):
            root.text = self.type_.to_xml(value)
        else:
            root.append(self.type_.to_etree(value))

        return root

    def to_xml(self):
        return etree.tostring(self.to_etree())
