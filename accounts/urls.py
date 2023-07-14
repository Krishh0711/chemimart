from django.urls import path
from accounts.views import SellerAccountLoginView

urlpatterns = [
    path('api/seller/login/', SellerAccountLoginView.as_view(), name='seller-account-register'),
]