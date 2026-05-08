frappe.query_reports['Cari Hesap Ekstresi'] = {
    'filters': [
        {
            'fieldname': 'current_account',
            'label': 'Cari Hesap',
            'fieldtype': 'Link',
            'options': 'CG Current Account',
            'reqd': 1
        }
    ]
};
