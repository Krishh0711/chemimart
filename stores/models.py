import time
from django.db import models
from accounts.models import SellerAccount
from django.utils.text import slugify
from common.models import AbstractTimeStampModel
from django.core.validators import MinValueValidator

class Store(AbstractTimeStampModel):
    seller_account = models.ForeignKey(SellerAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    store_link = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.store_link = slugify(self.name + " " + str(int(time.time())))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(AbstractTimeStampModel):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    mrp = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='product_images/')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    @property
    def discount(self):
        discount_percentage = ((self.mrp - self.sale_price) / self.mrp) * 100
        return f"{discount_percentage:.2f}%"


