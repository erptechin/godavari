import frappe

def get_context(context):
    context.user = frappe.session.user
    # context.pages = frappe.db.get_list('Custom Pages', fields=['page_name', 'page_url', 'page_contains'])
    return context