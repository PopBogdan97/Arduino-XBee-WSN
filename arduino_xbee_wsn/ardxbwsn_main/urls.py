from django.urls import path
from ardxbwsn_main import views
from rest_framework import routers
from .api import SensorViewSet

router = routers.DefaultRouter()
router.register('api/sensors', SensorViewSet, 'sensors')



urlpatterns = router.urls