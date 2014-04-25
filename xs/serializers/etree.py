"""
xs.serializers.etree
------------

Serialize xs classes into etree nodes to represent as XML.
"""

from ..compat import etree
from ..complextype import ComplexType
from ..core import _DataType
from ..element import TopLevelElement
from ..simpletypes import _SimpleType

class EtreeSerializer(object):

    def serialize(self, obj):
        """Serialize an object to an etree.

        obj must be either a TopLevelElement or an instance of a ComplexType
        subclass.
        """
        if isinstance(obj, TopLevelElement):
            value = obj.value
            type_ = obj.type_
            name = obj.name
            if not value:
                msg = "TopLevelElement has not been assigned a value"
                raise ValueError(msg)
        elif isinstance(obj, ComplexType):
            value = obj
            type_ = obj.__class__
            name = type_.__name__
        else:
            raise Exception

        return self._serialize(value, type_, name)

    def _serialize(self, value, type_, name):
        if not issubclass(type_, _DataType):
            msg = "type_ must be an xs data type"
            raise ValueError(msg)

        node = etree.Element(name)

        if issubclass(type_, _SimpleType):
            node.text = type_.to_xml(value)
        elif issubclass(type_, ComplexType):
            if not isinstance(value, type_):
                msg = ("Unexpected object %s (%s) received when serializing "
                       "%s (%s)" % (value, type(value), name, type_))
                raise ValueError(msg)
            for attribute in type_.attributes:
                attribute_value = getattr(value, attribute.name)
                if attribute_value:
                    # Attibutes must have simple types
                    node.set(attribute.name,
                            attribute.type_.to_xml(attribute_value))

            content = type_.content
            if content:
                for component in content.components:
                    name = component.name
                    type_ = component.type_
                    val = getattr(value, name)

                    if component.multiple:
                        # TODO: enforce min_occurs when multiple=True
                        for each in val:
                            node.append(self._serialize(each, type_, name))
                    else:
                        if component._min_occurs > 0 and val is None:
                            msg = "Required element %s is missing" % name
                            raise ValueError(msg)
                        if val is not None:
                            node.append(self._serialize(val, type_, name))
        else:
            raise Exception

        return node
