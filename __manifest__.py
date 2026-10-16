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
    "summary": "Automated batch loading and synchronization of Persian (fa_IR) translation files in Odoo 19",
    "description": """
MeNo Persian Translator for Odoo 19
===================================
A high-performance enterprise utility designed to automate the batch loading,
synchronization, and deployment of Persian (fa_IR) PO translation files across Odoo 19 apps.

Key Features & Capabilities:
----------------------------
* Automated batch import of PO translation files from local module paths.
* Native compatibility with Odoo 19 JSONB translatable field architecture.
* Automatic verification and activation of the Persian (fa_IR) language pack.
* Configurable overwrite options (safeguard custom strings or reset to base translation).
* Optimized memory footprint and batch operations to avoid server timeouts.
* Enterprise-grade security: restricted strictly to System Administrators (Settings).
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
