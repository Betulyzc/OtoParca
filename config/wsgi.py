"""
WSGI config for config project.

Production-ready WSGI configuration.
Supports environment-based settings (dev / prod).
"""

import os
from django.core.wsgi import get_wsgi_application

# Canlıda DJANGO_SETTINGS_MODULE ortam değişkeni set edilirse onu kullanır.
# Örn: config.settings (tek dosya) veya config.settings.prod gibi.
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    os.getenv("DJANGO_SETTINGS_MODULE", "config.settings")
)

application = get_wsgi_application()
