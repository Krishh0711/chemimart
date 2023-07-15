from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.serializers import SellerAccountLoginSerializer


class SellerAccountLoginView(APIView):
    """
    API view for seller account login.
    """
    def post(self, request):
        serializer = SellerAccountLoginSerializer(data=request.data)
        if serializer.is_valid():
            status_code = status.HTTP_200_OK
            seller, is_created = serializer.save()
            if is_created:
                status_code = status.HTTP_201_CREATED
            refresh = RefreshToken.for_user(seller.user)
            return Response({'access': str(refresh.access_token), 'refresh': str(refresh)}, status=status_code, content_type="application/json")
        return Response({'error' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)