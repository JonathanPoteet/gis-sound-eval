# src/views.py
from rest_framework.views import APIView
from rest_framework.response import Response

class SpatialFeatureView(APIView):
    def get(self, request):
        return Response({"message": "PostGIS features endpoint placeholder"})