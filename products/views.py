from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET

from .models import Product, Brand


@require_GET
def home(request):
    # Sadece ürünü olan markalar (performans: sadece gereken alanlar)
    brands = (
        Brand.objects
        .annotate(product_count=Count("products"))
        .filter(product_count__gt=0)
        .only("name", "slug")
        .order_by("name")
    )
    return render(request, "home.html", {"brands": brands})


@require_GET
def all_products(request):
    q = (request.GET.get("q") or "").strip()

    qs = (
        Product.objects
        .select_related("brand", "category")
        .only(
            "name", "slug", "oem_code", "compatible", "short_desc", "image", "featured", "created_at",
            "brand__name", "brand__slug",
            "category__name", "category__slug",
        )
        .order_by("-created_at")
    )

    if q:
        qs = qs.filter(
            Q(name__icontains=q) |
            Q(oem_code__icontains=q) |
            Q(compatible__icontains=q) |
            Q(brand__name__icontains=q) |
            Q(category__name__icontains=q)
        ).distinct()

    # Canlıda performans için sayfalama
    paginator = Paginator(qs, 24)  # sayfa başına ürün
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(request, "products.html", {"products": page_obj, "q": q, "page_obj": page_obj})


@require_GET
def brand_page(request, slug):
    brand = get_object_or_404(Brand.objects.only("id", "name", "slug"), slug=slug)

    products_qs = (
        Product.objects
        .select_related("brand", "category")
        .filter(brand=brand)
        .only(
            "name", "slug", "oem_code", "compatible", "short_desc", "image", "featured", "created_at",
            "brand__name", "brand__slug",
            "category__name", "category__slug",
        )
        .order_by("-created_at")
    )

    paginator = Paginator(products_qs, 24)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(
        request,
        "brand.html",
        {"brand": brand, "products": page_obj, "page_obj": page_obj}
    )


@require_GET
def product_detail(request, slug):
    p = get_object_or_404(
        Product.objects
        .select_related("brand", "category")
        .only(
            "name", "slug", "oem_code", "compatible", "short_desc", "image", "featured", "created_at",
            "brand__name", "brand__slug",
            "category__name", "category__slug",
        ),
        slug=slug
    )
    return render(request, "product_detail.html", {"p": p})
