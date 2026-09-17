from django.urls import path
from .views import SpatialFeatureView

urlpatterns = [
    path('features/', SpatialFeatureView.as_view(), name='spatial-features'),
]