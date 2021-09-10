from app.orders.models import Order, OrderStatus
from rest_framework.serializers import ModelSerializer


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderStatusSerializer(ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = "__all__"
