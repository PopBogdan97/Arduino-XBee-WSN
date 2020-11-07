from django.urls import path
from dashboard import views

urlpatterns = [
    path('dashboard/', views.charts, name='charts'),
    path('dashboard/<int:sensor_id>/', views.charts_detail, name='charts_detail'),
]