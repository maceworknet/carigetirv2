# AGENT.md — CariGetir V2

## Proje Adı

**CariGetir V2**

## Proje Tanımı

CariGetir V2, Frappe Framework kullanılarak geliştirilecek modüler bir SaaS işletme yönetim platformudur.

Platformun amacı; küçük, orta ve büyüyen işletmelere tek panel üzerinden **ERP, POS ve İK** hizmetleri sunmaktır. Sistem paketlere göre modül ve özellik erişimi sağlayacak, ayrıca sistem yöneticisi her firma için paket dışı özel özellik açma/kapatma işlemleri yapabilecektir.

Bu proje Frappe’nin hazır ERPNext, HRMS veya POS uygulamalarını doğrudan kullanmayacaktır. Tüm ERP, POS ve İK modülleri özel olarak geliştirilecektir. Frappe yalnızca framework, panel, DocType, kullanıcı/rol/izin, raporlama, API, print format ve multi-tenant altyapısı olarak kullanılacaktır.

---

## Ana Vizyon

CariGetir V2 şu konumlandırma ile geliştirilecektir:

> Küçük ve orta ölçekli işletmeler için geliştirilen; ERP, POS ve İK modüllerini tek panelde birleştiren, paketlere göre özelleştirilebilir bulut tabanlı işletme yönetim platformu.

Kısa slogan:

> İşletmeni tek panelden yönet.

Alternatif sloganlar:

- Cari, stok, satış ve personel yönetimi tek panelde.
- İşletmen için modüler yönetim sistemi.
- ERP, POS ve İK artık tek platformda.
- Küçük işletmeler için büyük yönetim kolaylığı.
- Paketini seç, modüllerini kullan, işini büyüt.

---

## Temel Ürün Yapısı

CariGetir V2 üç ana ürün modülünden oluşacaktır:

1. **ERP**
2. **POS**
3. **İK**

Bu ürünler paketler aracılığıyla ayrı ayrı veya birlikte satılabilecektir.

Örnek paket kombinasyonları:

- Sadece ERP Paketi
- Sadece POS Paketi
- Sadece İK Paketi
- ERP + POS Paketi
- ERP + İK Paketi
- POS + İK Paketi
- ERP + POS + İK Paketi

---

## Genel SaaS Mantığı

Sistem şu temel mantıkla çalışacaktır:

1. SaaS Super Admin sistemde paketler oluşturur.
2. Her pakete modül ve özellikler atanır.
3. Firma sisteme kaydedilir.
4. Firmaya bir paket atanır.
5. Firma kullanıcıları sadece paketindeki modül ve özellikleri görebilir.
6. Sistem yöneticisi, gerekirse firmaya özel olarak paket dışı özellik açabilir.
7. Sistem yöneticisi, gerekirse pakette bulunan bir özelliği firma özelinde kapatabilir.
8. Kullanıcı erişimi hem paket/özellik kontrolünden hem de rol/yetki kontrolünden geçer.

Yetki kontrol sırası:

```text
Firma aktif mi?
Abonelik aktif mi?
Firma hangi pakete sahip?
Paket hangi modülleri içeriyor?
Paket hangi özellikleri içeriyor?
Firma özelinde açılmış özellik var mı?
Firma özelinde kapatılmış özellik var mı?
Kullanıcının rolü bu işlemi yapmaya yetiyor mu?
```

---

## Frappe Kullanım Yaklaşımı

Bu projede Frappe şu amaçlarla kullanılacaktır:

- Admin panel altyapısı
- DocType tabanlı veri modeli
- Kullanıcı yönetimi
- Rol ve izin sistemi
- Form ve liste ekranları
- Raporlama altyapısı
- Print format sistemi
- REST API altyapısı
- Workflow altyapısı
- Bildirim sistemi
- Multi-tenant veya tek site çok firma mimarisi
- Custom app geliştirme

Frappe’nin hazır uygulamaları kullanılmayacaktır:

- ERPNext doğrudan kullanılmayacak
- HRMS doğrudan kullanılmayacak
- Hazır POS doğrudan kullanılmayacak

Tüm modüller CariGetir markasına özel olarak geliştirilecektir.

---

## Önerilen Frappe App Yapısı

Başlangıçta modüler ve sürdürülebilir bir app yapısı tercih edilmelidir.

```text
frappe-bench/
  apps/
    carigetir_core/
    carigetir_erp/
    carigetir_pos/
    carigetir_hr/
```

### carigetir_core

Ana SaaS yönetim uygulamasıdır.

İçerik:

- Firma yönetimi
- Paket yönetimi
- Abonelik yönetimi
- Özellik yönetimi
- Firma bazlı özellik ayarları
- Kullanıcı limitleri
- Şube limitleri
- Depo limitleri
- Kasa limitleri
- Personel limitleri
- Sistem ayarları
- Ödeme/abonelik altyapısı
- Sistem raporları

### carigetir_erp

CariGetir’in ticari yönetim ve finans modülüdür.

İçerik:

- Cari hesaplar
- Müşteriler
- Tedarikçiler
- Proforma faturalar
- Teklif yönetimi
- Gelirler
- Giderler
- Tahsilatlar
- Ödemeler
- Cari ekstresi
- Finans raporları
- Depo bağlantısı

### carigetir_pos

POS ve perakende satış yönetimi modülüdür.

İçerik:

- Ürün kartları
- Stok kartları
- Barkod sistemi
- Stok hareketleri
- Satış ekranı
- Kasa yönetimi
- Fiş yazdırma
- İade işlemleri
- POS raporları
- Gün sonu işlemleri

### carigetir_hr

İnsan kaynakları modülüdür.

İçerik:

- Personeller
- Departmanlar
- Pozisyonlar
- İzinler
- Puantaj
- Mesai
- Maaş kayıtları
- Personel evrakları
- İK raporları

---

## Multi-Tenant Kararı

Başlangıç için önerilen mimari:

```text
Tek Frappe Site + Çok Firma
```

Bu modelde tüm firmalar tek Frappe sitesinde bulunur. Her kayıtta firma/tenant alanı bulunur. Kullanıcılar sadece kendi firmasına ait verilere erişebilir.

Başlangıç domain yapısı:

```text
app.carigetir.com
```

İleride büyük müşteriler için ayrı tenant/site modeli desteklenebilir:

```text
firma1.carigetir.com
firma2.carigetir.com
```

Başlangıçta tek site çok firma modeli tercih edilmelidir çünkü:

- Geliştirmesi daha hızlıdır.
- Yönetimi daha kolaydır.
- MVP için daha uygundur.
- Sunucu maliyeti daha düşüktür.
- Tek panelden SaaS yönetimi daha basittir.

Ancak her DocType’ta firma izolasyonu zorunlu olmalıdır.

---

## Temel Roller

Sistemde başlangıçta şu roller olacaktır:

```text
SaaS Super Admin
Firma Admini
ERP Yöneticisi
POS Yöneticisi
Kasiyer
İK Yöneticisi
Personel
```

### SaaS Super Admin

Tüm sistemi yönetir.

Yetkileri:

- Tüm firmaları görüntüleme
- Firma oluşturma
- Firma düzenleme
- Firma pasifleştirme
- Paket oluşturma
- Paket düzenleme
- Paket silme/pasifleştirme
- Modül ve özellik yönetimi
- Firma bazlı özellik açma/kapatma
- Kullanıcı limitlerini yönetme
- Abonelikleri yönetme
- Ödeme durumlarını takip etme
- Sistem raporlarını görüntüleme

### Firma Admini

Kendi firmasını yönetir.

Yetkileri:

- Kendi kullanıcılarını oluşturma
- Kendi şubelerini yönetme
- Kendi modüllerini kullanma
- Yetki verilen alanları düzenleme
- Firma ayarlarını düzenleme
- Kendi raporlarını görüntüleme

### ERP Yöneticisi

ERP süreçlerini yönetir.

Yetkileri:

- Cari hesap oluşturma
- Müşteri oluşturma
- Tedarikçi oluşturma
- Proforma fatura oluşturma
- Gelir/gider kaydetme
- Tahsilat/ödeme kaydetme
- Cari ekstresi alma
- ERP raporlarını görme

### POS Yöneticisi

POS ve stok süreçlerini yönetir.

Yetkileri:

- Ürün ekleme
- Stok yönetimi
- Barkod yönetimi
- Satışları görüntüleme
- Kasa raporlarını inceleme
- Kritik stokları takip etme
- Gün sonu raporlarını görme

### Kasiyer

Satış ekranını kullanır.

Yetkileri:

- Barkod okutma
- Satış yapma
- Sepet oluşturma
- Ödeme alma
- Fiş yazdırma
- İade işlemi yapma
- Kendi satışlarını görme

### İK Yöneticisi

Personel süreçlerini yönetir.

Yetkileri:

- Personel ekleme
- Departman yönetimi
- İzinleri yönetme
- Puantaj takibi
- Mesai yönetimi
- Personel raporları

### Personel

Kendi bilgilerini ve izin/personel ekranlarını görür.

Yetkileri:

- Kendi profilini görüntüleme
- İzin talebi oluşturma
- Kendi puantajını görüntüleme
- Kendisine açık belgeleri görme

---

## Paket Sistemi

Her paket şu alanlardan oluşacaktır:

```text
Paket adı
Paket açıklaması
Aylık fiyat
Yıllık fiyat
Dahil olan ürünler
Dahil olan özellikler
Kullanıcı limiti
Şube limiti
Depo limiti
Kasa limiti
Personel limiti
Stok kart limiti
Cari hesap limiti
Proforma fatura limiti
Aktif/pasif durumu
```

### Örnek Paketler

#### POS Başlangıç Paketi

```text
1 şube
1 kasa
2 kullanıcı
500 stok kartı
Stok kart yönetimi
Barkodlu satış
Kasa modülü
Günlük satış raporu
Fiş yazdırma
```

#### ERP Başlangıç Paketi

```text
2 kullanıcı
Cari hesap yönetimi
Müşteri yönetimi
Tedarikçi yönetimi
Gelir/gider takibi
Proforma fatura oluşturma
PDF çıktı alma
Cari ekstresi
```

#### İK Başlangıç Paketi

```text
50 personel limiti
Personel kartları
Departman yönetimi
İzin takibi
Puantaj takibi
Personel raporları
```

#### CariGetir Pro Paketi

```text
ERP + POS
5 kullanıcı
2 şube
3 kasa
2000 stok kartı
Proforma fatura
Satış yönetimi
Stok yönetimi
Kasa yönetimi
Finans raporları
Kar-zarar raporu
```

#### CariGetir Kurumsal Paket

```text
ERP + POS + İK
Sınırsız kullanıcı
Çoklu şube
Çoklu depo
Çoklu kasa
Gelişmiş raporlama
Firma bazlı özel yetkilendirme
Onay akışları
Özel belge şablonları
```

---

## Feature Key Sistemi

Her modül ve özellik sistemde feature key ile tanımlanacaktır.

### ERP Feature Key Örnekleri

```text
erp.customer
erp.supplier
erp.current_account
erp.current_account.statement
erp.proforma
erp.proforma.create
erp.proforma.edit
erp.proforma.delete
erp.proforma.pdf
erp.proforma.convert_to_invoice
erp.proforma.send_email
erp.proforma.send_whatsapp
erp.income
erp.expense
erp.payment
erp.collection
erp.reports
```

### POS Feature Key Örnekleri

```text
pos.product
pos.product.create
pos.stock
pos.stock.movement
pos.barcode
pos.sales
pos.sales.return
pos.cash_register
pos.receipt_print
pos.reports
pos.daily_report
pos.best_selling_report
pos.low_stock_alert
```

### İK Feature Key Örnekleri

```text
hr.employee
hr.department
hr.position
hr.attendance
hr.leave
hr.overtime
hr.payroll
hr.employee_document
hr.reports
```

### Core Feature Key Örnekleri

```text
core.company
core.branch
core.user_management
core.subscription
core.plan
core.feature_override
core.system_reports
```

---

## Başlangıç DocType Listesi

### Core DocType’lar

```text
CG Company
CG Branch
CG Plan
CG Plan Feature
CG Feature
CG Subscription
CG Company Feature Override
CG Company User
CG System Settings
CG Usage Limit
CG Module Access Log
```

### ERP DocType’lar

```text
CG Customer
CG Supplier
CG Current Account
CG Current Transaction
CG Proforma Invoice
CG Proforma Invoice Item
CG Proforma Template
CG Proforma Status Log
CG Income
CG Expense
CG Payment
CG Collection
CG Financial Report
```

### POS DocType’lar

```text
CG Product
CG Product Category
CG Brand
CG Warehouse
CG Stock Movement
CG POS Sale
CG POS Sale Item
CG Cash Register
CG Cash Movement
CG POS Payment
CG POS Return
CG Receipt Print Log
```

### İK DocType’lar

```text
CG Employee
CG Department
CG Position
CG Attendance
CG Leave Request
CG Overtime
CG Payroll Record
CG Employee Document
CG Shift
```

---

# ERP Modülü

ERP modülü CariGetir V2’nin ilk ve ana modülü olacaktır.

## ERP Ana Özellikleri

```text
Cari hesap yönetimi
Müşteri yönetimi
Tedarikçi yönetimi
Proforma fatura yönetimi
Teklif yönetimi
Alış işlemleri
Satış işlemleri
Gelir yönetimi
Gider yönetimi
Tahsilat takibi
Ödeme takibi
Borç/alacak takibi
Cari ekstresi
Depo yönetimi
Finans raporları
```

---

## Proforma Fatura Sistemi

Proforma fatura sistemi ERP modülünün önemli bir parçası olacaktır.

Amaç:

Resmi fatura kesmeden önce müşteriye ön bilgilendirme, teklif veya satış öncesi belge hazırlamak.

Proforma fatura gerçek muhasebe faturası gibi kasa veya vergi kaydı oluşturmayacaktır. Ancak müşteri, ürün/hizmet, tutar, vergi, indirim ve ödeme bilgilerini içeren profesyonel bir belge oluşturacaktır.

### Proforma Fatura Özellikleri

```text
Proforma fatura oluşturma
Müşteri seçme
Ürün veya hizmet ekleme
Miktar belirleme
Birim fiyat girme
KDV oranı seçme
İndirim ekleme
Ara toplam hesaplama
KDV toplamı hesaplama
Genel toplam hesaplama
Para birimi seçme
Geçerlilik tarihi belirleme
Ödeme şartları ekleme
Teslimat şartları ekleme
Açıklama/not ekleme
PDF olarak çıktı alma
E-posta ile paylaşma
WhatsApp ile paylaşma
Proforma durum takibi
Proformayı satışa/faturaya dönüştürme
```

### Proforma Durumları

```text
Taslak
Gönderildi
Onaylandı
Reddedildi
İptal Edildi
Faturaya Dönüştürüldü
```

### Proforma Fatura Alanları

```text
Proforma No
Firma
Müşteri
Düzenleme Tarihi
Geçerlilik Tarihi
Para Birimi
Ürün/Hizmet Kalemleri
Ara Toplam
İndirim
KDV Toplamı
Genel Toplam
Ödeme Şartları
Teslimat Şartları
Açıklama
Durum
Oluşturan Kullanıcı
PDF Çıktısı
```

### Proforma Kalem Alanları

```text
Ürün/Hizmet Adı
Açıklama
Miktar
Birim
Birim Fiyat
İndirim
KDV Oranı
Satır Toplamı
```

### Proforma Akışı

```text
Proforma Oluşturuldu
↓
Müşteriye Gönderildi
↓
Müşteri Onayladı
↓
Satış Kaydına Dönüştürüldü
↓
Gerekirse Resmi Fatura Oluşturuldu
```

---

# POS Modülü

POS modülü perakende satış yapan işletmeler için geliştirilecektir.

## POS Ana Özellikleri

```text
Stok kart yönetimi
Ürün kategori yönetimi
Barkod yönetimi
Satış ekranı
Kasa modülü
Fiş yazdırma
Stoktan otomatik düşme
İade işlemleri
Gün sonu raporu
Kar-zarar takibi
Ciro takibi
En çok satan ürün raporu
Kritik stok uyarısı
```

## POS Temel Akış

```text
Ürün ekle
↓
Barkod tanımla
↓
Stok miktarı gir
↓
Satış ekranında barkod okut
↓
Sepete ürün eklensin
↓
Satış tamamlanınca stok düşsün
↓
Kasa hareketi oluşsun
↓
Fiş yazdırılsın
↓
Raporlara yansısın
```

## Stok Kart Alanları

```text
Ürün adı
Ürün kodu
Barkod numarası
Kategori
Marka
Birim
Alış fiyatı
Satış fiyatı
KDV oranı
Mevcut stok miktarı
Kritik stok miktarı
Depo
Raf/kod bilgisi
Ürün görseli
Aktif/pasif durumu
```

## Stok Hareketleri

Stok artıran işlemler:

```text
Ürün girişi
Satın alma
İade alınması
Manuel stok düzeltme
```

Stok azaltan işlemler:

```text
Satış
Fire
İade çıkışı
Manuel stok düşme
```

Stok hareket kayıt alanları:

```text
Ürün
İşlem türü
Önceki stok
İşlem miktarı
Yeni stok
İşlemi yapan kullanıcı
Tarih/saat
Açıklama
```

## Satış Modülü

Satış ekranında şunlar bulunacaktır:

```text
Barkod okutma alanı
Ürün arama alanı
Sepet listesi
Adet değiştirme
İndirim uygulama
KDV hesaplama
Nakit ödeme
Kart ödeme
Parçalı ödeme
Satışı tamamlama
Fiş yazdırma
Satışı iptal etme
İade işlemi
```

Satış tamamlanınca sistem şunları yapacaktır:

```text
Satış kaydı oluşturur
Satılan ürünleri stoktan düşer
Kasa hareketi oluşturur
Ciroya yansıtır
Kar-zarar hesabına dahil eder
Fiş çıktısı oluşturur
```

## Kasa Modülü

Kasa modülünde şunlar bulunacaktır:

```text
Günlük satış toplamı
Nakit satış toplamı
Kart satış toplamı
Toplam ciro
Toplam maliyet
Tahmini brüt kar
Kasa açılış tutarı
Kasa kapanış tutarı
Kasaya para girişi
Kasadan para çıkışı
Gün sonu raporu
```

## Fiş Yazdırma ve Cihaz Uyumu

İlk aşamada desteklenecek yapı:

```text
Tarayıcı üzerinden fiş çıktısı
58mm termal yazıcı formatı
80mm termal yazıcı formatı
USB barkod okuyucu
Bluetooth barkod okuyucu
Barkod okuyucuyu klavye girişi gibi kullanma
Windows yazıcı sistemi
```

## POS Raporları

```text
Günlük satış raporu
Haftalık satış raporu
Aylık satış raporu
Ürün bazlı satış raporu
En çok satan ürünler
En az satan ürünler
Stok azalan ürünler
Kritik stok raporu
Kategori bazlı satış raporu
Personel bazlı satış raporu
Kasa hareket raporu
Kar-zarar raporu
Ciro raporu
```

---

# İK Modülü

İK modülü firmaların personel süreçlerini yönetmesini sağlayacaktır.

## İK Ana Özellikleri

```text
Personel kartları
Departman yönetimi
Pozisyon yönetimi
İşe giriş tarihi
Maaş bilgisi
İzin hakkı
İzin talepleri
Puantaj takibi
Mesai takibi
Devamsızlık takibi
Personel belge arşivi
Personel raporları
```

## İleri Aşama İK Özellikleri

```text
Vardiya sistemi
QR ile giriş/çıkış
Mobil personel paneli
Bordro hesaplama
Prim sistemi
Performans değerlendirme
Personel görev takibi
```

---

# Arayüz ve Tasarım Yaklaşımı

CariGetir V2 paneli modern, sade ve karmaşık olmayan bir tasarıma sahip olmalıdır.

Tasarım yaklaşımı:

- Shadcn UI hissi veren sade arayüz
- Temiz kart yapıları
- Yumuşak gölgeler
- Modern tablo ekranları
- Kullanıcı dostu form yapıları
- Responsive kullanım
- Mobil uyumlu temel ekranlar
- POS satış ekranında hızlı kullanım
- Gereksiz karmaşadan kaçınma

Frappe Desk varsayılan deneyimi korunabilir fakat özel sayfalarda daha modern arayüzler geliştirilebilir.

Özellikle özel tasarlanması gereken ekranlar:

```text
SaaS Super Admin Dashboard
Firma Dashboard
ERP Dashboard
POS Satış Ekranı
Kasa Dashboard
Proforma Fatura Oluşturma Ekranı
İK Dashboard
```

---

# Geliştirme Fazları

## Faz 0 — Proje Hazırlığı ve Teknik Kurulum

Amaç: Geliştirme ortamını kurmak ve proje omurgasını başlatmak.

Yapılacaklar:

```text
Frappe bench kurulumu
Yeni Frappe site oluşturma
carigetir_core app oluşturma
carigetir_erp app oluşturma
carigetir_pos app oluşturma
carigetir_hr app oluşturma
GitHub reposu oluşturma
Antigravity IDE ile proje klasörünü açma
Kod standartlarını belirleme
Temel branch yapısını oluşturma
```

Çıktılar:

```text
Çalışır Frappe geliştirme ortamı
Boş CariGetir app yapıları
GitHub bağlantısı
İlk commit
```

---

## Faz 1 — SaaS Core MVP

Amaç: Platformun paket, firma ve özellik yönetimi omurgasını kurmak.

Yapılacaklar:

```text
CG Company DocType oluştur
CG Branch DocType oluştur
CG Plan DocType oluştur
CG Feature DocType oluştur
CG Plan Feature DocType oluştur
CG Subscription DocType oluştur
CG Company Feature Override DocType oluştur
CG Company User DocType oluştur
CG System Settings DocType oluştur
Firma aktif/pasif mantığını ekle
Abonelik başlangıç/bitiş mantığını ekle
Paket ve feature eşleştirmesini kur
Firma bazlı özellik aç/kapat mantığını kur
Temel kullanıcı rol yapısını oluştur
```

Geliştirilecek temel fonksiyonlar:

```text
get_current_company()
has_feature(company, feature_key)
is_subscription_active(company)
get_company_plan(company)
get_enabled_features(company)
check_usage_limit(company, limit_key)
```

Çıktılar:

```text
Firma oluşturulabilir
Paket oluşturulabilir
Özellik oluşturulabilir
Paketlere özellik atanabilir
Firmaya paket atanabilir
Firma bazlı özellik override yapılabilir
```

---

## Faz 2 — ERP Core MVP

Amaç: CariGetir’in ana ERP/cari yönetim modülünü oluşturmak.

Yapılacaklar:

```text
CG Customer DocType oluştur
CG Supplier DocType oluştur
CG Current Account DocType oluştur
CG Current Transaction DocType oluştur
CG Income DocType oluştur
CG Expense DocType oluştur
CG Payment DocType oluştur
CG Collection DocType oluştur
Cari hesap bakiyesi hesaplama mantığını kur
Gelir/gider kayıt akışını oluştur
Tahsilat/ödeme kayıt akışını oluştur
Cari ekstresi görünümünü oluştur
ERP Dashboard oluştur
```

Çıktılar:

```text
Müşteri oluşturulabilir
Tedarikçi oluşturulabilir
Cari hesap oluşturulabilir
Gelir/gider kaydı girilebilir
Tahsilat/ödeme girilebilir
Cari bakiyesi görüntülenebilir
Cari ekstresi alınabilir
```

---

## Faz 3 — Proforma Fatura MVP

Amaç: ERP modülüne proforma fatura sistemini eklemek.

Yapılacaklar:

```text
CG Proforma Invoice DocType oluştur
CG Proforma Invoice Item Child Table oluştur
CG Proforma Template DocType oluştur
CG Proforma Status Log DocType oluştur
Proforma numarası otomatik oluştur
Müşteri seçme mantığını kur
Ürün/hizmet kalemi ekleme mantığını kur
Ara toplam hesaplama
İndirim hesaplama
KDV hesaplama
Genel toplam hesaplama
Durum yönetimi ekle
PDF print format oluştur
WhatsApp paylaşım linki oluştur
E-posta gönderim altyapısını hazırla
Proformadan satış/fatura kaydına dönüşüm altyapısını tasarla
```

Çıktılar:

```text
Proforma fatura oluşturulabilir
Kalem eklenebilir
Toplamlar otomatik hesaplanır
Durum takibi yapılabilir
PDF çıktısı alınabilir
WhatsApp ile paylaşılabilir
```

---

## Faz 4 — POS Core MVP

Amaç: POS sisteminin temel stok ve satış altyapısını kurmak.

Yapılacaklar:

```text
CG Product DocType oluştur
CG Product Category DocType oluştur
CG Brand DocType oluştur
CG Warehouse DocType oluştur
CG Stock Movement DocType oluştur
CG Cash Register DocType oluştur
CG Cash Movement DocType oluştur
CG POS Sale DocType oluştur
CG POS Sale Item Child Table oluştur
CG POS Payment DocType oluştur
Stok artırma/azaltma mantığını kur
Barkod ile ürün bulma mantığını kur
Satış sonrası stok düşme mantığını kur
Satış sonrası kasa hareketi oluşturma mantığını kur
```

Çıktılar:

```text
Ürün eklenebilir
Barkod tanımlanabilir
Stok girilebilir
Satış kaydı oluşturulabilir
Satış sonrası stok düşer
Kasa hareketi oluşur
```

---

## Faz 5 — POS Satış Ekranı ve Fiş

Amaç: Gerçek POS kullanım ekranını geliştirmek.

Yapılacaklar:

```text
Özel POS satış ekranı oluştur
Barkod okutma inputu oluştur
Ürün arama alanı oluştur
Sepet mantığını kur
Adet değiştirme
İndirim uygulama
Nakit ödeme
Kart ödeme
Parçalı ödeme
Satışı tamamlama
Satış iptal
İade altyapısı
58mm fiş print formatı
80mm fiş print formatı
Tarayıcıdan yazdırma desteği
```

Çıktılar:

```text
Kasiyer hızlı satış yapabilir
Barkodla ürün sepete eklenir
Ödeme alınabilir
Fiş yazdırılabilir
İade işlemi yapılabilir
```

---

## Faz 6 — Raporlama MVP

Amaç: ERP ve POS için temel raporları oluşturmak.

Yapılacaklar:

```text
ERP finans özeti raporu
Cari bakiye raporu
Gelir/gider raporu
Tahsilat/ödeme raporu
POS günlük satış raporu
Kasa hareket raporu
En çok satan ürünler raporu
Kritik stok raporu
Kar-zarar raporu
Ciro raporu
Firma Dashboard metrikleri
SaaS Super Admin Dashboard metrikleri
```

Çıktılar:

```text
Firma kendi finans ve satış raporlarını görebilir
SaaS Super Admin tüm sistemi genel metriklerle izleyebilir
```

---

## Faz 7 — İK MVP

Amaç: Temel insan kaynakları yönetimini eklemek.

Yapılacaklar:

```text
CG Employee DocType oluştur
CG Department DocType oluştur
CG Position DocType oluştur
CG Attendance DocType oluştur
CG Leave Request DocType oluştur
CG Overtime DocType oluştur
CG Payroll Record DocType oluştur
CG Employee Document DocType oluştur
Personel kartı oluşturma
İzin talebi oluşturma
İzin onay/reddetme
Puantaj girişi
Mesai kaydı
İK Dashboard
```

Çıktılar:

```text
Personel eklenebilir
Departman ve pozisyon atanabilir
İzin yönetimi yapılabilir
Puantaj tutulabilir
Mesai girilebilir
```

---

## Faz 8 — Abonelik, Ödeme ve Ticari Sistem

Amaç: SaaS gelir modelini aktif hale getirmek.

Yapılacaklar:

```text
Abonelik yenileme mantığı
Süresi biten firmaları kısıtlama
Manuel ödeme onayı
Ödeme geçmişi
Paket yükseltme
Paket düşürme
Kullanım limiti aşımı uyarıları
İyzico entegrasyon hazırlığı
PayTR entegrasyon hazırlığı
Fatura/ödeme bildirimleri
```

Çıktılar:

```text
Firmalar paketlere göre yönetilir
Abonelik süreleri takip edilir
Ödeme durumları izlenir
Paket yükseltme/düşürme yapılabilir
```

---

## Faz 9 — Gelişmiş Özellikler

Amaç: Platformu daha güçlü ve pazarlanabilir hale getirmek.

Yapılacaklar:

```text
Çoklu şube desteği
Çoklu depo desteği
Çoklu kasa desteği
Firma bazlı özel tema
Özel belge şablonları
Gelişmiş onay akışları
API erişimi
Mobil uyumlu özel ekranlar
Bildirim sistemi
Stok azalma uyarıları
Proforma onay akışı
QR/personel giriş çıkış altyapısı
Dış entegrasyon altyapısı
```

Çıktılar:

```text
Platform kurumsal müşterilere daha uygun hale gelir
Özelleştirilebilir SaaS yapısı güçlenir
```

---

## Faz 10 — Yayına Hazırlık

Amaç: CariGetir V2’yi gerçek müşteri kullanımına hazır hale getirmek.

Yapılacaklar:

```text
Test verileri oluştur
Yetki testleri yap
Firma veri izolasyonu testleri yap
Paket/feature testleri yap
POS satış senaryosu testleri yap
Proforma senaryosu testleri yap
Cari bakiye testleri yap
Performans testleri yap
Yedekleme planı oluştur
Sunucu deployment hazırlığı yap
Domain ve SSL yapılandırması
Hata loglama ve izleme
Kullanıcı dokümantasyonu
Tanıtım landing page hazırlığı
```

Çıktılar:

```text
Müşteriye sunulabilir CariGetir V2 beta sürümü
Canlı sunucu kurulumu
Temel kullanım dokümanı
```

---

# Antigravity IDE İçin Çalışma Kuralları

Bu projede Antigravity IDE kullanılacaktır. Agent aşağıdaki kurallara göre çalışmalıdır.

## Genel Kurallar

1. Her faz ayrı ayrı geliştirilmelidir.
2. Bir faz bitmeden sonraki faza geçilmemelidir.
3. Önce DocType yapıları oluşturulmalı, sonra iş mantığı yazılmalıdır.
4. Paket ve feature kontrolü en baştan uygulanmalıdır.
5. Her DocType’ta firma/tenant izolasyonu düşünülmelidir.
6. Gereksiz karmaşık yapılar MVP’ye eklenmemelidir.
7. Kodlar modüler, okunabilir ve sürdürülebilir olmalıdır.
8. Frappe’nin standart yapısı bozulmamalıdır.
9. Hazır ERPNext/HRMS/POS modülleri kullanılmamalıdır.
10. Geliştirilen her özellik test edilmelidir.

## Kodlama Kuralları

- Python tarafında Frappe standartlarına uy.
- DocType controller dosyalarında validation mantığını net tut.
- Ortak helper fonksiyonları `carigetir_core/utils` altında topla.
- Feature kontrol fonksiyonlarını merkezi tut.
- Aynı kodu farklı modüllerde tekrar etme.
- İsimlendirmelerde `CG` prefix kullanımını koru.
- Her önemli işlem için kullanıcı ve tarih bilgisi kaydet.
- Kritik işlemlerde log oluştur.
- Finansal hesaplamalarda otomatik toplamları server-side doğrula.
- Client-side hesaplama yapılsa bile backend doğrulaması yap.
- Yetki kontrolünü sadece frontend’e bırakma.
- Her veri kaydında firma alanı zorunlu olsun.

## Güvenlik Kuralları

- Kullanıcı sadece kendi firmasının verisini görmelidir.
- Firma izolasyonu ihlal edilmemelidir.
- Paket dışı özelliklere erişim engellenmelidir.
- Rolü olmayan kullanıcı işlem yapamamalıdır.
- Aboneliği pasif firmaların kritik işlemleri kısıtlanmalıdır.
- Silme işlemlerinde mümkünse hard delete yerine pasifleştirme tercih edilmelidir.
- Finansal kayıtlar düzenlenirken log tutulmalıdır.
- Satış, ödeme, tahsilat gibi işlemler izlenebilir olmalıdır.

## UI/UX Kuralları

- Arayüz sade ve hızlı olmalıdır.
- POS ekranı kasiyer kullanımına uygun olmalıdır.
- Formlarda gereksiz alanlar gösterilmemelidir.
- Dashboardlar kart yapısıyla özet bilgi vermelidir.
- Kritik işlemlerde onay modalı kullanılmalıdır.
- Rapor ekranlarında tarih filtresi bulunmalıdır.
- Mobil kullanım göz önünde bulundurulmalıdır.
- Tasarımda modern, sade, shadcn benzeri bir his hedeflenmelidir.

---

# MVP Öncelik Sırası

En doğru ilk geliştirme sırası:

```text
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
```

---

# İlk MVP Kapsamı

İlk MVP şu kapsamda tutulmalıdır:

```text
SaaS Core
Firma Yönetimi
Paket Yönetimi
Feature Yönetimi
Firma Bazlı Özellik Aç/Kapat
ERP Core
Müşteri Yönetimi
Tedarikçi Yönetimi
Cari Hesap
Gelir/Gider
Tahsilat/Ödeme
Proforma Fatura
PDF Çıktı
Cari Ekstresi
Temel ERP Dashboard
```

İlk MVP’de POS ve İK menüde pasif/yakında olarak gösterilebilir.

---

# Antigravity İçin İlk Görev

Agent ilk olarak şu işi yapmalıdır:

```text
Frappe Framework üzerinde CariGetir V2 için modüler app yapısını kur.
Önce carigetir_core uygulamasını oluştur.
Firma, Paket, Feature, Abonelik ve Firma Feature Override DocType yapılarını oluştur.
Feature kontrolü için merkezi helper fonksiyonlarını hazırla.
ERP, POS ve İK app klasörlerini sonraki fazlar için boş şekilde hazırla.
```

---

# İlk Teknik Dosya Yapısı Hedefi

```text
apps/
  carigetir_core/
    carigetir_core/
      doctype/
        cg_company/
        cg_branch/
        cg_plan/
        cg_feature/
        cg_plan_feature/
        cg_subscription/
        cg_company_feature_override/
        cg_company_user/
        cg_system_settings/
      utils/
        company.py
        features.py
        subscription.py
        limits.py
      hooks.py

  carigetir_erp/
    carigetir_erp/
      doctype/

  carigetir_pos/
    carigetir_pos/
      doctype/

  carigetir_hr/
    carigetir_hr/
      doctype/
```

---

# Önemli Notlar

- CariGetir V2, mevcut carigetir.com sisteminin yeni nesil versiyonu olarak geliştirilecektir.
- Eski sistem birebir kopyalanmayacaktır; yeni mimari daha modüler ve SaaS odaklı olacaktır.
- Sistem başlangıçta sade tutulmalı, ancak ileride büyümeye uygun tasarlanmalıdır.
- Özellik sistemi en baştan doğru kurulmalıdır.
- Tüm modüllerde firma bazlı veri izolasyonu temel prensip olmalıdır.
- POS, ERP ve İK modülleri birbirine bağlanabilir ama bağımsız paketlenebilir olmalıdır.
- Proforma fatura sistemi ERP MVP içinde öncelikli geliştirilmelidir.
- Frappe hazır uygulamaları değil, özel CariGetir app’leri kullanılmalıdır.
