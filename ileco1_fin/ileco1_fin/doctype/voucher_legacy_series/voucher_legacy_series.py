# -*- coding: utf-8 -*-
# Copyright (c) 2020, Joseph Marie M. Alba and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cint
from frappe.model.document import Document


class VoucherLegacySeries(Document):
    pass


@frappe.whitelist()
def get_voucher_legacy_series(key, digits=8):
    current = frappe.db.sql(
        "SELECT `current`, `prefix` FROM `tabVoucher Legacy Series` WHERE `name`=%s FOR UPDATE", (key,))
    if current and current[0][0] is not None:
        new_current = current[0][0]
        prefix = current[0][1]
        # yes, update it
        frappe.db.sql(
            "UPDATE `tabVoucher Legacy Series` SET `current` = `current` + 1 WHERE `name`=%s", (key,))
        new_current = cint(new_current) + 1
        voucher_no = '{0}-{1}'.format(prefix,
                                      ('%0' + str(digits) + 'd') % new_current)
        return voucher_no
    return None
