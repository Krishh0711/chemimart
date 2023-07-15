from django.db import models
from accounts.managers import UserManager
from django.contrib.auth.models import AbstractBaseUser
from common.models import AbstractTimeStampModel

class User(AbstractBaseUser):
    mobile_number = models.CharField(max_length=10, unique=True)
    otp = models.CharField(max_length=6)
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'mobile_number'

    def verify_otp(self, otp):
        return True


class SellerAccount(AbstractTimeStampModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.mobile_number


class CustomerAccount(AbstractTimeStampModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()


    def __str__(self):
        return self.user.mobile_number