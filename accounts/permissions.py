from rest_framework.permissions import BasePermission
from accounts.models import SellerAccount

class IsSeller(BasePermission):
    """
    Custom permission class that checks if the user is a seller.
    """
    def has_permission(self, request, view):
        return request.user.is_seller