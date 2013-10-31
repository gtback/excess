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
    - By declaring a data descriptor on a ComplexType class.  In this case the
      actual `Element` object is attached to the class, not instances of the
      class, but each instance stores its own value for each element.
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

    # For Element instances (as opposed to descriptors on ComplexType classes)
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = self.type_.check_value(value)

    def to_etree(self):
        root = etree.Element(self.name)
        if issubclass(self.type_, _SimpleType):
            root.text = self.type_.to_xml(self.value)

        return root

    def to_xml(self):
        return etree.tostring(self.to_etree())
