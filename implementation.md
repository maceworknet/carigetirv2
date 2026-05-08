# CariGetir V2 - Implementation Document

## 1. Development Guidelines
- **Modularity:** Develop each phase separately. Do not mix incomplete phases.
- **Data Isolation:** Every relevant DocType MUST have a `company` field for tenant isolation.
- **Validation:** Write clear validation logic in DocType controllers. Server-side validation is mandatory, especially for financial calculations.
- **Naming Conventions:** Use `CG` prefix for DocTypes. Helper functions should be under `carigetir_core/utils`.
- **No Direct Frappe Apps:** Do NOT use ERPNext, HRMS, or default POS apps. Use custom apps built on Frappe Framework.

## 2. Directory Structure Goal
```text
apps/
  carigetir_core/
    carigetir_core/
      doctype/
      utils/
        company.py
        features.py
        subscription.py
        limits.py
      hooks.py

  carigetir_erp/
  carigetir_pos/
  carigetir_hr/
```

## 3. Development Phases

### Phase 0: Project Setup
- Frappe bench setup, site creation.
- Create `carigetir_core`, `carigetir_erp`, `carigetir_pos`, `carigetir_hr` apps.

### Phase 1: SaaS Core MVP
- DocTypes: CG Company, CG Branch, CG Plan, CG Feature, CG Plan Feature, CG Subscription, CG Company Feature Override, CG System Settings.
- Core functions: `has_feature`, `get_current_company`, `is_subscription_active`, `check_usage_limit`.

### Phase 2: ERP Core MVP
- DocTypes: CG Customer, CG Supplier, CG Current Account, CG Income, CG Expense, CG Payment, CG Collection.
- Functions: Current account balances, basic transactions, ERP dashboard.

### Phase 3: Proforma Invoice MVP
- DocTypes: CG Proforma Invoice, CG Proforma Invoice Item.
- Features: PDF generation, WhatsApp sharing, conversion to sales invoice.

### Phase 4 & 5: POS Core & Sales Screen
- Features: Products, Stock Movement, Barcodes, POS Sales, Cash Registers.
- UI: Dedicated fast sales screen with barcode scanning, offline/cart logic, receipt printing.

### Phase 6: Reporting MVP
- ERP Financial summaries, Current Account balances.
- POS Daily sales, Stock alerts.

### Phase 7: HR MVP
- Employee management, Departments, Leave requests, Attendance.

### Phase 8 & 9 & 10: Advanced & Go-Live
- Subscriptions, Payments, Multi-branch/warehouse, API, Final Testing, Deployment.

## 4. Security Rules
- Restrict data to current company only.
- Deny access to modules/features outside of the subscribed plan.
- Implement soft-deletes (disable) instead of hard-deletes for critical data.
- Maintain audit logs for financial records and transactions.
