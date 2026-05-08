import frappe

@frappe.whitelist(allow_guest=True)
def iyzico_webhook():
    # TODO: Implement Iyzico webhook processing logic
    data = frappe.request.get_json()
    # Check signature, update subscription status, log payment
    return {"status": "success"}

@frappe.whitelist(allow_guest=True)
def paytr_webhook():
    # TODO: Implement PayTR webhook processing logic
    data = frappe.request.form
    # Check signature, update subscription status, log payment
    return "OK"
