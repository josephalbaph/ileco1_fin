from __future__ import unicode_literals

import frappe


def get_context(context):
    # do your magic here
    # context.template = 'ileco1_fin/ileco1_fin/web_form/templates/web_form.html'
    pass


def get_list_context(context):
    context.filters = { 'voucher_legacy': 'Journal Voucher'}


def has_website_permission(doc, ptype, user, verbose=False):
	return True
