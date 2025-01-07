from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userinfo")
    phone = models.CharField(max_length=30, null=True)
    address = models.TextField(null=True)
    password_reset_code = models.CharField(max_length=300, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}"