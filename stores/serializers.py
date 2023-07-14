from rest_framework import serializers
from accounts.models import SellerAccount
from stores.models import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'seller_account', 'name', 'address', 'store_link']
        read_only_fields = ('store_link',)
        extra_kwargs = {'seller_account': {'write_only': True}}