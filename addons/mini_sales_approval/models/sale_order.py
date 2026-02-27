from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    approval_count = fields.Integer(compute='_compute_approval_count')

    def _compute_approval_count(self):
        for order in self:
            order.approval_count = self.env['sale.approval.request'].search_count([('sale_order_id', '=', order.id)])

    def action_confirm(self):
        # Agar contextda skip_approval bo'lsa (menejer tasdiqlaganidan keyin)
        if self.env.context.get('skip_approval'):
            return super(SaleOrder, self).action_confirm()

        for order in self:
            if order.amount_total > 10000:
                approval = self.env['sale.approval.request'].search([
                    ('sale_order_id', '=', order.id),
                    ('state', '=', 'approved')
                ])
                if not approval:
                    # Yangi request yaratish
                    self.env['sale.approval.request'].create({
                        'sale_order_id': order.id,
                        'state': 'submitted'
                    })
                    raise UserError(_("Sotuv summasi 10,000 dan yuqori. Tasdiqlash so'rovi yuborildi. Menejer tasdiqlashini kuting."))
        
        return super(SaleOrder, self).action_confirm()

    def action_view_approvals(self):
        return {
            'name': _('Approvals'),
            'type': 'ir.actions.act_window',
            'res_model': 'sale.approval.request',
            'view_mode': 'tree,form',
            'domain': [('sale_order_id', '=', self.id)],
            'context': {'default_sale_order_id': self.id}
        }