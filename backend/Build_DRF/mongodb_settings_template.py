import os

# from django.conf import settings
from . import settings

settings.DATABASES["default"]["ENGINE"] = "djongo"
settings.DATABASES["default"]["NAME"] = "Cluster0"
settings.DATABASES["default"]["CLIENT"] = {
    "host": "__HOST__",
    "username": "__USERNAME__",
    "password": "__PASSWORD__",
}
