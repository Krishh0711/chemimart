from django.db import models
from accounts.managers import UserManager
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    mobile_number = models.CharField(max_length=10, unique=True)
    otp = models.CharField(max_length=6)
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'mobile_number'

    def verify_otp(self, otp):
        return True