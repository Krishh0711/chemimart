from rest_framework import serializers
from accounts.models import SellerAccount
from stores.models import Store, Product
from decimal import Decimal


class StoreListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'seller_account', 'name', 'address', 'store_link']
        read_only_fields = ('store_link',)
        extra_kwargs = {'seller_account': {'write_only': True}}


class ProductSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)
    store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all(), required=False, write_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'store', 'name', 'image', 'description', 'sale_price', 'mrp', 'discount']
        read_only_fields = ('discount',)
    

    def validate(self, attrs):
        # Raise error if product name already exists in store
        name = attrs.get('name')
        store=self.context['store']
        product = Product.objects.filter(store=store, name=name)
        if product.exists():
            raise serializers.ValidationError({"name":"Product with name {0} already exists in {1} store".format(name, store.name)})
        # Raise error if sale_price is greater than mrp
        mrp = attrs.get('mrp')
        sale_price = attrs.get('sale_price')
        if mrp < sale_price:
            raise serializers.ValidationError({"sale_price":"Sale price of the product cannot be grater than its MRP"})
        return attrs
    
    def create(self, validated_data):
        validated_data['store'] = self.context['store']
        return super().create(validated_data)



class StoreDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Store
        fields = ['id', 'name', 'address']