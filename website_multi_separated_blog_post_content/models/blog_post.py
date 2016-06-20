# -*- coding: utf-8 -*-
# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models


class BlogPost(models.Model):

    _name = 'blog.post'
    _inherit = ['blog.post', 'multi.website.abstract.content']
