## MeNo Persian Translator – Odoo 19

---
```text
  __  __         _   _        ____         __  _  
 |  \/  |  ___  | \ | |  ___ / ___|  ___  / _|| |_  
 | |\/| | / _ \ |  \| | / _ \\___ \ / _ \| |_ | __|  
 | |  | ||  __/ | |\  || (_) |___) | (_) |  _|| |_  
 |_|  |_| \___| |_| \_| \___/|____/ \___/|_|   \__|
-------------------------------------------------------
Developer: MeNoSoft
Website: https://menosoft.ir
Project: MeNo Persian Translator for Odoo 19
Part of MeNoSoft. See LICENSE file for full copyright and licensing details.
-------------------------------------------------------
```
---

<div align="center">
  
![MeNoSoft Logo](https://menosoft.ir/logo.png)

### ماژول بارگذاری و همگام‌سازی دسته‌جمعی ترجمه فارسی مِنو ۱۹
### MeNo Persian Translator for Odoo 19

[![Odoo Version](https://img.shields.io/badge/Odoo-19.0-blue.svg)](https://www.odoo.com)
[![License](https://img.shields.io/badge/License-AGPL--3-green.svg)](LICENSE)
[![Development](https://img.shields.io/badge/Developer-MeNoSoft-orange.svg)](https://menosoft.ir)

</div>

## 📋 معرفی | Introduction

**MeNo Persian Translator** یک ابزار حرفه‌ای، سریع و زیرساختی جهت بارگذاری و همگام‌سازی دسته‌جمعی پکیج‌های ترجمه فارسی (`fa_IR`) در مِنو ۱۹ است. این ماژول توسط تیم **MeNoSoft** توسعه یافته و با تکیه بر معماری ذخیره‌سازی ترجمه در مِنو مدرن (ستون‌های JSONB)، فایل‌های `.po` موجود در ماژول را با دقت و سرعت بالا در پایگاه‌داده ایمپورت و اعمال می‌کند.

**MeNo Persian Translator** is a professional and high-performance translation importer designed for Odoo 19. Developed by the **MeNoSoft** team, this module facilitates batch loading and synchronization of Persian (`fa_IR`) `.po` translation files, fully compliant with modern Odoo JSONB translation architecture.

## ✨ ویژگی‌ها | Features

- ⚡ **بارگذاری دسته‌جمعی و سریع** - پردازش یکپارچه و بهینه فایل‌های `.po` بدون ایجاد سربار روی پایگاه‌داده
- 🔄 **سازگار با ساختار مدرن مِنو ۱۹** - تطابق کامل با معماری فیلدهای ترجمه‌پذیر JSONB
- 🛡️ **فعال‌سازی هوشمند زبان** - بررسی و فعال‌سازی خودکار زبان `fa_IR` در دیتابیس در صورت غیرفعال بودن
- 📝 **سیستم گزارش‌دهی داخلی** - نمایش شفاف لاگ فایل‌های بارگذاری‌شده در پنجره ویزارد
- 🔒 **امنیت در سطح سازمانی** - محدودسازی دسترسی اجرا تنها به مدیران ارشد سیستم (`Settings / Administrator`)
- ⚙️ **کنترل بازنویسی (Overwrite)** - قابلیت بازنویسی یا حفظ عبارات و ترجمه‌های سفارشی گذشته

## 📦 ماژول‌های وابسته | Dependencies

- `base` - ماژول پایه و هسته سیستم مِنو

## 🚀 نصب و راه‌اندازی | Installation

۱. ماژول را در دایرکتوری ماژول‌های سفارشی (`custom_addons`) سرور مِنو قرار دهید:
bash
# Normally installation path
/custom_addons/meno_persian_translator/
۲. فایل‌های ترجمه استاندارد خود را درون پوشه `i18n_po` قرار دهید.
۳. سرور مِنو را ریستارت کنید:
bash
sudo systemctl restart odoo
۴. با حساب کاربری مدیر سیستم وارد شده، حالت توسعه‌دهنده (Developer Mode) را فعال کرده و از منوی **Apps** گزینه **Update Apps List** را بزنید.
۵. عبارت **MeNo Persian Translator for Odoo** را جستجو و بر روی **Activate** کلیک کنید.

## ⚙️ نحوه استفاده و پیکربندی | Usage & Configuration

پس از نصب، جهت اجرای عملیات واردسازی دسته‌جمعی مراحل زیر را دنبال کنید:

۱. به منوی **تنظیمات (Settings) ← ترجمه‌ها (Translations) ← واردسازی فایل‌های ترجمه فارسی** بروید.  
۲. در پنجره بازشده:
   - کد زبان مقصد را بررسی فرمایید (پیش‌فرض: `fa_IR`).
   - در صورت نیاز به جایگزینی تمام عبارات پیشین، تیک **بازنویسی ترجمه‌های موجود** را فعال نگه‌دارید.
۳. بر روی دکمه **شروع بارگذاری** کلیک کنید.  
۴. پس از اتمام پردازش، گزارش موفقیت‌آمیز بودن بارگذاری فایل‌ها در تب **گزارش عملیات** نمایش داده خواهد شد.

## 👨‍💻 توسعه‌دهنده | Developer

<div align="center">
  
**MeNoSoft** - راهکارهای نرم‌افزاری نوین

[![Website](https://img.shields.io/badge/Website-menosoft.ir-blue)](https://menosoft.ir)
[![Email](https://img.shields.io/badge/Email-info@menosoft.ir-red)](mailto:info@menosoft.ir)

</div>

## 📄 لایسنس | License

این ماژول تحت لیسانس **AGPL-3** منتشر شده است. برای اطلاعات بیشتر فایل [LICENSE](LICENSE) را مطالعه فرمایید.

This module is published under the **AGPL-3** license. For more information, please read the [LICENSE](LICENSE) file.

## 🤝 پشتیبانی | Support

برای دریافت پشتیبانی فنی، گزارش باگ یا سفارش توسعه ماژول‌های سفارشی می‌توانید از راه‌های زیر با ما در ارتباط باشید:

- **وبسایت**: [https://menosoft.ir](https://menosoft.ir)
- **ایمیل**: info@menosoft.ir
- **تلفن**: <span dir="ltr">021-9130-7531</span>
- **موبایل**: <span dir="ltr">093-5521-7531</span>
---

<div align="center">
  
**Copyright © 2026 MeNoSoft. All rights reserved.**

</div>
