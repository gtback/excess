from __future__ import absolute_import

from datetime import date
import re

from .po import PurchaseOrder, USAddress

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
   <comment>Hurry, my lawn is going wild<!/comment>
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
</purchaseOrder>
"""

UGLIFIED = re.sub(b">\s+<", b"><", SUPPORTED).strip()


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

    p.shipTo = shipTo
    p.billTo = billTo
    print(UGLIFIED)
    print(p.to_xml())
    assert UGLIFIED == p.to_xml()
