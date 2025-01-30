from django.db import models
from ProductCategory.models import Category, SubCategory

# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand_name}"

class ProductColor(models.Model):
    color_name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.color_name}"


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.RESTRICT, related_name="product_set")
    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT)
    product_name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    tax = models.FloatField()
    price = models.FloatField()
    discount = models.FloatField()
    stock_quantity = models.IntegerField()
    weight = models.FloatField()
    color = models.ForeignKey(ProductColor, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_name}"


class ProductImage(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="productimage_set")
    image_path = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

