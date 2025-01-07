from django.shortcuts import render

# Create your views here.

def home(request):
    print(request.user.is_authenticated)
    return render(request, 'Home/home.html')