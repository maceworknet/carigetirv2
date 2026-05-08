import frappe
from frappe.model.document import Document

class CGCurrentTransaction(Document):
    def validate(self):
        if self.amount <= 0:
            frappe.throw("İşlem tutarı 0'dan büyük olmalıdır.")
            
    def on_submit(self):
        self.update_account_balance()
        
    def on_cancel(self):
        self.update_account_balance(cancel=True)
        
    def update_account_balance(self, cancel=False):
        if not self.current_account:
            return
            
        account = frappe.get_doc("CG Current Account", self.current_account)
        
        # Borç (Debit) = +, Alacak (Credit) = -
        amount = self.amount if not cancel else -self.amount
        
        if self.transaction_type == "Alacak":
            amount = -amount
            
        account.balance = (account.balance or 0.0) + amount
        account.save(ignore_permissions=True)
