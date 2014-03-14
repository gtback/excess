"""
An implementation of The Purchase Order Schema, po.xsd

See http://www.w3.org/TR/xmlschema-0/#POSchema
"""

import xs


class PurchaseOrderType(xs.ComplexType):
    attributes = [
        xs.Attribute("orderDate", xs.Date)
    ]
