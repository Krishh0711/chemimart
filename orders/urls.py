from django.urls import path
from orders.views import UpdateCartItemsView, PlaceOrderView, OrderDetails

urlpatterns = [
    path('update_cart/', UpdateCartItemsView.as_view(), name='update-cart-items-view'),
    path('place_order/', PlaceOrderView.as_view(), name='place-order-view'),
    path('order/<str:order_id>/details/', OrderDetails.as_view(), name='order-detail-view'),
]