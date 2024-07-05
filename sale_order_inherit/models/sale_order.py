from odoo import fields,models,api,_
from datetime import timedelta

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'inherit sale order'

    due_date = fields.Date(string='Due Date', compute='_compute_due_date', store=True)
    discount = fields.Float(string='Discount (%)', default=0.0)
    total_after_discount = fields.Monetary(string='Total After Discount', compute='_compute_total_after_discount',
                                           store=True, currency_field='currency_id')

    @api.depends('amount_total', 'discount')
    def _compute_total_after_discount(self):
        for order in self:
            discount_amount = (order.amount_total * order.discount) / 100
            order.total_after_discount = order.amount_total - discount_amount

    @api.depends('date_order')
    def _compute_due_date(self):
        for order in self:
            if order.date_order:
                order.due_date = fields.Date.from_string(order.date_order) + timedelta(days=7)
            else:
                order.due_date = 3
