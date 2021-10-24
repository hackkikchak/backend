DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "corsheaders",
    "rest_framework",
    "django_filters",
    "djoser",
    "drf_yasg",
]

PROJECT_APPS = [
    "backend.src",
    "backend.apps.services",
    "backend.apps.restaurants",
    "backend.apps.users",
    "backend.apps.warehouse",
    "backend.apps.products",
    "backend.apps.cart",
    "backend.apps.orders",
    #
    "backend.apps.role_buyer",
    "backend.apps.role_cook",
    "backend.apps.role_cashier",
    "backend.apps.role_courier",
    "backend.apps.role_admin",


]

DEVELOPER_APPS = [
    *DEFAULT_APPS,
    *PROJECT_APPS,
    "debug_toolbar",
]

PRODUCTION_APPS = [*DEFAULT_APPS, *PROJECT_APPS]
