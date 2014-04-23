"""
xs.parsers.etree
------------

Parse etrees into xs-based classes.
"""

from ..compat import etree
from ..simpletypes import _SimpleType
from ..core import _DataType
from ..element import TopLevelElement

class EtreeParser(object):

    def __init__(self):
        self.types = {}

    def register(self, item, name=None):
        """
        """
        if not name:
            if isinstance(item, TopLevelElement):
                type_ = item
                name = item.name
            elif isinstance(item, type) and issubclass(item, _DataType):
                type_ = item
                name = type_.__name__
            else:
                raise ValueError("Unable to register %s" % item)
        self.types[name] = type_

    def parse_string(self, string):
        """
        """
        root = etree.fromstring(string.strip())
        return self._parse_root(root)

    def parse(self, filename):
        """
        """
        tree = etree.parse(filename)
        return self._parse_root(tree.getroot())

    def _parse_root(self, root):
        """
        """

        name = root.tag
        if name not in self.types:
            raise ValueError("Unknown element %s" % name)

        # Instantiate the correct type
        type_ = self.types[name]

        return self._parse_node(root, type_)

    def _parse_node(self, node, type_):
        obj = type_()

        components = type_._component_dict()

        # Parse attributes
        for (key, value) in node.attrib.items():
            component = components[key]
            setattr(obj, key, component.type_.from_xml(value))

        # Parse child elements
        for child in node:
            component = components[child.tag]

            if issubclass(component.type_, _SimpleType):
                value = child.text.strip()
            else:
                value = self._parse_node(child, component.type_)

            if component.multiple:
                getattr(obj, child.tag).append(value)
            else:
                setattr(obj, child.tag, value)

        return obj
