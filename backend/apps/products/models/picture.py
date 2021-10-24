from django.db import models
from django.utils.translation import gettext as _
from apps.services.models import OrderMixin


class Picture(OrderMixin):
    """
    Изображение товара
    """

    product = models.ForeignKey(
        "products.Product",
        verbose_name=_("Товар"),
        on_delete=models.CASCADE,
        related_name="pictures",
    )
    image = models.ImageField(
        _("Изображение"),
        blank=True,
        null=True,
    )


    class Meta:
        verbose_name = _("Изображение товара")
        verbose_name_plural = _("Изображения товаров")

    def __str__(self):
        return self.product.name