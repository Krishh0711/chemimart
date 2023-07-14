import time
from django.db import models
from accounts.models import SellerAccount
from django.utils.text import slugify
from common.models import AbstractTimeStampModel

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
