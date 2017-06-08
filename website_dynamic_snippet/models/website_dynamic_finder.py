# -*- coding: utf-8 -*-
# © 2015-2017 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models


class WebsiteDynamicFinder(models.AbstractModel):
    _name = 'website.dynamic.finder'

    _max_items = 20

    is_favorite = fields.Boolean('Website Favorite')

    def _get_domain(self, is_favorite=None, **kwargs):
        """
        Method used to be overwrite in order to get a specific domain
        depending of the given **kwargs
        :rparam: specific domain
        :rtype: empty list or list of tuples
        """
        domain = []
        if is_favorite:
            domain = [('is_favorite','=', is_favorite)]
        return domain

    @api.model
    def get_datas(self, is_favorite=None, nbr_items=None, **kwargs):
        """
        Method userd to be overwrite in order to get a specic record set
        returned.
        :rparam: specific record set
        :rtype: recordset
        """
        domain = self._get_domain(is_favorite=is_favorite)
        nbr_items = nbr_items or self._max_items
        return self.search(domain, limit=nbr_items)
