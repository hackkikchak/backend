from django.db import models
from django.utils.translation import gettext as _
from apps.services.models import (
    DateCreatedMixin,
    DateUpdatedMixin,
)


class Order(DateUpdatedMixin, DateCreatedMixin, models.Model):
    """
    Заказ
    """

    class OrderTypes(models.IntegerChoices):
        DELIVERY = 1, _('Доставка')
        TAKEAWAY = 2, _('На вынос')
        RESTAURANT = 3, _('В зале')

    class Status(models.IntegerChoices):
        DELIVERY = 1, _('В процессе приготовления')
        TAKEAWAY = 2, _('Готов к выдаче')
        RESTAURANT = 3, _('В зале')

    user = models.ForeignKey(
        "users.User",
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,
        related_name="cart",
    )
    type_order = models.IntegerField(choices=OrderTypes.choices, default=3)
    comment = models.TextField(
        verbose_name=_("Описание"), blank=True, null=True
    )
    # дата создания
    # дата


    class Meta:
        verbose_name = _("Заказ")
        verbose_name_plural = _("Заказы")
        ordering = ["-date_created"]