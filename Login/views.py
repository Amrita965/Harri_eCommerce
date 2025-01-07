from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import string
import random
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.

def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)

        except User.DoesNotExist:
            messages.error(request, "Invalid username or password.")
            return redirect("Login:login_view")
        
        if check_password(password, user.password):
            user.is_active = True
            user.save()
            login(request, user)
            messages.success(request, "You have logged in successfully")
            return redirect("Home:home")

        user = authenticate(request, username=username, password=password)

        print(user)

        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in successfully!")
            return redirect("Home:home")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("Login:login_view")
    
    dict = {
        "title": "Login Page"
    }
    return render(request, "Login/login.html", context=dict)

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have logged out successfully!")
    return redirect("Login:login_view")


def password_reset_request(request):

    if request.method == "POST":
        email = request.POST.get("email")

        print(request.POST)

        try:
            user = User.objects.get(email=email)

            reset_code = ''.join(random.choices(string.ascii_letters + string.digits, k=150))
            user.userinfo.password_reset_code = reset_code
            user.userinfo.save()

            # Create password reset link
            reset_link = request.build_absolute_uri(reverse("Login:reset_password", kwargs={"reset_code": reset_code}))
    
            # Render the HTML template with context
            html_content = render_to_string("Login/reset_password_email_template.html", {"user": user, "reset_link": reset_link})
            
            # Create email
            email = EmailMessage(
                subject='Your OTP Code',
                body=html_content,
                from_email=settings.EMAIL_HOST_USER,
                to=[user.email],
            )
            email.content_subtype = 'html' # Set content type to HTML
            email.send(fail_silently=False)

            messages.success(request, "Password reset link sent to your email.")
            return redirect("Login:password_reset_request")

            "http://127.0.0.1:8000/reset-password/?reset_code=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


        except User.DoesNotExist:
            print("No user found")
            messages.error(request, "No user found with that email address.")
            return redirect("Login:password_reset_request")


    return render(request, "Login/forgot_password.html")


def reset_password(request, reset_code):
    return render(request, "Login/reset_password.html")
