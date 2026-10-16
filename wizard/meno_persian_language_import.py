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
import logging
import os

from odoo import _, fields, models
from odoo.exceptions import UserError
from odoo.tools.misc import ustr
from odoo.tools.translate import TranslationImporter

_logger = logging.getLogger(__name__)


class PersianLanguageImport(models.TransientModel):
    _name = "persian.language.import"
    _description = "Language Importer for Persian (Batch)"

    code = fields.Char(
        string="زبان مقصد (ISO Code)",
        default="fa_IR",
        required=True,
        help="کد استاندارد زبان، برای مثال fa_IR",
    )
    overwrite = fields.Boolean(
        string="بازنویسی ترجمه‌های موجود",
        default=True,
        help="در صورت فعال بودن، ترجمه‌های پیش‌فرض و سفارشی موجود با محتوای این فایل‌ها جایگزین می‌شوند.",
    )
    log_messages = fields.Html(
        string="گزارش عملیات",
        readonly=True,
        default="",
        sanitize=False,
    )

    def _ensure_language_active(self, lang_code):
        """بررسی فعال بودن زبان در سیستم؛ در غیر این صورت فعال‌سازی خودکار آن انجام می‌شود."""
        lang = self.env["res.lang"].search([("code", "=", lang_code)], limit=1)
        if not lang:
            # جستجو در زبان‌های غیرفعال
            lang = self.env["res.lang"].with_context(active_test=False).search([("code", "=", lang_code)], limit=1)
            if lang:
                lang.write({"active": True})
            else:
                raise UserError(
                    _("زبان با کد '%s' در سیستم تعریف نشده است. لطفاً ابتدا از بخش تنظیمات زبان‌ها آن را ایجاد کنید.")
                    % lang_code
                )
        elif not lang.active:
            lang.write({"active": True})

    def import_lang(self):
        self.ensure_one()
        lang_code = self.code.strip()
        self._ensure_language_active(lang_code)

        # ساخت مسیر استاندارد و امن پوشه i18n_po در ریشه ماژول
        current_dir = os.path.dirname(os.path.abspath(__file__))
        i18n_path = os.path.abspath(os.path.join(current_dir, "..", "i18n_po"))

        if not os.path.isdir(i18n_path):
            raise UserError(
                _("پوشه ترجمه‌ها با مسیر مشخص شده یافت نشد:\n%s") % i18n_path
            )

        logs = [f"<p><strong>شروع فرآیند واردسازی ترجمه‌ها برای زبان [{lang_code}]...</strong></p>"]
        file_count = 0

        try:
            translation_importer = TranslationImporter(self.env.cr, verbose=False)

            for subdir, _, files in os.walk(i18n_path):
                for file in files:
                    if file.lower().endswith(".po"):
                        po_file_path = os.path.join(subdir, file)
                        _logger.info("در حال بارگذاری فایل ترجمه: %s", po_file_path)

                        with open(po_file_path, mode="rb") as fileobj:
                            translation_importer.load(fileobj, "po", lang_code)

                        logs.append(f"<p class='text-muted'>✔ بارگذاری موفق: <code>{file}</code></p>")
                        file_count += 1

            if file_count == 0:
                logs.append("<p class='text-warning'>⚠️ هیچ فایل .po در مسیر مورد نظر یافت نشد.</p>")
            else:
                # ذخیره‌سازی تجمیعی در جداول دیتابیس (JSONB)
                translation_importer.save(overwrite=self.overwrite)
                logs.append(
                    f"<p class='text-success'><strong>عملیات با موفقیت پایان یافت. مجموعاً {file_count} فایل وارد گردید.</strong></p>"
                )
                _logger.info("عملیات بارگذاری دسته جمعی ترجمه fa_IR برای %s فایل تکمیل شد.", file_count)

            self.log_messages = "".join(logs)

        except Exception as ex:
            _logger.exception("خطا در پردازش یا بازنویسی فایل‌های ترجمه.")
            raise UserError(
                _(
                    "خطا در واردسازی ترجمه‌ها رخ داد.\n\n"
                    "جزئیات فنی:\n%s"
                )
                % ustr(ex)
            ) from ex

        # حفظ پنجره ویزارد جهت نمایش لاگ نهایی به کاربر
        return {
            "type": "ir.actions.act_window",
            "res_model": self._name,
            "view_mode": "form",
            "res_id": self.id,
            "target": "new",
        }
