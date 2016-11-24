# -*- coding: utf-8 -*-
# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class MultiWebsiteAbstractContent(models.AbstractModel):

    _name = 'multi.website.abstract.content'
    _description = 'Multi Website Abstract Content'

    @api.model
    def _multi_mode_recompute(self, args, website_id):
        website_domain = [
            '|',
            ('website_id', '=', website_id),
            ('website_id', '=', False),
        ]
        if args:
            multi_domain = ['&'] + website_domain
            for dom in args:
                multi_domain.append(dom)
        else:
            multi_domain = website_domain
        return multi_domain

    website_id = fields.Many2one(
        comodel_name='website', string='Website')

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        website_id = self.env.context.get('website_id')
        if website_id:
            args = self._multi_mode_recompute(args, website_id)
        res = super(MultiWebsiteAbstractContent, self).search(
            args, offset, limit=limit, order=order, count=count)
        return res
