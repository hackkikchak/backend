from django.db import models
from django.utils.translation import gettext as _



class OrderMixin(models.Model):
    """
    Order Mixin;
    Contains 'order' field;
    Содержит поле 'order' - (Сортировка)
    """

    order = models.PositiveIntegerField(verbose_name=_("Order"), default=0)

    class Meta:
        abstract = True


class DateCreatedMixin(models.Model):
    """
    Date Created Mixin;
    Contains 'date_created' field;
    Содержит поле 'date_created' - (Дата Создания)
    """

    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class DateUpdatedMixin(models.Model):
    """
    Date Updated Mixin;
    Contains 'date_updated' field;
    Содержит поле 'date_updated' - (Дата последнего обновления)
    """

    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True