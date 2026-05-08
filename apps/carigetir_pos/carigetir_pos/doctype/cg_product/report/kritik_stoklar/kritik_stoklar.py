import frappe

def execute(filters=None):
    columns = [
        {'fieldname': 'product', 'label': 'Ürün', 'fieldtype': 'Link', 'options': 'CG Product', 'width': 200},
        {'fieldname': 'stock', 'label': 'Mevcut Stok', 'fieldtype': 'Float', 'width': 120},
        {'fieldname': 'critical', 'label': 'Kritik Seviye', 'fieldtype': 'Float', 'width': 120}
    ]
    data = []
    return columns, data
