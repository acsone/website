# -*- coding: utf-8 -*-
# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class Website(models.Model):

    _inherit = 'website'

    public_name = fields.Char()

    @api.multi
    def name_get(self):
        """
        Use public_name as name_get in order to be more user friendly
        """
        result = []
        for w in self:
            result.append((w.id, w.public_name or w.name))
        return result
