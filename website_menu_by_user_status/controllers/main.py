# -*- coding: utf-8 -*-
# Copyright 2017 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import http
from odoo.http import request

from odoo.addons.web.controllers.main import Home


class Website(Home):

    def _get_page_access(self, url):
        # compose access page url
        base_url = u'/page/'
        base_url += url

        # check Public user or Logged user
        if request.env.user == request.website.user_id:
            return request.env['website.menu'].sudo().search(
                [('user_not_logged', '=', True), ('url', '=', base_url)])
        else:
            return request.env['website.menu'].sudo().search(
                [('user_logged', '=', True), ('url', '=', base_url)])

    @http.route('/', type='http', auth="public", website=True)
    def index(self, **kw):
        # Do not return 404 for odoo backend menu
        main_menu = request.env.ref('website.main_menu',
                                    raise_if_not_found=False)
        if not main_menu:
            url = request.httprequest.referrer.split('/')[-1]
            to_display = self._get_page_access(url)
            if not len(to_display) > 0:
                return request.render('website.404')
        return super(Website, self).index(**kw)

    @http.route('/page/<page:page>', type='http', auth="public", website=True,
                cache=300)
    def page(self, page, **opt):
        to_display = self._get_page_access(page)
        if len(to_display) > 0:
            return super(Website, self).page(page, **opt)
        return request.render('website.404')
