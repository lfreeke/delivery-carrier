# Copyright 2020 Therp BV <https://therp.nl>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo.tests.common import Form, TransactionCase


class TestCarrierServiceLevel(TransactionCase):
    def setUp(self):
        super(TestCarrierServiceLevel, self).setUp()
        self.testcarrier = self.env["delivery.carrier"].create(
            {
                "name": "Test Carrier",
                "product_id": self.env.ref("product.product_delivery_01").id,
            }
        )
        self.testcarrier_level = self.env["carrier.service.level"].create(
            {"name": "Test Carrier Level", "carrier_id": self.testcarrier.id}
        )
        self.picking_type = self.env["stock.picking.type"].create(
            {
                "name": "Test picking type",
                "sequence_code": "A Code",
                "code": "outgoing",
                "company_id": self.env.ref("stock.res_company_1").id,
                "warehouse_id": self.env.ref("stock.stock_warehouse_shop0").id,
            },
        )

    def test_onchange_carrier_service_level(self):
        """ Test onchange on_change_carrier_id"""
        form = Form(self.env["stock.picking"])
        form.carrier_id = self.testcarrier
        form.carrier_service_level_id = self.testcarrier_level
        form.picking_type_id = self.picking_type
        do = form.save()
        self.assertEqual(do.carrier_id, self.testcarrier)
        self.assertEqual(do.carrier_service_level_id, self.testcarrier_level)
        form.carrier_id = self.env["delivery.carrier"]
        do = form.save()
        self.assertFalse(do.carrier_service_level_id)
