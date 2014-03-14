"""
An implementation of The Purchase Order Schema, po.xsd

See http://www.w3.org/TR/xmlschema-0/#POSchema
"""

import xs


class USAddress(xs.ComplexType):
    content = xs.Sequence(
        xs.Element("name", xs.String),
        xs.Element("street", xs.String),
        xs.Element("city", xs.String),
        xs.Element("state", xs.String),
        xs.Element("zip", xs.Decimal),
    )
    attributes = [
        #TODO: add 'fixed="US")
        xs.Attribute("country", xs.NMTOKEN)
    ]

class PurchaseOrderType(xs.ComplexType):
    content = xs.Sequence(
        xs.Element("shipTo", USAddress),
        xs.Element("billTo", USAddress)
    )

    attributes = [
        xs.Attribute("orderDate", xs.Date)
    ]

