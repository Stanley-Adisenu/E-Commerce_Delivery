from rest_framework import serializers
from .models import Delivery

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['id','order_id','delivery_status','tracking_number','courier','estimated_delivery_date','created_at','updated_at']