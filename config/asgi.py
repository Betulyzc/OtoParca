"""
ASGI config for config project.

Production-ready ASGI configuration.
Supports environment-based settings (dev / prod).
"""

import os
from django.core.asgi import get_asgi_application

# Canlıda DJANGO_SETTINGS_MODULE ortam değişkeni set edilirse onu kullanır.
# Örn: config.settings.prod
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    os.getenv("DJANGO_SETTINGS_MODULE", "config.settings")
)

application = get_asgi_application()
