"""
xs.serializers.xml
------------

Serialize xs classes into XML.
"""

from ..compat import etree

from .etree import EtreeSerializer

HEADER = b'<?xml version="1.0"?>'


class XMLSerializer(object):

    def __init__(self, etree_serializer=None, **options):
        if not etree_serializer:
            etree_serializer = EtreeSerializer(**options)

        self.etree_serializer = etree_serializer
        self.options = options

    def serialize(self, obj):
        parts = []
        if self.options.get('include_header'):
            parts.append(HEADER)

        parts.append(etree.tostring(self.etree_serializer.serialize(obj)))
        return b"".join(parts)
