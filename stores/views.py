from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from stores.models import Store, Product
from stores.serializers import StoreSerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsSeller
from accounts.models import SellerAccount
from stores.decorators import valid_store_id_required

class StoreListCreateView(APIView):
    """
    API view for listing and creating stores.
    Requires seller authentication.
    GET: Get a list of all stores.
    POST: Create a new store.
    """
    permission_classes = [IsAuthenticated, IsSeller]

    def get(self, request):
        """
        Retrieve stores associated with the logged-in seller account.
        """
        seller_account = SellerAccount.objects.get(user=request.user)
        queryset = Store.objects.filter(seller_account=seller_account)
        serializer = StoreSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new store associated with the logged-in seller account.
        """
        try:
            seller_account = SellerAccount.objects.get(user=request.user)
        except SellerAccount.DoesNotExist:
            return Response({'error': 'Seller account not found.'}, status=404)
        serializer = StoreSerializer(data={"seller_account": seller_account.id, **request.data})
        if serializer.is_valid():
            store = serializer.save()
            response_data = {
                'store_id': store.id,
                'store_link': store.store_link
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)


class ProductListCreateView(APIView):
    """
    API view for listing and creating products for seller account.
    Requires seller authentication and valid store ID.
    GET: Get a list of all products.
    POST: Create a new product.
    """
    permission_classes = [IsAuthenticated, IsSeller]
    parser_classes = (MultiPartParser, FormParser,)
    
    @valid_store_id_required
    def get(self, request, **kwargs):
        """
        Retrieve all products for the logged in seller's store.
        """
        queryset = Product.objects.filter(store=request.store)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @valid_store_id_required
    def post(self, request, **kwargs):
        """
        Create a new product for the logged in seller's store.
        """
        serializer = ProductSerializer(data=request.data, context={'store': request.store})
        if serializer.is_valid():
            product = serializer.save()
            response_data = {
                'id': product.id,
                'name': product.name,
                'image': product.image.url
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)




