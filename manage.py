import os
import sys
from django.conf import settings
from django.core.management import execute_from_command_line
from django.urls import path

if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY="segredo-super-secreto-para-despesas",
        ROOT_URLCONF=__name__,
        MIDDLEWARE=[
            "django.middleware.common.CommonMiddleware",
            "django.middleware.csrf.CsrfViewMiddleware",
        ],
        INSTALLED_APPS=[
            "django.contrib.contenttypes",
            "django.contrib.auth",
            "despesas",
        ],
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": "db.sqlite3",
            }
        },
        TIME_ZONE="UTC",
        USE_TZ=True,
    )

from despesas import listar_despesas, criar_despesa

urlpatterns = [
    path("", listar_despesas, name="listar"),
    path("criar/", criar_despesa, name="criar"),
]

if __name__ == "__main__":
    execute_from_command_line(sys.argv)