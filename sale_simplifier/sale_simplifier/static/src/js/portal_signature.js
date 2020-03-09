odoo.define('sale_simplifier.signature_form', function (require) {
    "use strict";
    var core = require('web.core');
    var qweb = core.qweb;
    var ajax = require('web.ajax');
    var rpc = require("web.rpc");
    var signature_form = require('portal.signature_form');


    signature_form.SignatureForm.include({
        _loadTemplates: function () {
            console.log("sale_simplifier._loadTemplates");
            return ajax.loadXML('/sale_simplifier/static/src/xml/portal_signature.xml', qweb);
        },
                submitSign: function (ev) {
            ev.preventDefault();

            // extract data
            var self = this;
            var $confirm_btn = self.$el.find('button[type="submit"]');

            // process : display errors, or submit
            var partner_name = self.$("#o_portal_sign_name").val();
            var social_reason = self.$("#o_portal_sign_social_reason").val();
            var legal_representative = self.$("#o_portal_sign_legal_representative").val();
            var type_identifier = self.$("#o_portal_sign_type_identifier:checked").val();
            var identifier = self.$("#o_portal_sign_identifier").val();
            var signature = self.$("#o_portal_signature").jSignature('getData', 'image');
            var is_empty = signature ? this.empty_sign[1] === signature[1] : true;

            this.$('#o_portal_sign_name').parent().toggleClass('o_has_error', !partner_name).find('.form-control, .custom-select').toggleClass('is-invalid', !partner_name);
            this.$('#o_portal_social_reason').parent().toggleClass('o_has_error', !social_reason).find('.form-control, .custom-select').toggleClass('is-invalid', !social_reason);
            this.$('#o_portal_legal_representative').parent().toggleClass('o_has_error', !legal_representative).find('.form-control, .custom-select').toggleClass('is-invalid', !legal_representative);
            this.$('#o_portal_sign_draw').toggleClass('bg-danger text-white', is_empty);
            if (is_empty || ! partner_name) {
                return false;
            }

            $confirm_btn.prepend('<i class="fa fa-spinner fa-spin"></i> ');
            $confirm_btn.attr('disabled', true);
            console.log('submit');
            return rpc.query({
                route: this.options.callUrl,
                params: {
                    'res_id': this.options.resId,
                    'access_token': this.options.accessToken,
                    'partner_name': partner_name,
                    'social_reason': social_reason,
                    'legal_representative': legal_representative,
                    'type_identifier':type_identifier,
                    'identifier':identifier,
                    'signature': signature ? signature[1] : false,
                },
            }).then(function (data) {
                self.$('.fa-spinner').remove();
                if (data.error) {
                    self.$('.o_portal_sign_error_msg').remove();
                    $confirm_btn.before(qweb.render('portal.portal_signature_error', {message: data.error}));
                    $confirm_btn.attr('disabled', false);
                }
                else if (data.success) {
                    $confirm_btn.remove();
                    var $success = qweb.render("portal.portal_signature_success", {widget: data});
                    self.$('#o_portal_sign_draw').parent().replaceWith($success);
                }
                if (data.force_refresh) {
                    if (data.redirect_url) {
                        window.location = data.redirect_url;
                    } else {
                        window.location.reload();
                    }
                }
            });
        },
    });
});