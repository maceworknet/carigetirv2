import frappe

def execute(filters=None):
    columns = [
        {'fieldname': 'date', 'label': 'Tarih', 'fieldtype': 'Date', 'width': 120},
        {'fieldname': 'type', 'label': 'İşlem Yönü', 'fieldtype': 'Data', 'width': 100},
        {'fieldname': 'amount', 'label': 'Tutar', 'fieldtype': 'Currency', 'width': 120}
    ]
    data = []
    return columns, data
