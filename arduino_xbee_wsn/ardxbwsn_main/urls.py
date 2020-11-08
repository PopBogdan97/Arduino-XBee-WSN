from django.urls import path
from ardxbwsn_main import views

urlpatterns = [
    path('sensors/', views.sensor_list),
    path('sensors/<int:pk>/', views.sensor_detail),
]