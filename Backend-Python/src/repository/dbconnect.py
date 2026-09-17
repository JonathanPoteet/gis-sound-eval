import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

import django

django.setup()

from django.contrib.gis.db import models
from django.db import connection

class GISPlace(models.Model):
    name = models.CharField(max_length=100)
    geom = models.PointField(srid=4326)

    class Meta:
        app_label = "repository"


def check_database_connection() -> None:
    """Raise an exception if the configured PostGIS database is unavailable."""
    connection.ensure_connection()