odoo.define('website_dynamic_snippet.website_dynamic_snippet_editor', function(require) {
    'user strict';
    var core = require('web.core');
    var ajax = require('web.ajax');
    var Model = require('web.Model');
    var WebEditorWidget = require('web_editor.widget');
    var Dialog = WebEditorWidget.Dialog;
    var s_options = require('web_editor.snippets.options');
    var base = require('web_editor.base');
    var website = require('website.website');
    var widget = require('web_editor.widget');
    var _t = core._t;
    ajax.loadXML('/website_dynamic_snippet/static/src/xml/website_dynamic_snippet.editor.xml', core.qweb);

var WebsiteDynamicFinderSettingsDialog = Dialog.extend({
        template: 'web_editor.dialog.editor_dialog_website_dynamic_finder_related_settings',
        init: function (parent, options, $editable, media) {
            this.$target = parent;
            this._super(parent, _.extend({}, {
                     title: _t("Filter Settings"),
                 }, options || {}
            ));
        },
        start: function () {
            var self = this;
            self.$snippet_title = self.$("input[id='title-snippet']");
            self.$all_links= self.$("input[id='all-links']");
            self.$limit_input = self.$("input[id='limit']");
            self.$favorite_chk = self.$("input[id='favorite']");
            self.$msg_input = self.$("input[id='empty-list-message']");
            return this._super(this, arguments).then(this.proxy('bind_data'));
        },

        save: function () {
            var self = this;
            self.$target.attr("data-title-snippet", self.$snippet_title.val());
            self.$target.attr("data-all-links", self.$all_links.val());
            self.$target.attr("data-limit", self.$limit_input.val());
            self.$target.attr("data-favorite", self.$favorite_chk.prop('checked'));
            self.$target.attr("data-empty-msg", self.$msg_input.val());
            self.$target.closest("div[data-oe-model='ir.ui.view']").addClass('o_dirty');
            return this._super.apply(this, arguments);
        },

        bind_data: function () {
            var self = this;
            self.$favorite_chk.prop('checked', self.$target.attr('data-favorite') == 'true');
            self.$limit_input.val(self.$target.attr('data-limit') || 2);
            self.$msg_input.val(self.$target.attr("data-empty-msg"));
            self.$snippet_title.val(self.$target.attr("data-title-snippet"));
            self.$all_links.val(self.$target.attr("data-all-links"));
        },
    });

    s_options.registry.website_dynamic_finder_related_snippet = s_options.Class.extend({
        on_prompt: function () {
            var self = this;
            return new WebsiteDynamicFinderSettingsDialog(self.$target, {}).open();
        },
        drop_and_build_snippet: function() {
            var self = this;
            this._super();
            this.on_prompt();
        },
        start : function () {
            var self = this;
            this.$el.find(".js_website_dynamic_finder_related_settings").on("click", _.bind(this.on_prompt, this));
            this._super();
        },
        clean_for_save: function () {
            this.$target.find('.parametricTemplate')
            .empty()
            .append(
                jQuery('<t />')
                    .attr('t-call', this.$target.attr('data-template-id'))
                    .attr('t-ignore-branding', '1')
                    .append(
                        jQuery('<t />')
                            .attr('t-value', "'" + this.$target.attr('data-title-snippet') + "'")
                            .attr('t-set', 'snippet_title')
                            .attr('t-ignore-branding', '1'),
                        jQuery('<t />')
                            .attr('t-value', "'" + this.$target.attr('data-all-links') + "'")
                            .attr('t-set', 'all_links')
                            .attr('t-ignore-branding', '1'),
                        jQuery('<t />')
                            .attr('t-value', this.$target.attr('data-favorite') == 'true' ? 'True': 'False')
                            .attr('t-set', 'favorite')
                            .attr('t-ignore-branding', '1'),
                        jQuery('<t />')
                            .attr('t-value', this.$target.attr('data-limit') || 'None')
                            .attr('t-set', 'limit')
                            .attr('t-ignore-branding', '1'),
                        jQuery('<t />')
                            .attr('t-value', "'" + this.$target.attr('data-model-name') + "'")
                            .attr('t-set', 'model_name')
                            .attr('t-ignore-branding', '1'),
                        jQuery('<t />')
                            .attr('t-value', "'" + this.$target.attr("data-empty-msg") + "'")
                            .attr('t-set', 'empty_msg')
                            .attr('t-ignore-branding', '1')
                    )
            );
        },
    });


});
