import frappe

def get_context(context):
    context.user = frappe.session.user
    context.services = frappe.db.get_list("Services", fields=["title", "image", "description"])
    return context