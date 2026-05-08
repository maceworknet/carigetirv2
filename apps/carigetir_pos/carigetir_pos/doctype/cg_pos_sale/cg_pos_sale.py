import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime

class CGPOSSale(Document):
    def validate(self):
        # Calculate totals
        self.total_amount = sum([item.amount for item in self.items])
        if self.discount > 0:
            self.total_amount -= self.discount
            
    def on_submit(self):
        self.update_stock()
        
    def on_cancel(self):
        self.update_stock(cancel=True)
        
    def update_stock(self, cancel=False):
        for item in self.items:
            product = frappe.get_doc("CG Product", item.product)
            
            qty = item.qty if not cancel else -item.qty
            
            # Sale reduces stock, so we subtract
            product.current_stock = (product.current_stock or 0.0) - qty
            product.save(ignore_permissions=True)
            
            # Create a stock movement record
            movement = frappe.new_doc("CG Stock Movement")
            movement.company = self.company
            movement.product = item.product
            movement.movement_type = "Çıkış" if not cancel else "İade"
            movement.qty = item.qty
            movement.date = now_datetime()
            movement.insert(ignore_permissions=True)
            # Submit the stock movement directly if it's submittable
            # movement.submit() # Uncomment if Stock Movement is a submittable DocType
