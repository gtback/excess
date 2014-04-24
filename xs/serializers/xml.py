"""
xs.serializers.xml
------------

Serialize xs classes into XML.
"""

from ..compat import etree

from .etree import EtreeSerializer


class XMLSerializer(object):

    def __init__(self, etree_serializer=None):
        if not etree_serializer:
            etree_serializer = EtreeSerializer()

        self.etree_serializer = etree_serializer

    def serialize(self, obj):
        return etree.tostring(self.etree_serializer.serialize(obj))
