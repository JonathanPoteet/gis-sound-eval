import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.contrib.gis.db import models
from django.db import connection
from django.core.serializers import serialize
from django.http import HttpResponse

class GISPlace(models.Model):
    name = models.CharField(max_length=100)
    geom = models.PointField(srid=4326)

    class Meta:
        app_label = "repository"


    def check_database_connection() -> None:
        """Raise an exception if the configured PostGIS database is unavailable."""
        connection.ensure_connection()

    def get_map_data(request):
        # Query your spatial data from PostGIS
        places = GISPlace.objects.all()
        
        # Serialize spatial queryset directly to GeoJSON format
        geojson_data = serialize('geojson', places, geometry_field='geom', fields=('name',))
        
        return HttpResponse(geojson_data, content_type='application/json')