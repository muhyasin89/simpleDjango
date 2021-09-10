from app.api.serializers.orders_serializers import (
    OrderSerializer,
    OrderStatusSerializer,
)
from app.orders.models import Order, OrderStatus
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response


def get_filtering_order(queryset, urls_params):
    if "sort" in urls_params:
        if urls_params["sort"].lower() == "pending":
            queryset = Order.pending.all()
        elif urls_params["sort"].lower() == "complete":
            queryset = Order.complete.all()
        elif urls_params["sort"].lower() == "failed":
            queryset = Order.failed.all()

    return queryset


class OrderListView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    ordering_fields = "-date_created"

    def get_queryset(self):
        queryset = super().get_queryset()

        urls_params = self.request.GET

        if urls_params:
            queryset = get_filtering_order(queryset, urls_params)

        return queryset


class OrderRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderStatusSerializer
    lookup_fields = ["pk"]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Exception as e:
            return Response(status=400)
        return Response(status=204)


class OrderStatusListView(ListCreateAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer
    ordering_fields = "-date_created"


class OrderStatusRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderSerializer
    lookup_fields = ["pk"]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Exception as e:
            return Response(status=400)
        return Response(status=204)
