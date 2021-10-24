from django.db import models
from django.utils.translation import gettext as _


class Restaurant(models.Model):
    """
    Ресторан
    """

    name = models.CharField(verbose_name=_("Наименование"), max_length=255)
    address = models.CharField(verbose_name=_("Адрес"), max_length=500)
    description = models.TextField(
        verbose_name=_("Описание"), blank=True, null=True
    )
    is_published = models.BooleanField(
        verbose_name=_("Является опубликованным"), default=False
    )

    class Meta:
        verbose_name = _("Ресторан")
        verbose_name_plural = _("Рестораны")

    def __str__(self):
        return self.name