frappe.pages['cg-pos-screen'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'CariGetir POS',
        single_column: true
    });
    $(frappe.render_template('cg_pos_screen', {})).appendTo(page.main);
}
