from app.api.views.orders_views import (
    OrderListView,
    OrderRetrieveUpdateDeleteView,
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
]
