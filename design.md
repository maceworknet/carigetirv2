# CariGetir V2 - System Design Document

## 1. Project Overview
- **Project Name:** CariGetir V2
- **Vision:** A modular SaaS business management platform integrating ERP, POS, and HR for small and medium-sized enterprises.
- **Slogan:** İşletmeni tek panelden yönet.

## 2. Core Architecture
- **Framework:** Frappe Framework
- **Approach:** Custom modules for ERP, POS, and HR. Ready-made Frappe apps (ERPNext, HRMS) will NOT be used.
- **Multi-Tenant Architecture:** Single Site + Multi Company. Every DocType must include a company/tenant field for strict data isolation.

## 3. Module Structure
### `carigetir_core` (SaaS Management)
- **Features:** Company management, plans, subscriptions, feature control, feature overrides, user limits.

### `carigetir_erp` (Finance & Commercial)
- **Features:** Current accounts, customers, suppliers, proforma invoices, income, expense, collections, payments, finance reports.
- **Proforma Invoices:** Key focus. Allows PDF generation, WhatsApp/Email sharing, and conversion to actual invoices.

### `carigetir_pos` (Retail & POS)
- **Features:** Products, stock tracking, barcode management, sales screen, cash register, receipt printing.

### `carigetir_hr` (Human Resources)
- **Features:** Employees, departments, attendance, leaves, overtime, payroll.

## 4. Authorization & Roles
- **System Check Order:** Company Active? -> Subscription Active? -> Plan Modules/Features -> Feature Overrides -> User Role.
- **Roles:** SaaS Super Admin, Firma Admini, ERP Yöneticisi, POS Yöneticisi, Kasiyer, İK Yöneticisi, Personel.

## 5. UI / UX Design Approach
- **Style:** Modern, minimal, "shadcn UI" feel. Soft shadows, clean cards, modern tables.
- **Focus:** Fast usage for POS, responsive/mobile-friendly for key screens, specialized dashboards.

## 6. DocType Definitions
- Prefix `CG` is used for all custom DocTypes.
- **Core:** CG Company, CG Plan, CG Feature, CG Subscription, etc.
- **ERP:** CG Customer, CG Supplier, CG Current Account, CG Proforma Invoice, etc.
- **POS:** CG Product, CG POS Sale, CG Stock Movement, CG Cash Register, etc.
- **HR:** CG Employee, CG Attendance, CG Leave Request, etc.
