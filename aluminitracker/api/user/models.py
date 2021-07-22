from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    phone = models.IntegerField()
    rollno = models.IntegerField()
    gender = models.CharField(max_length=20)
    user_status = models.CharField(max_length=20, default='Student')
    company = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='user/', blank=True, null=True)
    verified = models.BooleanField(blank=True, default=False)
    session_token = models.CharField(max_length=10, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
