from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):

    class UserRoles(models.IntegerChoices):
        BUYER = 1, _('Покупатель')
        ADMINISTRATOR = 2, _('Администратор')
        CASHIER = 3, _('Кассир')
        COOK = 4, _('Повар')
        COURIER = 5, _('Курьер')


    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, "
            "digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    second_name = models.CharField(
        _("second name"), max_length=150, blank=True
    )

    role = models.IntegerField(_("Роль пользователя"),choices=UserRoles.choices, default=1)

    email = models.EmailField(_("email address"), blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    avatar = models.ImageField(
        _("Изображение"),
        blank=True,
        null=True,

    )

    @property
    def role_string(self):
        return self.UserRoles.ADMINISTRATOR.label

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)




    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "last_name",
        "first_name",
        "second_name",
        "email",
        "is_staff",
        "role",
        "avatar",
        "is_active",
        "role_string",
    ]

    class Meta:
        swappable = "AUTH_USER_MODEL"
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
