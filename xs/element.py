from .compat import etree
from .core import _Component
from .simpletypes import _SimpleType


class Element(_Component):
    """Python representation of an xs:element.

    Elements can be constructed and used as data descriptors on ComplexType
    classes.
    """

    def __init__(self, name, type_):
        super(Element, self).__init__(name, type_)
        #TODO: add other xs:element-specific properties

    def __call__(self, value):
        return SimpleElement(self.name, self.type_, value)

    def __get__(self, instance, owner):
        # If calling on a class rather than an instance of that class, return
        # the Element itself, rather than the instance's value for the Element.
        if instance is None:
            return self

        # If this instance has been given a value, return that value.
        # Otherwise, return the element's default value.
        return instance._fields.get(self.name, self.default)

    def __set__(self, instance, value):
        if ((value is not None) and (not self.type_.can_contain(value))):
            if self.multiple and isinstance(value, list):
                # TODO: if a list, check if each item in the list is the
                # correct type.
                pass
            elif self.type_._try_cast:
                value = self.type_(value)
            else:
                raise ValueError("%s must be a %s, not a %s" %
                                    (self.name, self.type_, type(value)))
        instance._fields[self.name] = value

        #TODO: implement callback hooks

    @property
    def multiple(self):
        #TODO: support maxOccurs>1
        return False

    @property
    def default(self):
        """Return the default value of this element.

        If minOccurs is 0, this will be either None or [], depending on whether
        maxOccurs is >1 or not.
        """
        if self.multiple:
            return []
        else:
            return None


class SimpleElement(_Component):

    def __init__(self, name, type_, value):
        super(SimpleElement, self).__init__(name, type_)
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not self.type_.can_contain(value):
            raise ValueError("Invalid type")

        self._value = value

    def to_etree(self):
        root = etree.Element(self.name)
        if issubclass(self.type_, _SimpleType):
            root.text = self.type_.to_xml(self.value)

        return root

    def to_xml(self):
        return etree.tostring(self.to_etree())
