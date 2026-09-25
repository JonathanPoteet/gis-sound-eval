# src/views.py
import src.service.service as service

# so python is establishing a view here that will handle requests to the /api/map/ endpoint. The view will use the GisService class from the service layer to get map data and return it as a response.
# the url pattern for this view is defined in the urls.py file
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.response import Response

class SpatialFeatureView(APIView):
    def __init__(self):
        self.gis_service = service.GisService()

    def get(self, request):
        try:
            # Use the service layer to get map data
            geojson_data = self.gis_service.get_map_data(request)
            # rather than returning all data we want to only return a list of features
            features = geojson_data.get("features", [])
            return Response({"features": features})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
