from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone

# Create your models here.

class UserInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userinfo")
    phone = models.CharField(max_length=30, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    password_reset_code = models.CharField(max_length=300, null=True, blank=True)
    reset_code_created_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_reset_code_expired(self):
        expiration_time = timedelta(hours=1)
        # print(expiration_time)
        if self.reset_code_created_at:
            return timezone.now() > self.reset_code_created_at + expiration_time
        return True

    def __str__(self):
        return f"{self.user.username}"
    
