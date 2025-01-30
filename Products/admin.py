from django.contrib import admin
from .models import Brand, Product, ProductImage, ProductColor

# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "brand_name", "description", "created_at", "updated_at")

@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = ("id", "color_name", "created_at", "updated_at")

# admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ProductImage)

"categories/1/"