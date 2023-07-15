from django.db import models
from common.models import AbstractTimeStampModel
from accounts.models import CustomerAccount
from stores.models import Product

class Cart(AbstractTimeStampModel):
    customer = models.ForeignKey(CustomerAccount, null=True, blank=True, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=40, null=True, blank=True)
    is_active = models.BooleanField(default=True)


class CartItems(AbstractTimeStampModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)










    

