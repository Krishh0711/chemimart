from functools import wraps
from accounts.models import SellerAccount
from stores.models import Store
from rest_framework.response import Response

def valid_store_id_required(func):
    """
    Decorator to validate the store ID and add it to the request.
    """
    def wrapper(view, request, *args, **kwargs):
        store_id = kwargs.get('store_id', None)
        seller_account = SellerAccount.objects.get(user=request.user)
        if not store_id:
            return Response({'error':"Invalid store id"}, status=400)
        try:
            store = Store.objects.get(id=store_id)
            if store.seller_account.id != store.seller_account.id:
                return Response({'error':"Invalid store id"}, status=400)
        except Store.DoesNotExist:
            return Response({'error':"Invalid store id"}, status=400)
        request.store = store  
        return func(view, request, *args, **kwargs)
    return wrapper