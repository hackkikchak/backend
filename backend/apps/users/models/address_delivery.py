from django.db import models
from django.utils.translation import gettext as _
from apps.services.models import (
    DateCreatedMixin,
    DateUpdatedMixin,
)


class AddressDelivery(DateUpdatedMixin, DateCreatedMixin, models.Model):
    """
    Способ доставки
    """


    user = models.ForeignKey(
        "users.User",
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,
    )
    name = models.CharField(verbose_name=_("Пользователь"),max_length=500,blank=True, null=True)


    class Meta:
        verbose_name = _("Способ доставки")
        verbose_name_plural = _("Способ доставки")
