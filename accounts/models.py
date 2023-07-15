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
    
    
    @classmethod
    def get_or_create_customer(cls, mobile_number, address):
        """
        Get or create a customer with the given mobile number and address.
        Args:
            mobile_number (str): The mobile number for the customer.
            address (str): The address for the customer.

        Returns:
            Customer: The customer object associated with the user.
        """
        user, is_created = User.objects.get_or_create(mobile_number=mobile_number)
        if user.is_buyer:
            return cls.objects.get(user=user)
        user.is_buyer = True
        user.save()
        return cls.objects.create(user=user, address=address)
        

        
