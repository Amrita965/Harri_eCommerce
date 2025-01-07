from django.urls import path
from .views import login_view, logout_view, password_reset_request, reset_password

app_name="Login"

urlpatterns = [
    path("login/", login_view, name="login_view"),
    path("logout/", logout_view, name="logout_view"),
    path("forgot-password/", password_reset_request, name="password_reset_request"),
    path("reset-password/<str:reset_code>/", reset_password, name="reset_password")
]
