# CariGetir V2 - Task List

## Immediate Task for Antigravity (Phase 0 & 1 Setup)
1. **Frappe App Structure:** Create modular app structure.
   - Initialize `carigetir_core`.
   - Initialize `carigetir_erp`, `carigetir_pos`, `carigetir_hr` (empty shells for now).
2. **Core DocTypes:** Create foundational DocTypes in `carigetir_core`:
   - `CG Company`
   - `CG Branch`
   - `CG Plan`
   - `CG Feature`
   - `CG Plan Feature`
   - `CG Subscription`
   - `CG Company Feature Override`
3. **Core Helper Functions:** Implement centralized feature checking utilities in `carigetir_core/utils/features.py`.

## MVP Priority List

1. Frappe proje kurulumu
2. carigetir_core app
3. Firma sistemi
4. Paket sistemi
5. Feature sistemi
6. Firma bazlı feature override
7. Kullanıcı/rol sistemi
8. carigetir_erp app
9. Müşteri/cari hesap sistemi
10. Gelir/gider ve tahsilat/ödeme
11. Proforma fatura
12. PDF/print format
13. ERP dashboard
14. POS stok altyapısı
15. POS satış ekranı
16. POS kasa ve fiş
17. Raporlama
18. İK temel modül
19. Abonelik/ödeme
20. Yayına hazırlık

## Scope of First MVP
- **SaaS Core:** Companies, Plans, Features, Overrides.
- **ERP Core:** Customers, Suppliers, Current Accounts, Income/Expense, Collections/Payments, Proforma Invoices (w/ PDF), Statements, Dashboard.
- *(Note: POS and HR will be visible in the menu but marked as inactive/coming soon during the first MVP.)*
