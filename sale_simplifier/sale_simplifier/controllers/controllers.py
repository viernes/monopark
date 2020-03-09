from odoo import fields, http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.portal.controllers.mail import _message_post_helper
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager


class CustomerPortal(CustomerPortal):

    @http.route(['/my/orders/<int:order_id>/accept'], type='json', auth="public", website=True)
    def portal_quote_accept(
            self, res_id, access_token=None,
            partner_name=None,
            social_reason=None,
            legal_representative=None,
            type_identifier=None,
            identifier=None,
            signature=None, order_id=None
    ):
        try:
            order_sudo = self._document_check_access('sale.order', res_id, access_token=access_token)
        except (AccessError, MissingError):
            return {'error': _('Invalid order')}

        if not order_sudo.has_to_be_signed():
            return {'error': _('Order is not in a state requiring customer signature.')}
        if not signature:
            return {'error': _('Signature is missing.')}

        if not order_sudo.has_to_be_paid():
            order_sudo.action_confirm()

        order_sudo.signature = signature
        order_sudo.signed_by = partner_name
        dict_partner = {}
        dict_contact = {}

        order_sudo.partner_id.type_document != type_identifier \
            and dict_contact.update({'type_document': type_identifier})
        order_sudo.partner_id.identifier != identifier \
            and dict_contact.update({'identifier': identifier})
        dict_contact and order_sudo.partner_id.write(dict_contact)

        parent_id = order_sudo.partner_id.parent_id
        if parent_id:
            parent_id.social_razn != social_reason \
                and dict_partner.update({'social_razn': social_reason})
            parent_id.legal_representative != legal_representative and \
                dict_partner.update({'legal_representative': legal_representative})
            dict_partner and parent_id.write(dict_partner)
        else:
            order_sudo.partner_id.social_razn != social_reason and \
                dict_partner.update({'social_razn': social_reason})
            order_sudo.partner_id.legal_representative != legal_representative and \
                dict_partner.update({'legal_representative': legal_representative})
            dict_partner and parent_id.write(dict_partner)
        pdf = request.env.ref('sale.action_report_saleorder').sudo().render_qweb_pdf([order_sudo.id])[0]
        _message_post_helper(
            res_model='sale.order',
            res_id=order_sudo.id,
            message=_('Order signed by %s') % (partner_name,),
            attachments=[('%s.pdf' % order_sudo.name, pdf)],
            **({'token': access_token} if access_token else {}))

        return {
            'force_refresh': True,
            'redirect_url': order_sudo.get_portal_url(query_string='&message=sign_ok'),
        }
