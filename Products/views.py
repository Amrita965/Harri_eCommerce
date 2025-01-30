from django.shortcuts import render
from ProductCategory.models import Category, SubCategory
from Products.models import Product
# Create your views here.

def all_products(request, subcategory_name=None):

    categories = Category.objects.all()
    dict = {
        "title": "All Products",
        "categories": categories
    }

    if subcategory_name:
        sub_category = SubCategory.objects.get(subcategory_name = subcategory_name)
        products = sub_category.product_set.all()

        dict.update({"products": products, "sub_category": sub_category})

    return render(request, "Products/all_products.html", context=dict)