from __future__ import absolute_import

from datetime import date

from .po import PurchaseOrderType, USAddress

def test_building_purchase_order():
    p = PurchaseOrderType()
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
    print p.to_xml()
    raise
