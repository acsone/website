.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :alt: License: AGPL-3

Website Dynamic Snippet
=======================

This module allows to implement dynamic snippet based on a backend's model

Configuration
=============

To implement your dynamic snippet you have to:

* Add a dependency into your custom module from "website_dynamic_snippet" and the module that adds the model you want
to show into the website. Here we can take "event" for exemple.
* You have to create your snippet as all other snippet. Into the tag "<section>" you have to add those properties too:
** class="website_dynamic_finder_related_entry oe_snippet_body"
** data-model-name='blog.post'
** data-template-id='website_blog_dynamic_snippet.blog_post_snippet_list'> with the last one taht is the template that will be dynamiccaly called 
* Once the templating is over you have to make an inherit from the backend's model to 'website.dynamic.snippet' that is define here as an Abstract model
     _name = "event.event"
     _inherit = ['event.event', 'website.dynamic.finder']
** If you want to extend the behavior of the research you can also overwrite the defined method "get_datas" or "get_domain". By default it also add a is_favorite field used
to create a priority onto the dynamic content shown into the frontend.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/website/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback
`here <https://github.com/OCA/website/issues/new?body=module:%20website_dynamic_snippet%0Aversion:%208.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.


Credits
=======

Contributors
------------

* Laurent Mignon <laurent.mignon@acsone.eu>
* Jonathan Nemry <jonathan.nemry@acsone.eu>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.
