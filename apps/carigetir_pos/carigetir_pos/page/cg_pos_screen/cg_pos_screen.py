import frappe

@frappe.whitelist()
def get_pos_data():
    return 'success'
