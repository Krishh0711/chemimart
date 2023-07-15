from rest_framework.views import APIView
from orders.models import Cart, CartItems
from orders.decorators import valid_product_id_and_quantity_required
from rest_framework.response import Response

class UpdateCartItemsView(APIView):
    
    @valid_product_id_and_quantity_required
    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id', None)
        quantity = request.data.get('quantity', None)
        if not request.session.session_key:
            request.session.save()
        try:
            cart, is_created = Cart.get_or_create_cart(str(request.session.session_key))
            if quantity >=0:
                CartItems.add_to_cart(cart, product_id, quantity)
            else:
                if not is_created:
                    CartItems.remove_from_cart(cart, product_id, -1*quantity)
            response_data = {
                "cart_items" : CartItems.get_all_items_of_cart(cart)
            }
            return Response(response_data, status=201)
        except Exception as e:
            # TODO: log error for internal tracking
            print(e.errors)
            return Response({'error': "Something went wrong. Please try again later"}, status=500)

