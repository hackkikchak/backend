from django.db import models
from django.utils.translation import gettext as _
from apps.services.models import (
    DateCreatedMixin,
    DateUpdatedMixin,
)


class PaymentMethod(DateUpdatedMixin, DateCreatedMixin, models.Model):
    """
    Способ оплаты
    """


    user = models.ForeignKey(
        "users.User",
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,

    )
    name = models.CharField(verbose_name=_("Пользователь"),max_length=500,blank=True, null=True)


    class Meta:
        verbose_name = _("Способ оплаты")
        verbose_name_plural = _("Способ оплаты")
