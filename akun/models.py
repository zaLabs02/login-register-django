from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nama = models.CharField(max_length=200, blank=True, null=True)
    foto_profil = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username


# Create your models here.
