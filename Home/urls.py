from django.urls import path
from .views import home

app_name = "Home"

urlpatterns = [
    path('', home, name="home"),
]
