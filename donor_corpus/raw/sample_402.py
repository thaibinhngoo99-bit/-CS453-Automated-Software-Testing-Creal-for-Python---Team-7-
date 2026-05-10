from __future__ import unicode_literals
import frappe

def set_default_address(doc,method):
	if doc.is_primary_address:
		for row in doc.links:
			if row.link_doctype=="Customer":
				cust = frappe.get_doc("Customer",row.link_name)
				cust.default_address=doc.name
				cust.save()

def set_default_contact(doc,method):
	if doc.is_primary_contact:
		for row in doc.links:
			if row.link_doctype=="Customer":
				cust = frappe.get_doc("Customer",row.link_name)
				cust.default_contact_person=doc.name
				cust.save()