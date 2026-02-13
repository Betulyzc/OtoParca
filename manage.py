#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.
Production-ready: settings modülü env ile override edilebilir.
"""
import os
import sys


def main():
    """
    Run administrative tasks.

    Canlıda farklı settings (prod/dev) kullanmak için:
    DJANGO_SETTINGS_MODULE ortam değişkeni set edilirse onu kullanır,
    set edilmemişse varsayılan olarak config.settings kullanır.
    """
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        os.getenv("DJANGO_SETTINGS_MODULE", "config.settings")
    )

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
