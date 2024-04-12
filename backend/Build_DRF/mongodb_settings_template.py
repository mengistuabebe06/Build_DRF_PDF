import os
from django.conf import settings

# Access database information from settings.py
db_engine = settings.DATABASES["default"]["ENGINE"]
db_name = settings.DATABASES["default"]["NAME"]
db_host = settings.DATABASES["default"]["CLIENT"]["host"]
db_username = settings.DATABASES["default"]["CLIENT"]["username"]
db_password = settings.DATABASES["default"]["CLIENT"]["password"]

# Use the database information in your code
settings.DATABASES["ENGINE"] = db_engine
settings.DATABASES["NAME"] = db_name
settings.DATABASES["CLIENT"] = {
    "host": db_host,
    "username": db_username,
    "password": db_password,
}
