import uuid
from django.db import models
from common.models import AbstractTimeStampModel
from accounts.models import CustomerAccount
from stores.models import Product
from django.core.validators import MinValueValidator
from orders.constants import ORDER_ITEM_PROCESSING ,ORDER_ITEM_SHIPPED, ORDER_ITEM_DELIVERED ,ORDER_ITEM_CANCELLED, PAYMENT_PENDING, PAYMENT_COMPLETED, PAYMENT_FAILED

class Cart(AbstractTimeStampModel):
    customer = models.ForeignKey(CustomerAccount, null=True, blank=True, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=40, null=True, blank=True)
    is_active = models.BooleanField(default=True)


    @classmethod
    def get_or_create_cart(cls, session_id):
        return cls.objects.get_or_create(session_id=session_id, is_active=True)



class CartItems(AbstractTimeStampModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    
    @classmethod
    def add_to_cart(cls, cart, product_id, quantity):
        cart_item, is_created = cls.objects.get_or_create(cart=cart, product_id=product_id)
        if is_created:
            cart_item.quantity = quantity
        else:
            cart_item.quantity += quantity
        cart_item.save()

    @classmethod
    def remove_from_cart(cls, cart, product_id, quantity):
        try:
            cart_item = cls.objects.get(cart=cart, product_id=product_id)
            if cart_item.quantity <= quantity:
                cart_item.delete()
            else:
                cart_item.quantity -= quantity
                cart_item.save()
        except CartItems.DoesNotExist:
            pass

    @classmethod
    def get_all_items_of_cart(cls, cart):
        cart_items_qs = cls.objects.filter(cart=cart).values('product__id', 'product__name', 'quantity', 'product__store__store_link')
        return list(cart_items_qs)


class Order(AbstractTimeStampModel):

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_PENDING, 'Pending'),
        (PAYMENT_COMPLETED, 'Completed'),
        (PAYMENT_FAILED, 'Failed'),
    ]
    
    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE)
    address = models.TextField()
    payment_status = models.IntegerField(choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_PENDING)


class OrderItem(AbstractTimeStampModel):
    ORDER_ITEM_STATUS_CHOICES = [
        (ORDER_ITEM_PROCESSING, 'Processing'),
        (ORDER_ITEM_SHIPPED, 'Shipped'),
        (ORDER_ITEM_DELIVERED, 'Delivered'),
        (ORDER_ITEM_CANCELLED, 'Cancelled'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)   
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    order_item_status = models.IntegerField(choices=ORDER_ITEM_STATUS_CHOICES, default=ORDER_ITEM_PROCESSING)










    

