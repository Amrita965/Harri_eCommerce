from django.urls import path
from .views import register_view

app_name="SignUp"

urlpatterns = [
    path("signup/", register_view, name="register_view")
]
