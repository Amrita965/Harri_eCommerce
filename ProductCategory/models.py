from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    image_path = models.ImageField(upload_to="category_img") # MEDIA_ROOT/category_img
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.category_name}"
    

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategory_set")
    subcategory_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subcategory_name}"