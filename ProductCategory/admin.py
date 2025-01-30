from django.contrib import admin
from .models import Category, SubCategory
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_name", "image_path", "created_at", "updated_at")

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "subcategory_name", "created_at", "updated_at")