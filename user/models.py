from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    age = models.IntegerField(default=0)
    profile_pic = models.ImageField(upload_to='profile_pics/',null=True)

    class Meta:
        db_table = 'user'
        