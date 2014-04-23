"""
Tests for the Purchase Order example schema.
"""

from __future__ import absolute_import

from datetime import date

from xs.test import uglify
from xs.parsers import EtreeParser

from .po import Item, Items, PurchaseOrder, USAddress

# The full example, the target for implementation
COMPLETE = b"""
<?xml version="1.0"?>
<purchaseOrder orderDate="1999-10-20">
   <shipTo country="US">
      <name>Alice Smith</name>
      <street>123 Maple Street</street>
      <city>Mill Valley</city>
      <state>CA</state>
      <zip>90952</zip>
   </shipTo>
   <billTo country="US">
      <name>Robert Smith</name>
      <street>8 Oak Avenue</street>
      <city>Old Town</city>
      <state>PA</state>
      <zip>95819</zip>
   </billTo>
   <comment>Hurry, my lawn is going wild!</comment>
   <items>
      <item partNum="872-AA">
         <productName>Lawnmower</productName>
         <quantity>1</quantity>
         <USPrice>148.95</USPrice>
         <comment>Confirm this is electric</comment>
      </item>
      <item partNum="926-AA">
         <productName>Baby Monitor</productName>
         <quantity>1</quantity>
         <USPrice>39.98</USPrice>
         <shipDate>1999-05-21</shipDate>
      </item>
   </items>
</purchaseOrder>
"""

# The output as currently supported.
SUPPORTED = b"""
<purchaseOrder orderDate="1999-10-20">
   <shipTo>
      <name>Alice Smith</name>
      <street>123 Maple Street</street>
      <city>Mill Valley</city>
      <state>CA</state>
      <zip>90952</zip>
   </shipTo>
   <billTo>
      <name>Robert Smith</name>
      <street>8 Oak Avenue</street>
      <city>Old Town</city>
      <state>PA</state>
      <zip>95819</zip>
   </billTo>
   <comment>Hurry, my lawn is going wild!</comment>
   <items>
      <item partNum="872-AA">
         <productName>Lawnmower</productName>
         <quantity>1</quantity>
         <USPrice>148.95</USPrice>
         <comment>Confirm this is electric</comment>
      </item>
      <item partNum="926-AA">
         <productName>Baby Monitor</productName>
         <quantity>1</quantity>
         <USPrice>39.98</USPrice>
         <shipDate>1999-05-21</shipDate>
      </item>
   </items>
</purchaseOrder>
"""


def test_building_purchase_order():
    p = PurchaseOrder()
    p.orderDate = date(1999, 10, 20)

    shipTo = USAddress()
    shipTo.name = "Alice Smith"
    shipTo.street = "123 Maple Street"
    shipTo.city = "Mill Valley"
    shipTo.state = "CA"
    shipTo.zip = "90952"

    billTo = USAddress()
    billTo.name = "Robert Smith"
    billTo.street = "8 Oak Avenue"
    billTo.city = "Old Town"
    billTo.state = "PA"
    billTo.zip = "95819"

    i1 = Item()
    i1.partNum = "872-AA"
    i1.productName = "Lawnmower"
    i1.quantity = 1
    # TODO: Fix Decimal to support floats
    i1.USPrice = "148.95"
    i1.comment = "Confirm this is electric"

    i2 = Item()
    i2.partNum = "926-AA"
    i2.productName = "Baby Monitor"
    i2.quantity = 1
    i2.USPrice = "39.98"
    i2.shipDate = date(1999, 5, 21)

    p.shipTo = shipTo
    p.billTo = billTo
    p.comment = "Hurry, my lawn is going wild!"
    p.items = Items()
    p.items.item.append(i1)
    p.items.item.append(i2)

    expected = uglify(SUPPORTED)
    print(expected)
    print(p.to_xml())
    assert expected == p.to_xml()


def test_parse_purchase_order():
    parser = EtreeParser()
    parser.register(PurchaseOrder)
    order = parser.parse_string(SUPPORTED)

    assert order is not None
    assert order.orderDate == date(1999, 10, 20)
    assert order.billTo is not None
    assert order.shipTo is not None
    assert order.shipTo.name == "Alice Smith"
    assert len(order.items.item) == 2
    assert order.items.item[1].shipDate == date(1999, 5, 21)

    expected = uglify(SUPPORTED)
    print(expected)
    print(order.to_xml())
    assert expected == order.to_xml()
