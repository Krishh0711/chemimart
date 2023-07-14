from rest_framework.permissions import BasePermission
from accounts.models import SellerAccount

class IsSeller(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_seller