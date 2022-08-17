from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=100, null = True, blank = True, default='0')
    profile_image = models.ImageField(upload_to = 'profile_image/', null = True, blank = True, default = '0')