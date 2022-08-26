from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=100, null = True, blank = True, default='0')
    profile_image = models.ImageField(upload_to = 'profile_image/', null = True, blank = True, default = '0')

class UserFollow(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_follow")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_following")

    def __str__(self):
        return f"{self.from_user} {self.to_user}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"