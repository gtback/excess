"""
xs.parsers.etree
------------

Parse etrees into xs-based classes.
"""

from ..compat import etree

class EtreeParser(object):

    def __init__(self):
        self.types = {}

    def register(self, type_, name=None):
        """
        """
        if not name:
            name = type_.__name__
        self.types[name] = type_

    def parse_string(self, string):
        """
        """
        root = etree.fromstring(string)
        return self._parse(root)

    def parse(self, filename):
        """
        """
        tree = etree.parse(filename)
        return self._parse(tree.getroot())

    def _parse(self, root):
        """
        """

        name = root.tag
        if name not in self.types:
            raise ValueError("Unknown element %s" % name)

        # Instantiate the correct type
        type_ = self.types[name]
        obj = type_()

        components = type_._component_dict()

        for (k, v) in root.attrib:
            setattr(obj, k, v)

        for child in root:
            component = components[child.tag]

            if component.multiple:
                getattr(obj, child.tag).append(child.text)
            else:
                setattr(obj, child.tag, child.text)

        return obj
