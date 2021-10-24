from django.db import models
from django.utils.translation import gettext as _
from apps.services.models import (
    DateCreatedMixin,
    DateUpdatedMixin,
)



class Product(DateUpdatedMixin, DateCreatedMixin):
    """
    Товар
    """

    name = models.CharField(verbose_name=_("Наименование"), max_length=500)
    price = models.DecimalField(
        verbose_name=_("Цена"),
        max_digits=10,
        decimal_places=2,
    )
    description = models.TextField(
        verbose_name=_("Описание"), blank=True, null=True
    )
    category = models.ForeignKey(
        "products.Category",
        verbose_name=_("Категория"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="products",
    )
    is_published = models.BooleanField(
        verbose_name=_("Товар опубликован"), default=False
    )


    class Meta:
        verbose_name = _("Товар")
        verbose_name_plural = _("Товары")

    def __str__(self):
        return self.name