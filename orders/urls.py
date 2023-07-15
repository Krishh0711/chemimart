from django.urls import path
from orders.views import UpdateCartItemsView

urlpatterns = [
    path('update_cart/', UpdateCartItemsView.as_view(), name='update-cart-items-view'),
]