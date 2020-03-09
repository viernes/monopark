from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # def _compute_access_url(self):
    #     super(SaleOrder, self)._compute_access_url()
    #     for order in self:
    #         order.access_url = '/my/orders/customized/%s' % (order.id)
    #


