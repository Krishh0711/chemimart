from accounts.models import SellerAccount
from stores.models import Store
from rest_framework.response import Response
from rest_framework import status


def valid_store_id_required(func):
    """
    Decorator to validate the store ID and add it to the request.
    """
    def wrapper(view, request, *args, **kwargs):
        store_id = kwargs.get('store_id', None)
        try:
            store = Store.objects.get(id=store_id, seller_account__user_id=request.user.id)
            request.store = store  
        except Store.DoesNotExist:
            return Response({'error':"Invalid store id"}, status=status.HTTP_400_BAD_REQUEST)
        return func(view, request, *args, **kwargs)
    return wrapper