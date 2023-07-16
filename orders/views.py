from rest_framework.views import APIView
from orders.models import Cart, CartItems, OrderItem
from orders.decorators import valid_product_id_and_quantity_required
from rest_framework.response import Response
from rest_framework import status
from common.utils import validate_phone_number_and_otp
from common.constants import INTERNAL_SERVER_ERROR_MESSAGE
from orders.constants import CART_EMPTY_ERROR_MESSAGE

class UpdateCartItemsView(APIView):
    """
    API view for updating (adding/removing) cart items.

    This view handles the POST requests to update the cart items. If the provided quantity is greater than 0,
    it adds the quantity to the existing quantity of the same item in the cart. If the quantity is less than or
    equal to 0, it subtracts the absolute value of the quantity from the existing quantity of the same item.
    """
    
    @valid_product_id_and_quantity_required
    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id', None)
        quantity = request.data.get('quantity', None)
        if not request.session.session_key:
            request.session.save()
        try:
            cart, is_created = Cart.get_or_create_cart(request.session.session_key)
            if quantity >=0:
                CartItems.add_to_cart(cart, product_id, quantity)
            else:
                if not is_created:
                    CartItems.remove_from_cart(cart, product_id, -1*quantity)
            response_data = {
                "cart_items" : CartItems.get_all_items_of_cart(cart)
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            # TODO: log error for internal tracking
            return Response({'error': INTERNAL_SERVER_ERROR_MESSAGE}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PlaceOrderView(APIView):
    """
    API view for placing an order.
    """
    
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number', None)
        otp = request.data.get('otp', None)
        if not validate_phone_number_and_otp(phone_number, otp):
            return Response({'error': "Invalid phone number or OTP."}, status=status.HTTP_400_BAD_REQUEST)
        address = request.data.get('address', None)
        if not address or not isinstance(address, str):
            return Response({'error': "Please provide valid address"}, status=status.HTTP_400_BAD_REQUEST)
        if not request.session.session_key:
            request.session.save()
        try:
            cart = Cart.get_cart_object_by_user_session(request.session.session_key)
            if not cart:
                return Response({'error': CART_EMPTY_ERROR_MESSAGE}, status=status.HTTP_400_BAD_REQUEST)
            cart_items = CartItems.objects.filter(cart=cart)
            if cart_items.exists():
                order_id = OrderItem.place_order(cart, phone_number, address)
                return Response({"order_id": order_id}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': CART_EMPTY_ERROR_MESSAGE}, status=status.status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # TODO: log error for internal tracking
            return Response({'error': INTERNAL_SERVER_ERROR_MESSAGE}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# INFO: made this just for testing
class OrderDetails(APIView):
    """
    API view for retrieving order details.
    """
    def get(self, request, **kwargs):
        order_id = kwargs.get('order_id', '')
        data = {
            "order_details": list(OrderItem.get_order_item_detail_by_order_id(order_id))
        }
        return Response(data, status=200)
