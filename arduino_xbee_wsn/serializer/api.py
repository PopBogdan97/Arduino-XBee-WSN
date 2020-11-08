from dashboard.models import Sensor
from rest_framework import viewsets, permissions
from .serializers import SensorSerializer

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SensorSerializer