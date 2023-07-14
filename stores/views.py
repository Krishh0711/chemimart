from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from stores.models import Store
from stores.serializers import StoreSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsSeller
from accounts.models import SellerAccount

class StoreListCreateView(APIView):
    """
    API view for listing and creating stores.
    GET: Get a list of all stores.
    POST: Create a new store.
    """
    permission_classes = [IsAuthenticated, IsSeller]

    def get(self, request):
        """
        Retrieve stores associated with the logged-in seller account.
        Args: request (HttpRequest): HTTP request object.
        Returns: Response: List of stores associated with the seller account.
        """
        seller_account = SellerAccount.objects.get(user=request.user)
        queryset = Store.objects.filter(seller_account=seller_account)
        serializer = StoreSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new store associated with the logged-in seller account.
        Args: request (HttpRequest): HTTP request object.
        Returns: Response: Newly created store details including store ID and store link.
        Raises: SellerAccount.DoesNotExist: If the seller account for the logged-in user does not exist.
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



