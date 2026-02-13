from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Category, Brand


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "category", "oem_code", "featured", "created_at", "image_preview")
    list_filter = ("brand", "category", "featured")
    search_fields = ("name", "oem_code", "compatible")
    list_select_related = ("brand", "category")  # performans
    ordering = ("-created_at",)

    # Slug otomatik dolsun (admin önizleme). Modelde güvenli üretiyorsun zaten.
    prepopulated_fields = {"slug": ("name",)}

    # Çok kayıt varsa admin performansı için:
    autocomplete_fields = ("brand", "category")

    # Admin formunda alanları düzenli göster
    fieldsets = (
        (None, {
            "fields": ("name", "slug", "category", "brand", "oem_code", "compatible", "short_desc")
        }),
        ("Medya / Link", {
            "fields": ("image", "image_preview")
        }),
        ("Öne Çıkan / Tarih", {
            "fields": ("featured", "created_at")
        }),
    )

    # Canlıda created_at gibi alanlar admin’den değiştirilmesin:
    readonly_fields = ("created_at", "image_preview")

    # Admin listede ve formda görsel önizleme (canlıda da çalışır; MEDIA doğru servis edilmeli)
    def image_preview(self, obj):
        if obj and getattr(obj, "image", None):
            try:
                url = obj.image.url
            except Exception:
                return "-"
            return format_html(
                '<img src="{}" style="height:60px;width:auto;border-radius:6px;border:1px solid #ddd;" loading="lazy" />',
                url
            )
        return "-"
    image_preview.short_description = "Önizleme"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)
