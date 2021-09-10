from app.api.serializers.orders_serializers import OrderSerializer
from app.orders.models import Order
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response


class OrderListView(ListCreateAPIView):
    serializer_class = OrderSerializer
    ordering_fields = "-date_created"


class OrderRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_fields = ["pk"]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Exception as e:
            return Response(status=400)
        return Response(status=204)
