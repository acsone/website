# -*- coding: utf-8 -*-
# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class AbstractContent(models.Model):

    _name = 'abstract.content'

    @api.model
    def _multi_mode_recompute(self, domain):
        pass

    website_id = fields.Many2one(
        comodel_name='website', string='Website')

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        if args:
            pass