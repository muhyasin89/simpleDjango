from app.api.views.orders_views import (
    OrderListView,
    OrderRetrieveUpdateDeleteView,
    OrderStatusListView,
    OrderStatusRetrieveUpdateDeleteView,
)
from django.urls import path

app_name = "api_v1"

urlpatterns = [
    path(
        "orders",
        OrderListView.as_view(),
        name="order-list",
    ),
    path(
        "order/<int:pk>/detail/",
        OrderRetrieveUpdateDeleteView.as_view(),
        name="order-detail",
    ),
    path(
        "orders/status",
        OrderStatusListView.as_view(),
        name="order-list",
    ),
    path(
        "order/status/<int:pk>/detail/",
        OrderStatusRetrieveUpdateDeleteView.as_view(),
        name="order-detail",
    ),
]
