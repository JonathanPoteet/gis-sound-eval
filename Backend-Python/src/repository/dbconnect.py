# GeoDjango Model
from django.contrib.gis.db import models # <--- Import from contrib.gis

class GISPlace(models.Model):
    name = models.CharField(max_length=100)
    geom = models.PointField(srid=4326) # Native PostGIS spatial geometry