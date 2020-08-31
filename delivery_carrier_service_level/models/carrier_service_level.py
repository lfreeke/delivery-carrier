# Copyright 2020 Therp BV.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class ServiceLevel(models.Model):
    _name = "carrier.service.level"
    _description = "carrier service levels"
    _order = "carrier_id, code"

    code = fields.Char(string="Carrier Service Level Code")
    name = fields.Char(string="Carrier Service Level Name", required=True)
    carrier_id = fields.Many2one("delivery.carrier", string="Carrier")
    active = fields.Boolean(default=True)
