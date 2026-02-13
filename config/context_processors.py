from django.conf import settings


def business_info(request):
    """
    Production-ready context processor.

    - Sabit bilgiler settings.py üzerinden override edilebilir.
    - SITE_URL zorunlu olarak settings’ten gelir.
    - WhatsApp formatı başında + olmadan gönderilir.
    """

    return {
        "BUSINESS_NAME": getattr(settings, "BUSINESS_NAME", "Umay Oto Yedek Parça"),
        "BUSINESS_ADDRESS": getattr(settings, "BUSINESS_ADDRESS", "Darıca, Kocaeli"),
        "BUSINESS_PHONE": getattr(settings, "BUSINESS_PHONE", "+905331432357"),
        "BUSINESS_OWNER": getattr(settings, "BUSINESS_OWNER", "Yahya Yılmaz"),
        "BUSINESS_HOURS": getattr(settings, "BUSINESS_HOURS", "09:00 – 18:00 (Pzt – Cmt)"),

        # WhatsApp için + olmadan uluslararası format
        "BUSINESS_WHATSAPP": getattr(settings, "BUSINESS_WHATSAPP", "905331432357"),

        "BUSINESS_INSTAGRAM": getattr(settings, "BUSINESS_INSTAGRAM", "https://www.instagram.com/umay.oto"),
        "BUSINESS_FACEBOOK": getattr(settings, "BUSINESS_FACEBOOK", None),

        "MAP_EMBED_SRC": getattr(
            settings,
            "MAP_EMBED_SRC",
            "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d317.57589883183346!2d29.393528009666944!3d40.77723920814849!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14cadf8e01a0f4df%3A0x63d522302409b3cf!2sUmay%20Oto%20Yedek%20Par%C3%A7a!5e0!3m2!1str!2str!4v1755636859221!5m2!1str!2str",
        ),

        # Canonical + absolute URL üretimi için
        "SITE_URL": settings.SITE_URL,
    }
