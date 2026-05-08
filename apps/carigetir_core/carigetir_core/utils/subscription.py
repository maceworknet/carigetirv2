import frappe
from frappe.utils import today

def check_expired_subscriptions():
    """
    Daily scheduled job to check and expire subscriptions
    """
    expired_subs = frappe.get_all(
        "CG Subscription",
        filters={"status": "Active", "end_date": ("<", today())},
        pluck="name"
    )
    
    for sub_name in expired_subs:
        frappe.db.set_value("CG Subscription", sub_name, "status", "Expired")
        
    if expired_subs:
        frappe.db.commit()
