from django.db import models

from . import ORDER_STATUS, Complete, Failed, Pending


class OrderFailedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().order_status.filter(status=Failed)
            if super().get_queryset().order_status.count()
            else super().get_queryset().none()
        )


class OrderPendingManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().order_status.filter(status=Pending)
            if super().get_queryset().order_status.count()
            else super().get_queryset().none()
        )


class OrderCompleteManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().order_status.filter(status=Complete)
            if super().get_queryset().order_status.count()
            else super().get_queryset().none()
        )


# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=225)

    failed = OrderFailedManager()
    pending = OrderPendingManager()
    complete = OrderCompleteManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderStatus(models.Model):
    order = models.ForeignKey(
        Order,
        null=True,
        related_name="order_status",
        on_delete=models.SET_NULL,
    )
    status = models.IntegerField(choices=ORDER_STATUS, default=Pending)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
