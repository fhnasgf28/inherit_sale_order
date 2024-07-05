from odoo import fields,models,api,_

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'inherit sale order'

    due_date = fields.Date(string='Due Date')
    discount = fields.Float(string='Discount (%)', default=0.0)
    total_after_discount = fields.Monetary(string='Total After Discount', compute='_compute_total_after_discount',
                                           store=True, currency_field='currency_id')

    @api.depends('amount_total', 'discount')
    def _compute_total_after_discount(self):
        for order in self:
            discount_amount = (order.amount_total * order.discount) / 100
            order.total_after_discount = order.amount_total - discount_amount


