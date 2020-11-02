from django.db import models

# Create your models here.

class Sensor(models.Model):
    sensor_id = models.IntegerField()
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    timestamp = models.IntegerField()