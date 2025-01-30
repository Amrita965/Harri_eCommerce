from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.models import User
from .models import UserInfo
from django.contrib.auth.hashers import make_password

# Create your views here.

def register_view(request):

    if(request.user.is_authenticated):
        return redirect("Home:home")

    dict = {
        "title": "SignUp Page"
    }

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confPassword = request.POST.get("confPassword")

        # Password Validation
        if password != confPassword:
            messages.error(request, "Passwords do not match.")
            return redirect("SignUp:register_view")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("SignUp:register_view")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("SignUp:register_view")
        
        # Hashed the password
        # hashed_password = make_password(password)
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()

        UserInfo(user=user).save()

        messages.success(request, "You have successfully registered!")
        return redirect("Login:login_view")
        

    return render(request, "SignUp/signup.html", context=dict)