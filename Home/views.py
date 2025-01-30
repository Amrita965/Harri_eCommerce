from django.shortcuts import render
from ProductCategory.models import Category

# Create your views here.

def home(request):
    categories = Category.objects.all()
    dict = {
        "title": "Home Page",
        "categories": categories
    }
    print(request.user.is_authenticated)
    return render(request, 'Home/home.html', context=dict)