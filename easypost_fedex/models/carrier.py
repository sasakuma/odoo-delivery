# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) OncoDNA <http://www.oncodna.com>
#    See LICENSE file for full copyright and licensing details.
#
##############################################################################

from odoo import models, fields


class FedExEasypostCarrier(models.Model):
    _inherit = 'delivery.carrier'

    delivery_type = fields.Selection(selection_add=[('ep_fedex', "FedEx (Easypost)")])

    def ep_fedex_send_shipping(self, pickings):
        return self.ep_send_shipping(pickings)

    def ep_fedex_get_tracking_link(self, pickings):
        return self.ep_get_tracking_link(pickings)

    def ep_fedex_get_shipping_price_from_so(self, orders):
        return self.ep_get_shipping_price_from_so(orders)

    def ep_fedex_cancel_shipment(self, picking):
        self.ep_cancel_shipment(picking)
