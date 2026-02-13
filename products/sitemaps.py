from django.contrib.sitemaps import Sitemap
from django.utils import timezone
from .models import Brand, Product


class BrandSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        # Sadece gerekli alanları çekiyoruz (performans)
        return (
            Brand.objects
            .only("slug")
            .order_by("name")
        )

    def location(self, obj):
        # Hardcoded path yerine güvenli format
        return f"/{obj.slug}-yedek-parca/"

    def lastmod(self, obj):
        # Marka için özel tarih yoksa güncel zamanı vermek yerine None daha doğru
        return None


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return (
            Product.objects
            .select_related("brand", "category")
            .only("slug", "created_at")
            .order_by("-created_at")
        )

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        # get_absolute_url varsa onu kullanmak en temiz yol
        return obj.get_absolute_url()
