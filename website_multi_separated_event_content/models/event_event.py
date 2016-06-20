# -*- coding: utf-8 -*-
# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models


class EventEvent(models.Model):

    _name = 'event.event'
    _inherit = ['event.event', 'multi.website.abstract.content']
