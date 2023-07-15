from accounts.models import SellerAccount
from stores.models import Product
from rest_framework.response import Response
from rest_framework import status


def valid_product_id_and_quantity_required(func):
    """
    Decorator to validate the product ID and quantity.
    """
    def wrapper(view, request, *args, **kwargs):
        store_link = request.data.get('store_link', None)
        product_id = request.data.get('product_id', None)
        quantity = request.data.get('quantity', None)
        if not isinstance(quantity, int):
            return Response({'error':"Quantity should be integer"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            product = Product.objects.get(id=product_id, store__store_link=store_link, is_available=True)
        except:
            return Response({'error':"Product is not available at this store"}, status=status.HTTP_400_BAD_REQUEST)
        return func(view, request, *args, **kwargs)
    return wrapper