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


comment = xs.TopLevelElement("comment", xs.String)


class _quantity(xs.Restriction, xs.PositiveInteger):
    max_exclusive = 100


class SKU(xs.String):
    #TODO: add pattern restriction
    pass


class Item(xs.ComplexType):
    content = xs.Sequence(
        xs.Element("productName", xs.String),
        xs.Element("quantity", _quantity),
        xs.Element("USPrice", xs.Decimal),
        xs.Element(ref=comment, min_occurs=0),
        #TODO: enforce min_occurs
        xs.Element("shipDate", xs.Date, min_occurs=0)
    )
    attributes = [
        #TODO: add 'fixed="US")
        xs.Attribute("partNum", SKU)
    ]


class Items(xs.ComplexType):
    content = xs.Sequence(
        xs.Element("item", Item, min_occurs=0, max_occurs=xs.UNBOUNDED)
    )


class PurchaseOrderType(xs.ComplexType):
    content = xs.Sequence(
        xs.Element("shipTo", USAddress),
        xs.Element("billTo", USAddress),
        comment,
        xs.Element("items", Items),
    )

    attributes = [
        xs.Attribute("orderDate", xs.Date)
    ]


PurchaseOrder = xs.TopLevelElement("purchaseOrder", PurchaseOrderType)
