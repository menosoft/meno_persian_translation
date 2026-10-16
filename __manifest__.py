# -*- coding: utf-8 -*-
#
#  __  __         _   _        ____         __  _
# |  \/  |  ___  | \ | |  ___ / ___|  ___  / _|| |_
# | |\/| | / _ \ |  \| | / _ \\___ \ / _ \| |_ | __|
# | |  | ||  __/ | |\  || (_) |___) | (_) |  _|| |_
# |_|  |_| \___| |_| \_| \___/|____/ \___/|_|   \__|
#
# -------------------------------------------------------
# Developer: MeNoSoft
# Website: https://menosoft.ir
# Project: MeNo Persian Translator for Odoo 
# Part of MeNoSoft. See LICENSE file for full copyright and licensing details.
# -------------------------------------------------------
#

{
    "name": "MeNo Persian Translator for Odoo",
    "summary": "بارگذاری و همگام‌سازی دسته‌جمعی فایل‌های ترجمه فارسی در مِنو 19",
    "description": """
        ماژول اختصاصی جهت بارگذاری خودکار و بهینه‌سازی فایل‌های ترجمه فارسی (.po)
        برای بخش‌های مختلف ERP مِنو نسخه 19 با معماری فیلدهای JSONB و بازنویسی استاندارد.
    """,
    "author": "MeNoSoft Team",
    "website": "https://menosoft.ir",
    "category": "Internationalization",
    "version": "19.0.1.0.0",
    "license": "AGPL-3",
    "depends": [
        "base",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizard/meno_persian_language_import_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}

