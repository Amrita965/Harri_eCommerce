from django.urls import path
from .views import all_products

app_name = "Products"

urlpatterns = [
    path("all-products/", all_products, name="all_products"),
    path("all-products/<str:subcategory_name>/", all_products, name="all_products")
]
