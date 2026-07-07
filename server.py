#!/usr/bin/env python3
"""خادم محلي لصفحة تحميل تطبيق الاحصاء الطبي مع أنواع MIME الصحيحة."""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

PORT = 8080
ROOT = Path(__file__).resolve().parent

MIME_TYPES = {
    ".apk": "application/vnd.android.package-archive",
    ".mobileconfig": "application/x-apple-aspen-config",
}


class DownloadHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def guess_type(self, path):
        suffix = Path(path).suffix.lower()
        if suffix in MIME_TYPES:
            return MIME_TYPES[suffix]
        return super().guess_type(path)

    def end_headers(self):
        if self.path.endswith(".apk"):
            self.send_header("Content-Disposition", 'attachment; filename="al-ehsaa-altibbi.apk"')
        elif self.path.endswith(".mobileconfig"):
            self.send_header("Content-Disposition", 'attachment; filename="al-ehsaa-altibbi.mobileconfig"')
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()


def main():
    server = ThreadingHTTPServer(("0.0.0.0", PORT), DownloadHandler)
    print(f"الخادم يعمل على: http://localhost:{PORT}")
    print("لفتح الصفحة من الهاتف، استخدم IP جهازك على نفس الشبكة.")
    print("مثال: http://192.168.1.10:8080")
    print("اضغط Ctrl+C لإيقاف الخادم.")
    server.serve_forever()


if __name__ == "__main__":
    main()
