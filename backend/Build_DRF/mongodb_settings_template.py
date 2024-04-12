import os

from django.conf import settings

settings.DATABASES["ENGINE"] = "djongo"
settings.DATABASES["NAME"] = "Cluster0"
settings.DATABASES["CLIENT"] = {
    "host": "__HOST__",
    "username": "__USERNAME__",
    "password": "__PASSWORD__",
}
