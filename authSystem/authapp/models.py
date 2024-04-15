from django.db import models

class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    generated_otp = models.CharField(max_length=6, blank=True, null=True)
    your = models.TextField(max_length = 4)
