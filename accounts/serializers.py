from rest_framework import serializers
from accounts.models import SellerAccount, User
from django.db import transaction

class SellerAccountLoginSerializer(serializers.Serializer):
    mobile_number = serializers.CharField(max_length=10, required=True)
    otp = serializers.CharField(max_length=6, required=True)

    @transaction.atomic
    def create(self, validated_data):
        user, is_created = User.objects.get_or_create(mobile_number=validated_data.get('mobile_number'))
        if not user.verify_otp(validated_data.get('otp')):
            raise serializers.ValidationError({'message':'Invalid OTP'})
        if is_created or not user.is_seller:
            user.is_seller = True
            user.save()
        return SellerAccount.objects.get_or_create(user=user)