from rest_framework import serializers
from api.models import PricePolicy
class PriceSerializers(serializers.ModelSerializer):
    class Meta:
        model=PricePolicy
        fields='__all__'
