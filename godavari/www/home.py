import frappe

def get_context(context):
    context.services = frappe.db.get_list("Services", fields=["title", 'url', "image", "description"])
    return context