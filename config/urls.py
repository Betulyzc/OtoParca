from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.views.decorators.cache import cache_page

from products import views as v
from products.sitemaps import BrandSitemap, ProductSitemap

sitemaps = {
    "brands": BrandSitemap,
    "products": ProductSitemap,
}


@require_GET
@cache_page(60 * 60 * 6)  # 6 saat cache (production için iyi)
def robots_txt(request):
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        f"Sitemap: {settings.SITE_URL.rstrip('/')}/sitemap.xml\n"
    )
    return HttpResponse(content, content_type="text/plain")


urlpatterns = [
    path("yonetim/", admin.site.urls),
    path("", v.home, name="home"),
    path("urunler/", v.all_products, name="all_products"),
    path("<slug:slug>-yedek-parca/", v.brand_page, name="brand_page"),
    path("urun/<slug:slug>/", v.product_detail, name="product_detail"),

    # robots.txt
    path("robots.txt", robots_txt, name="robots_txt"),

    # sitemap.xml (cache önerilir)
    path("sitemap.xml", cache_page(60 * 60 * 6)(sitemap), {"sitemaps": sitemaps}, name="sitemap"),
]

# Development'da medya dosyalarını Django servis edebilir, production'da Nginx/Cloudflare servis etmeli.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
